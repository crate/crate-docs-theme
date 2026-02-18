/**
 * Swup Integration Module
 *
 * Implements client-side page transitions using Swup to avoid full page
 * reloads within a documentation section. Only the main content area
 * (main.sb-main) is replaced; the sidebar lives outside it and is
 * preserved naturally, keeping the user's scroll position intact.
 *
 * Cross-section navigation falls back to a full page reload;
 * sidebar scroll is bridged across that reload via sessionStorage
 * (see custom.js).
 *
 * See:
 * - Swup: https://swup.js.org/
 * - Morph Plugin: https://swup.js.org/plugins/morph-plugin
 */

import Swup from 'swup';
import SwupMorphPlugin from 'swup-morph-plugin';

const SIDEBAR_SELECTOR = '.sidebar-tree';
const MAIN_CONTAINER_SELECTOR = 'main.sb-main';
const SWUP_LINK_SELECTOR = `${MAIN_CONTAINER_SELECTOR} a[href], ${SIDEBAR_SELECTOR} a.reference.internal[href], ${SIDEBAR_SELECTOR} a.current-active[href]`;
const DOWNLOADABLE_FILE_EXTENSIONS = /\.(pdf|zip|exe|dmg|tar|gz)$/i;

// Monotonic token used to ignore stale async sidebar-sync completions when
// multiple Swup navigations happen in quick succession.
let sidebarSyncRunId = 0;

/** Reinitialize interactive elements after Swup replaces page content. */
function reinitializeAfterSwap({ pageData = null, allowFetchFallback = true } = {}) {
    // Intentional fire-and-forget: sidebar sync should not block page rendering.
    void syncSidebarCurrentStateFromFetchedPage(pageData, allowFetchFallback);

    // Trigger any Sphinx-specific initializations
    if (window.Sphinx && typeof window.initSearch === 'function') {
        try {
            window.initSearch();
        } catch {
            // Search initialization might not be available
        }
    }
}

/** Extract the sidebar-tree element from a Swup page payload. */
function getFetchedSidebarFromPageData(pageData) {
    if (!pageData) {
        return null;
    }

    if (pageData.document) {
        return pageData.document.querySelector(SIDEBAR_SELECTOR);
    }

    if (typeof pageData.html === 'string') {
        const parsed = new DOMParser().parseFromString(pageData.html, 'text/html');
        return parsed.querySelector(SIDEBAR_SELECTOR);
    }

    return null;
}

/** Check if an href is empty, a fragment, mailto, or javascript URI. */
function isNonNavigableHref(href) {
    return !href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('javascript:');
}

/** Resolve an href to a canonical pathname for comparison (strips .html, trailing slash). */
function normalizeHrefPath(href, baseUrl) {
    if (isNonNavigableHref(href)) {
        return null;
    }
    try {
        const url = new URL(href, baseUrl);
        return url.pathname
            .replace(/\/index\.html$/, '/')
            .replace(/\.html$/, '')
            .replace(/\/$/, '');
    } catch {
        return null;
    }
}

/**
 * Resolve an href to a local absolute path, or return the href as-is
 * for non-navigable/external URLs.
 */
function resolveLocalHref(href, baseUrl) {
    if (isNonNavigableHref(href)) {
        return href;
    }
    try {
        const url = new URL(href, baseUrl);
        if (url.origin !== window.location.origin) {
            return href;
        }
        return `${url.pathname}${url.search}${url.hash}`;
    } catch {
        return href;
    }
}

/** Convert all navigable sidebar links to absolute local paths. */
function absolutizeSidebarLinks(baseUrl = window.location.href) {
    const sidebar = document.querySelector(SIDEBAR_SELECTOR);
    if (!sidebar) {
        return;
    }

    sidebar.querySelectorAll('a[href]').forEach((anchor) => {
        const href = anchor.getAttribute('href') || '';
        if (!isNonNavigableHref(href)) {
            anchor.setAttribute('href', resolveLocalHref(href, baseUrl));
        }
    });
}

/**
 * Sync current-state classes from fetched sidebar to live sidebar by index.
 * Both sidebars must have the same number of anchors.
 */
function syncClassesByIndex(liveSidebar, liveAnchors, fetchedAnchors) {
    const baseUrl = window.location.href;

    liveAnchors.forEach((liveAnchor, index) => {
        const fetchedAnchor = fetchedAnchors[index];

        // Sync hrefs from fetched sidebar (fixes self-referencing "#" links).
        const fetchedHref = fetchedAnchor.getAttribute('href') || '';
        liveAnchor.setAttribute('href', resolveLocalHref(fetchedHref, baseUrl));

        liveAnchor.classList.toggle('current', fetchedAnchor.classList.contains('current'));

        const liveItem = liveAnchor.closest('li');
        const fetchedItem = fetchedAnchor.closest('li');
        if (liveItem && fetchedItem) {
            liveItem.classList.toggle('current', fetchedItem.classList.contains('current'));
            liveItem.classList.toggle('current-page', fetchedItem.classList.contains('current-page'));
        }
    });

    // Ensure only one active leaf link is highlighted.
    liveSidebar.querySelectorAll('a.current-active').forEach((el) => {
        el.classList.remove('current-active');
    });
    const currentPageAnchors = liveSidebar.querySelectorAll('li.current-page > a[href]');
    if (currentPageAnchors.length > 0) {
        currentPageAnchors[currentPageAnchors.length - 1].classList.add('current-active');
    }
}

/**
 * Mark an anchor and its ancestor <li> elements with current-state classes.
 */
function markAnchorAsCurrent(anchor, liveSidebar) {
    anchor.classList.add('current-active');

    let cursor = anchor.closest('li');
    let depth = 0;
    while (cursor && liveSidebar.contains(cursor) && depth < 20) {
        cursor.classList.add('current');
        if (depth === 0) {
            cursor.classList.add('current-page');
        }
        cursor = cursor.parentElement?.closest('li');
        depth += 1;
    }
}

/**
 * Find the live sidebar anchor that corresponds to the fetched sidebar's
 * current page. Matches by normalized path first, falls back to text content.
 */
function findCurrentAnchorByFallback(liveSidebar, fetchedSidebar) {
    // Identify the deepest current-page anchor in the fetched sidebar.
    const fetchedCurrentAnchors = fetchedSidebar.querySelectorAll('li.current-page > a[href]');
    if (fetchedCurrentAnchors.length === 0) {
        return null;
    }
    const fetchedCurrentAnchor = fetchedCurrentAnchors[fetchedCurrentAnchors.length - 1];

    const baseUrl = window.location.href;
    const fetchedHref = fetchedCurrentAnchor.getAttribute('href') || '';
    const fetchedPath = normalizeHrefPath(fetchedHref, baseUrl);
    const fetchedText = (fetchedCurrentAnchor.textContent || '').trim();

    // Scan live sidebar: prefer path match, accept text match as fallback.
    let textMatch = null;
    for (const anchor of liveSidebar.querySelectorAll('a[href]')) {
        const anchorHref = anchor.getAttribute('href') || '';
        const anchorPath = normalizeHrefPath(anchorHref, baseUrl);

        if (fetchedHref !== '#' && anchorHref !== '#' && fetchedPath && anchorPath && fetchedPath === anchorPath) {
            return anchor;
        }

        if (!textMatch && fetchedText && (anchor.textContent || '').trim() === fetchedText) {
            textMatch = anchor;
        }
    }

    return textMatch;
}

/**
 * Update the live sidebar's current-page highlighting to match the newly
 * navigated page. Compares the live sidebar against the fetched page's
 * sidebar: uses index-based sync when structures match (fast path), or
 * falls back to path/text matching when they differ.
 */
async function syncSidebarCurrentStateFromFetchedPage(pageData = null, allowFetchFallback = true) {
    const runId = ++sidebarSyncRunId;

    // Locate the live sidebar in the current document.
    const liveSidebar = document.querySelector(SIDEBAR_SELECTOR);
    if (!liveSidebar) {
        return;
    }

    try {
        // Prefer Swup's already-fetched page payload to avoid extra requests.
        let fetchedSidebar = getFetchedSidebarFromPageData(pageData);

        // Fallback only when page payload is unavailable.
        if (!fetchedSidebar && allowFetchFallback) {
            const response = await fetch(window.location.href, {
                headers: { 'X-Requested-With': 'swup-sidebar-sync' },
            });
            if (!response.ok) {
                return;
            }

            const html = await response.text();
            const parsed = new DOMParser().parseFromString(html, 'text/html');
            fetchedSidebar = parsed.querySelector(SIDEBAR_SELECTOR);
        }

        if (!fetchedSidebar) {
            return;
        }

        if (runId !== sidebarSyncRunId) {
            return;
        }

        // Reset current-state classes before applying new ones.
        liveSidebar.querySelectorAll('.current, .current-active, .current-page').forEach((el) => {
            el.classList.remove('current', 'current-active', 'current-page');
        });

        const liveAnchors = Array.from(liveSidebar.querySelectorAll('a[href]'));
        const fetchedAnchors = Array.from(fetchedSidebar.querySelectorAll('a[href]'));

        // Fast path: synchronize item-by-item when sidebar structures align.
        if (liveAnchors.length === fetchedAnchors.length && liveAnchors.length > 0) {
            syncClassesByIndex(liveSidebar, liveAnchors, fetchedAnchors);
            absolutizeSidebarLinks(window.location.href);
            return;
        }

        // Fallback: when sidebar structures differ (e.g. cross-project navigation),
        // find the current page's anchor in the live sidebar by matching against
        // the fetched sidebar's active link.
        const liveCurrentAnchor = findCurrentAnchorByFallback(liveSidebar, fetchedSidebar);
        if (!liveCurrentAnchor) {
            return;
        }

        markAnchorAsCurrent(liveCurrentAnchor, liveSidebar);
        absolutizeSidebarLinks(window.location.href);
    } catch (e) {
        console.warn('Swup: Could not sync sidebar current state', e);
    }
}

/** Initialize Swup for client-side navigation within the current docs root. */
export function initSwup() {
    if (!('fetch' in window)) {
        console.warn('Swup: Browser does not support fetch API. Falling back to standard page reloads.');
        return null;
    }

    if (!document.querySelector(MAIN_CONTAINER_SELECTOR)) {
        console.warn('Swup: Could not find main content container (main.sb-main). Skipping initialization.');
        return null;
    }

    try {
        const rootPath = window.location.pathname.replace(/[^/]*$/, '');

        const swup = new Swup({
            // Container to swap on page navigation
            containers: [MAIN_CONTAINER_SELECTOR],

            // Only intercept links we know belong to this documentation page shell
            linkSelector: SWUP_LINK_SELECTOR,

            // Ignore links outside current docs root or unsupported targets
            ignoreVisit: (href, { el } = {}) => {
                if (!el || !(el instanceof HTMLAnchorElement)) {
                    return true;
                }

                const relAttr = el.getAttribute('rel') || '';
                if (el.target === '_blank' || relAttr.includes('external')) {
                    return true;
                }

                if (el.hasAttribute('download')) {
                    return true;
                }

                const rawHref = el.getAttribute('href') || '';
                if (isNonNavigableHref(rawHref)) {
                    return true;
                }
                if (DOWNLOADABLE_FILE_EXTENSIONS.test(rawHref)) {
                    return true;
                }

                let targetUrl;
                try {
                    targetUrl = new URL(href, window.location.origin);
                } catch {
                    return true;
                }

                if (targetUrl.origin !== window.location.origin) {
                    return true;
                }

                return !targetUrl.pathname.startsWith(rootPath);
            },

            // Morph main content in-place rather than replacing it wholesale,
            // which avoids layout thrash and preserves focus/scroll in the content area.
            plugins: [new SwupMorphPlugin()],

            // Disable animation detection warnings when no transition-* classes exist
            animationSelector: false,
        });

        absolutizeSidebarLinks(window.location.href);
        reinitializeAfterSwap({ allowFetchFallback: false });

        // Handle post-navigation initialization.
        // Note: the sidebar (.sidebar-sticky) lives outside main.sb-main so Swup never
        // touches it; its scrollTop is preserved naturally across same-section navigations.
        // Cross-section navigations trigger a full page reload; sessionStorage is used
        // to restore scroll across that reload (see custom.js).
        swup.hooks.on('content:replace', (_visit, { page } = {}) => {
            reinitializeAfterSwap({ pageData: page });
        });

        return swup;
    } catch (error) {
        console.error('Swup: Initialization failed', error);
        return null;
    }
}

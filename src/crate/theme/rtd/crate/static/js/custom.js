/**
 * Custom theme JavaScript.
 *
 * Handles:
 * - Sidebar TOC scroll preservation across Swup navigations and full-page reloads
 * - Dark/light theme switching (persisted in localStorage)
 * - TOC expand/collapse behaviour
 * - Swup initialization
 */

import { initSwup } from './swup';

const SIDEBAR_SCROLL_KEY = 'crate-sidebar-scroll';

/**
 * Save sidebar scroll position to sessionStorage before page unload.
 * This enables scroll preservation across full-page reloads (cross-section navigation).
 */
function saveSidebarScrollBeforeUnload() {
    const sidebarSticky = document.querySelector('.sidebar-sticky');
    if (sidebarSticky && sidebarSticky.scrollTop > 0) {
        try {
            sessionStorage.setItem(SIDEBAR_SCROLL_KEY, String(sidebarSticky.scrollTop));
        } catch {
            // sessionStorage might not be available
        }
    }
}

/**
 * Restore sidebar scroll position from sessionStorage after page load.
 * Called after DOMContentLoaded to ensure the sidebar is rendered.
 */
function restoreSidebarScrollFromSessionStorage() {
    try {
        const savedScroll = sessionStorage.getItem(SIDEBAR_SCROLL_KEY);
        if (!savedScroll) {
            return;
        }
        const scrollValue = parseInt(savedScroll, 10);
        if (isNaN(scrollValue) || scrollValue <= 0) {
            return;
        }

        // Clear once used (one-shot restore)
        sessionStorage.removeItem(SIDEBAR_SCROLL_KEY);

        const sidebarSticky = document.querySelector('.sidebar-sticky');
        if (sidebarSticky) {
            sidebarSticky.scrollTop = scrollValue;
        }
    } catch {
        // sessionStorage might not be available
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Restore sidebar scroll before any other initialization
    restoreSidebarScrollFromSessionStorage();

    // Save sidebar scroll position before navigating away (handles cross-section full reloads)
    window.addEventListener('beforeunload', saveSidebarScrollBeforeUnload);

    // Initialize Swup for client-side navigation
    // Progressive enhancement: if initialization throws, keep standard
    // full-page navigation and continue running other page scripts.
    try {
        window.swup = initSwup();
    } catch (error) {
        console.warn('Swup initialization failed; falling back to full-page navigation:', error);
    }

    // Function to set the theme
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    }

    // Function to initialize the theme
    function initTheme() {
        // Check for saved theme in localStorage
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            // Use saved theme
            setTheme(savedTheme);
        } else {
            // No saved theme, use the system preference
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            setTheme(prefersDark ? 'dark' : 'light');
        }
    }

    // Listen for changes in the system preference
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (event) => {
        if (!localStorage.getItem('theme')) {
            // Only change if there's no theme saved in localStorage
            setTheme(event.matches ? 'dark' : 'light');
        }
    });

    // Initialize theme on page load
    initTheme();

    // Ensure the path to the current page is always expanded in the TOC.
    // This matters both for direct URL loads and non-swup fallbacks.

    document.querySelectorAll('.sidebar-tree li.current > .toctree-checkbox').forEach((checkbox) => {
        checkbox.checked = true;
    });

    // Auto-expand sections marked with data-auto-expand="true"
    // Used for Database Drivers when viewing a driver project.

    document.querySelectorAll('[data-auto-expand="true"]').forEach((li) => {
        const checkbox = li.querySelector('.toctree-checkbox');
        if (checkbox) {
            checkbox.checked = true;
        }
    });

    // Make clicking the link text expand the section and collapse siblings.
    // This provides consistent UX: clicking any title shows only that section's
    // children, matching what happens with cross-project navigation.
    document.querySelectorAll('.bs-docs-sidenav li.has-children > a, .bs-docs-sidenav li.has-children > .reference').forEach((link) => {
        link.addEventListener('click', () => {
            const li = link.parentElement;
            const checkbox = li.querySelector('.toctree-checkbox');

            // Collapse sibling sections at the same level
            const parent = li.parentElement;
            if (parent) {
                parent.querySelectorAll(':scope > li.has-children > .toctree-checkbox').forEach((siblingCheckbox) => {
                    if (siblingCheckbox !== checkbox && siblingCheckbox.checked) {
                        siblingCheckbox.checked = false;
                    }
                });
            }

            // Expand this section
            if (checkbox) {
                checkbox.checked = true;
            }

        });
    });

    // Cross-project navigation: clicking expand icon on entries with empty <ul>
    // should navigate to that project instead of just toggling the checkbox.
    // It's ok UX, but also just plain needed as we can't expand the TOC of another project :-(
    document.querySelectorAll('.bs-docs-sidenav li.has-children > label').forEach((label) => {
        label.addEventListener('click', (e) => {
            const li = label.parentElement;
            const ul = li.querySelector(':scope > ul');
            // Check if <ul> is empty (cross-project entry)
            if (ul && ul.children.length === 0) {
                const link = li.querySelector(':scope > a');
                if (link && link.href) {
                    e.preventDefault();
                    e.stopPropagation();
                    window.location.href = link.href;
                }
            }
            // If <ul> has children, default behavior (toggle checkbox) applies
        });
    });

    // Handle clicks on the "current" page link (marked with .current-active class).
    // Uses event delegation so it keeps working after Swup navigations update
    // the sidebar's current-active class to a different element.
    // - href="#": prevent browser's default fragment scroll; re-navigate via Swup instead
    // - Any other href: let Swup (or the browser) handle it normally
    document.addEventListener('click', (e) => {
        const a = e.target.closest('a.current-active');
        if (!a) {
            return;
        }
        if (a.getAttribute('href') === '#') {
            e.preventDefault();
            if (window.swup) {
                window.swup.navigate(window.location.pathname);
            }
        }
    }, false);

    // Mark current-state classes for Overview-like entries in sidebar tree
    // The overview content lives in index.md but Sphinx only marks toctree entries
    // as "current" when the pagename matches. Since the Overview href is rewritten
    // to "#" (self) on the root page, we detect that and add the current class.
    document.querySelectorAll('.sidebar-tree .toctree-l1 > a[href="#"]').forEach((a) => {
        a.classList.add('current');
        a.closest('li').classList.add('current');
    });
});

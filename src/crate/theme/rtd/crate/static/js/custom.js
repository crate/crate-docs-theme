/**
 * This JS file is for additional new JS built over the existing theme
 * ...so as to avoid breaking anything unexpectedly
 */

var Cookies = require('js-cookie');

document.addEventListener('DOMContentLoaded', () => {
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

    //
    // Preserve navigation state (left navbar) across page loads.
    //
    function saveNavState() {
        const checkboxes = document.querySelectorAll('.toctree-checkbox');
        const states = {};
        checkboxes.forEach((checkbox) => {
            if (checkbox.id) {
                states[checkbox.id] = checkbox.checked;
            }
        });
        try {
            localStorage.setItem('navState', JSON.stringify(states));
        } catch (e) {
            // Could be QuotaExceededError or other storage error
            console.warn('Could not save navigation state to localStorage:', e);
        }
    }

    function restoreNavState() {
        const savedStates = localStorage.getItem('navState');
        if (savedStates) {
            let states;
            try {
                states = JSON.parse(savedStates);
            } catch (e) {
                // If parsing fails, clear the corrupted data and do not restore state
                localStorage.removeItem('navState');
                return;
            }
            Object.keys(states).forEach((id) => {
                const checkbox = document.getElementById(id);
                if (checkbox) {
                    checkbox.checked = states[id];
                }
            });
        }
    }

    // Restore state on page load
    restoreNavState();

    // Save state when checkboxes change
    document.querySelectorAll('.toctree-checkbox').forEach((checkbox) => {
        checkbox.addEventListener('change', saveNavState);
    });

    // Make clicking the link text expand the section if collapsed, then navigate
    // Design: Click expands collapsed sections AND navigates to the page.
    // Already-expanded sections just navigate (no toggle). This allows users to
    // expand nested navigation while browsing, without collapsing sections they
    // want to keep visible.
    document.querySelectorAll('.bs-docs-sidenav li.has-children > a, .bs-docs-sidenav li.has-children > .reference').forEach((link) => {
        link.addEventListener('click', () => {
            const li = link.parentElement;
            const checkbox = li.querySelector('.toctree-checkbox');
            if (checkbox && !checkbox.checked) {
                // Only expand if collapsed - navigation proceeds regardless
                checkbox.checked = true;
                saveNavState();
            }
        });
    });
});

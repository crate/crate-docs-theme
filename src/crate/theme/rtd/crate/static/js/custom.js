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

    // Auto-expand sections marked with data-auto-expand="true"
    // Used for Database Drivers when viewing a driver project.
    // Only auto-expand if user hasn't explicitly set a preference for this checkbox.
    const savedStates = localStorage.getItem('navState');
    let userPreferences = {};
    if (savedStates) {
        try {
            userPreferences = JSON.parse(savedStates);
        } catch (e) {
            // Ignore parse errors, treat as no preferences
        }
    }
    let autoExpandStateChanged = false;

    document.querySelectorAll('[data-auto-expand="true"]').forEach((li) => {
        const checkbox = li.querySelector('.toctree-checkbox');
        if (checkbox && checkbox.id) {
            // Only auto-expand if user has no saved preference for this checkbox
            if (!(checkbox.id in userPreferences)) {
                checkbox.checked = true;
                autoExpandStateChanged = true;
            }
        }
    });

    // Save the auto-expanded state so it persists
    if (autoExpandStateChanged) {
        saveNavState();
    }

    // Save state when checkboxes change
    document.querySelectorAll('.toctree-checkbox').forEach((checkbox) => {
        checkbox.addEventListener('change', saveNavState);
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

            saveNavState();
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
});

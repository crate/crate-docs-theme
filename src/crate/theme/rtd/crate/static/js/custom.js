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
});

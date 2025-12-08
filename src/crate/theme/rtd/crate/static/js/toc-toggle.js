/**
 * TOC Navigation Expand/Collapse Toggle
 *
 * This module adds interactive expand/collapse functionality to the table of
 * contents (TOC) navigation sidebar. It allows users to click on parent items
 * to show/hide their children.
 *
 * Features:
 * - Click on items with children to toggle expand/collapse
 * - Auto-expand current page's parent hierarchy
 * - Add .has-children class for browsers without :has() support
 * - ARIA attributes for accessibility
 */

/**
 * Initialize TOC toggle behavior
 */
function initTocToggle() {
  // Only initialize if the toc-toggle-icons-enabled class is present
  const sidebar = document.querySelector('.toc-toggle-icons-enabled .bs-docs-sidenav');
  if (!sidebar) {
    return;
  }

  const tocItems = sidebar.querySelectorAll('.toctree li');

  let itemsWithChildren = 0;
  tocItems.forEach(item => {
    // Check if item has direct ul children (already rendered)
    const hasDirectChildren = item.querySelector(':scope > ul');

    // Check if the link suggests this is a parent page (links to index.html or has children)
    const link = item.querySelector(':scope > a');
    const linkHref = link ? link.getAttribute('href') : '';
    const linksToIndex = linkHref && (linkHref.endsWith('/index.html') || linkHref.includes('/index.html#'));

    // Check if this item is alone in its parent <ul> (no siblings)
    // Items with children are typically alone in their own <ul> block
    const parentUl = item.parentElement;
    const siblings = parentUl ? parentUl.querySelectorAll(':scope > li') : [];
    const isAloneInUl = siblings.length === 1;

    // Determine if item has or could have children:
    // - Has direct children already rendered, OR
    // - Links to index.html AND is alone in its <ul> (likely a section with children)
    const hasChildren = hasDirectChildren || (linksToIndex && isAloneInUl);

    if (!hasChildren) return;

    itemsWithChildren++;

    // Add .has-children class for browsers without :has() support
    item.classList.add('has-children');

    // Link was already found above, skip if not found
    if (!link) return;

    // Determine initial state
    const isCurrentPath = item.classList.contains('current') ||
                          item.classList.contains('active');

    // Mark as expanded if in current path, otherwise collapsed
    if (isCurrentPath) {
      item.classList.add('expanded');
    }

    // Initialize ARIA attribute
    link.setAttribute('aria-expanded', item.classList.contains('expanded').toString());

    // Add click handler to toggle expansion (only if item has direct children to toggle)
    if (hasDirectChildren) {
      link.addEventListener('click', (e) => {
        // Check if clicking on the icon area (right side)
        const linkRect = link.getBoundingClientRect();
        const clickX = e.clientX - linkRect.left;
        const linkWidth = linkRect.width;

        // If clicking in the last 30px (icon area), toggle instead of navigate
        if (clickX > linkWidth - 30) {
          e.preventDefault();
          toggleItem(item, link);
        }
      });
    }
    // For items that link to index.html but don't have children rendered yet,
    // clicking the icon will navigate to the page (normal link behavior)
  });
}

/**
 * Toggle expand/collapse state of a TOC item
 * @param {HTMLElement} item - The list item element
 * @param {HTMLElement} link - The anchor element
 */
function toggleItem(item, link) {
  const isExpanded = item.classList.toggle('expanded');
  // Force a reflow to ensure the browser applies the new CSS rules immediately.
  void item.offsetHeight;
  link.setAttribute('aria-expanded', isExpanded.toString());
}

// Run after DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initTocToggle);
} else {
  // DOM already loaded
  initTocToggle();
}

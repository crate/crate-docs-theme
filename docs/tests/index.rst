.. _tests:

#########################
Navigation bar test pages
#########################

**Same-project entries (entries with actual TOC content):**

1. Clicking the title expands the section, collapses sibling sections at the
   same level, and navigates to the section page
2. Clicking just the icon expands/collapses that section without navigating
3. Clicking the icon for an expanded section collapses it, leaving other
   expanded sections unchanged

**Cross-project entries (entries linking to other projects):**

4. Clicking the title navigates to that project
5. Clicking just the icon also navigates to that project (since the TOC
   content from another project isn't available to expand)

**Visual feedback:**

6. Hovering the mouse over an icon shows a fade background behind the icon
7. Hovering the mouse over the title shows a fade background behind the title
   and the icon
8. The current page is highlighted in the navigation bar

**Auto-expansion:**

9. The Database Drivers section auto-expands when viewing a driver project
   (only on first visit; user preference is respected thereafter)


**Pages:**

.. toctree::
    :titlesonly:
    :glob:

    section1/index
    section2/index
    *

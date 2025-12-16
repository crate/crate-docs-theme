.. _tests:

###########################
Navigation bar test pages
###########################

1. Clicking the title should expand the section and navigate to the section page
2. Clicking just the icon should expand but not navigate to the section
3. Clicking just the icon for an expanded section should collapse that section and leave other expanded sections expanded
4. Hovering the mouse over an icon should show a fade background behind the icon
5. Hovering the mouse over the title should show a fade background behind the title and the icon
6. The current page should be highlighted in the navigation bar as the user navigates through the pages below.


**Pages:**

.. toctree::
    :titlesonly:
    :glob:

    section1/index
    section2/index
    *

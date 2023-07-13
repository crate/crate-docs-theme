.. _index:

###########################
CrateDB documentation theme
###########################

*****
About
*****

A theme component for the `Sphinx static documentation generator`_.

Example documentation sections:

- https://crate.io/docs/crate/reference/
- https://crate.io/docs/python/en/latest/

********
Overview
********

This section outlines a few features, elements, and style-guides by example.

Classic Sphinx / reStructuredText
=================================

.. toctree::
    :maxdepth: 1

    headings
    admonitions
    lists
    tables
    links
    images
    diagrams
    codesnippets
    subpage
    glossary


Modern components
=================

.. toctree::
    :maxdepth: 1

    myst-overview
    design-markdown
    design-restructuredtext
    mermaid-diagrams-markdown
    mermaid-diagrams-restructuredtext


*******
Details
*******

.. meta::
    :description lang=en:
        This is the meta description, it should be between 150-300 characters.
        Meta descriptions are used for display but not for ranking.

This is a sample documentation project that can be used for visually testing
the theme.

How to use this documentation:

- Verify that each page element displays correctly. Some page elements identify
  themselves (e.g., the :ref:`index`) and some elements describe how they ought
  to appear (e.g., the :ref:`first admonition <first-admonition>`).

How to improve this documentation:

- If you notice any bugs, please `report an issue`_ or create a PR to fix them.

- Add page elements and use the available text to describe how the element
  should be displayed.


.. NOTE::

    To learn how to run sandbox or CI builds as a part of your testing and *Quality
    Assurance* (QA) workflow, see the `developer guide`_.


.. _developer guide: https://github.com/crate/crate-docs-theme/blob/main/DEVELOP.rst
.. _report an issue: https://github.com/crate/crate-docs-theme/issues/new
.. _Sphinx static documentation generator: https://www.sphinx-doc.org/

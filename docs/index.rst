.. _index:

###########################
CrateDB Documentation Theme
###########################

    Sphinx makes it easy to create intelligent and beautiful documentation.

A theme component for the `Sphinx`_ static documentation generator used by
the `CrateDB Documentation`_ across the board.

.. rubric:: Introduction

.. toctree::
    :maxdepth: 1

    authoring
    links


.. rubric:: Style Guides

A few markup snippets by example.


Modernized
==========

A side-by-side gallery demonstrating both reStructuredText and Markedly
Structured Text syntax.

.. grid::

    .. grid-item::
        :columns: 6

        .. toctree::
            :titlesonly:

            rst/index

    .. grid-item::
        :columns: 6

        .. toctree::
            :titlesonly:

            myst/index


Legacy
======

The legacy feature gallery exclusively uses reStructuredText.

.. toctree::
    :maxdepth: 1

    admonitions
    codesnippets
    diagrams
    glossary
    headings
    images
    lists
    projects
    subpage
    tables
    typography



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
  to appear (e.g., the :ref:`admonition gallery <admonition-gallery>`).

How to improve this documentation:

- If you notice any bugs, please `report an issue`_ or create a PR to fix them.

- Add page elements and use the available text to describe how the element
  should be displayed.


.. NOTE::

    To learn how to run sandbox or CI builds as a part of your testing and *Quality
    Assurance* (QA) workflow, see the `developer guide`_.


.. _CrateDB Documentation: https://cratedb.com/docs/
.. _developer guide: https://github.com/crate/crate-docs-theme/blob/main/DEVELOP.rst
.. _report an issue: https://github.com/crate/crate-docs-theme/issues/new
.. _Sphinx: https://www.sphinx-doc.org/

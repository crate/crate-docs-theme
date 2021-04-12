.. _index:

==========
Page Title
==========

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

    For help building this documentation as a part of your testing and *Quality
    Assurance* (QA) workflow, see the `developer guide`_.

.. rubric:: Table of Contents

.. contents::
   :local:


.. _top-level-heading:

Top-level heading
=================

.. _first-admonition:

.. NOTE::

    This is the first paragraph of a note admonition. The admonition is
    visually set off from the rest of the content and has a colored background.

    This is a second paragraph. To the left of both paragraphs, there is an
    icon that represents the concept of a "note".


.. _second-level-heading:

Second-level heading
--------------------

.. _closed-list:

This is a closed list:

* It has bullet points like this one
* The list items are spaced close together like subsequent lines in a paragraph
* Typically the items are short and are not terminated with a period

.. _open-list:

An open list is quite different:

.. rst-class:: open

* Notice how this sentence is terminated with a period.

  And there's a second paragraph too.

* This is the second item. Notice how it is separated from the first item like
  a regular paragraph would be.

This is a regular paragraph and not a list item.


.. _third-level-heading:

Third-level heading
~~~~~~~~~~~~~~~~~~~

.. NOTE::

    Here's a regular list:

    - This is the first list item
    - The list items are spaced close together like subsequent lines in a
      paragraph
    - This list is styled the same as the :ref:`closed list <closed-list>`
      above

    This is an open list:

     .. rst-class:: open

     - This list looks the same as the :ref:`open list <closed-list>` above

     - The list items are separated as if they were separate paragraphs


.. _fourth-level-heading:

Fourth-level heading
^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    subpage

    glossary
    links

This paragraph contains a link to the :ref:`foo <gloss-foo>` glossary entry
that should be styled black with a dotted underline to make it less prominent
and distinguish it from normal internal links.


.. _fifth-level-heading:

Fifth-level heading
...................

This is the deepest heading level we support.


.. _developer guide: https://github.com/crate/crate-docs-theme/blob/master/DEVELOP.rst#user-content-make-changes
.. _report an issue: https://github.com/crate/crate-docs/issues/new

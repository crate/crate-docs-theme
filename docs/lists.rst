========================
Different kinds of lists
========================

.. contents::
   :local:

Bullet lists
============

Basics
------

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


With admonition
---------------

These are lists within admonitions.

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


Enumerated lists
================

This demonstrates an auto-enumerated list with a nested bullet-list.

#. Item 1

   - Sub item 1
   - Sub item 2

#. Item 2

   - Sub item 1
   - Sub item 2

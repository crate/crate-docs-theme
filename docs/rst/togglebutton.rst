###################
Sphinx Togglebutton
###################


*****
About
*****

`sphinx-togglebutton`_ is a small Sphinx extension to make it possible to add a
"toggle button" to sections of your page. This allows you to:

- Collapse Sphinx admonitions (notes, warnings, etc.) so that their content is
  hidden until users click a toggle button.
- Collapse arbitrary chunks of content on your page with a collapse directive.


********
Examples
********


Collapsed
=========

The default version is to display the collapsed variant of the element.

.. note::
    :class: dropdown

    This is my note.

Opened
======

You may also **show the content by default**.

.. note::
    :class: dropdown, toggle-shown

    This is my note.

Container
=========

You can also use containers to add arbitrary toggle-able code. For example,
here's a container with an image inside.

.. container:: toggle, toggle-hidden

    .. admonition:: Look at that, an image!

        .. image:: https://media.giphy.com/media/mW05nwEyXLP0Y/giphy.gif


.. _sphinx-togglebutton: https://github.com/executablebooks/sphinx-togglebutton

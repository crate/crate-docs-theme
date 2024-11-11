###########
Admonitions
###########


*****
About
*****

Admonitions are visually set off from the rest of the content and have a
colored background. To the left of admonition content paragraphs, there is an
icon that represents the kind/type of the admonition.


********
Variants
********

There are two variants of admonitions.

Regular
=======
Regular admonitions are very compact, and use a smaller font size. They can be
used to convey more detailed information to the reader, even larger amounts of
text, without taking too much screen space, and without obstructing the reading
flow too much.

.. NOTE::

    Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.

Hero
====
On the other hand, `hero-/jumbotron-style`_ admonition components have a bolder
visual appearance. They can be used for showcasing hero unit style content, and
for calling extra attention to featured content or information. They are defined
by adding a ``:class: hero`` option to the markup directive.

.. NOTE::
    :class: hero

    Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.


.. _admonition-gallery:

*******
Gallery
*******

This section demonstrates all available admonition components, in both variants.

Regular
=======

.. NOTE::

    This is the first paragraph of a *note* admonition.

    This is a second paragraph.

.. TIP::

    This is the first paragraph of a *tip* admonition.

    This is a second paragraph.

.. SEEALSO::

    This is the first paragraph of a *seealso* admonition.

.. CAUTION::

    This is the first paragraph of a *caution* admonition.

.. WARNING::

    This is the first paragraph of a *warning* admonition.

.. DANGER::

    This is the first paragraph of a *danger* admonition.



``topic``
=========

.. topic:: This is a topic.

   This is what admonitions are a special case of, according to the docutils
   documentation.

``admonition``
==============

.. admonition:: The one with the custom titles

   It's got a certain charm to it.

``attention``
=============

.. attention::

   Climate change is real.

``caution``
===========

.. caution::

   Cliff ahead: Don't drive off it.

``danger``
==========

.. danger::

   Mad scientist at work!

``error``
=========

.. error::

   Does not compute.

``hint``
========

.. hint::

   Insulators insulate, until they are subject to ______ voltage.

``important``
=============

.. important::

   Tech is not neutral, nor is it apolitical.

``note``
========

.. note::

   This is a note.

``seealso``
===========

.. seealso::

   Other relevant information.

``tip``
=======

.. tip::

   25% if the service is good.

``todo``
========

.. todo::

   This needs the ``sphinx.ext.todo`` extension.

``warning``
===========

.. warning::

   Reader discretion is strongly advised.



Hero
====

.. NOTE::
    :class: hero

    This is the first paragraph of a *note* admonition.

    This is a second paragraph.

.. TIP::
    :class: hero

    This is the first paragraph of a *tip* admonition.

    This is a second paragraph.

.. SEEALSO::
    :class: hero

    This is the first paragraph of a *seealso* admonition.

.. CAUTION::
    :class: hero

    This is the first paragraph of a *caution* admonition.

.. WARNING::
    :class: hero

    This is the first paragraph of a *warning* admonition.

.. DANGER::
    :class: hero

    This is the first paragraph of a *danger* admonition.


With links
==========

.. NOTE::

    `Link to example.com <https://example.com>`_.

.. NOTE::
    :class: hero

    `Link to example.com <https://example.com>`_.


With item lists
===============

.. NOTE::

    - First
    - Second

      - Nested

.. NOTE::
    :class: hero

    - First
    - Second

      - Nested


.. _hero-/jumbotron-style: https://getbootstrap.com/docs/4.1/components/jumbotron/

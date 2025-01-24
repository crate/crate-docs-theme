######
Videos
######

Videos, for example from YouTube or Vimeo, can be embedded using inline
HTML, `sphinxcontrib-youtube`_, or `oembedpy`_.

Inline HTML
===========

This uses a basic ``<iframe ...></iframe>`` HTML markup, just written down
into the Markdown file. Voilà.

.. raw:: html

    <iframe width="480" height="320" src="https://www.youtube-nocookie.com/embed/YE7VzlLtp-4" title="Big Buck Bunny" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

sphinxcontrib-youtube
=====================

This uses the ``youtube`` and ``vimeo`` directives provided by ``sphinxcontrib-youtube``.

.. rubric:: YouTube
.. youtube:: YE7VzlLtp-4

.. rubric:: Vimeo
.. vimeo:: 1084537

oembedpy
========

This uses the ``oembed`` directive provided by ``oembedpy``.

.. oembed:: https://www.youtube.com/watch?v=YE7VzlLtp-4
    :maxwidth: 480
    :maxheight: 320

.. tip::

    See :ref:`oembed-rst` to learn about all capabilities of the ``oembed`` directive.


.. _oEmbedPy: https://oembedpy.readthedocs.io/
.. _sphinxcontrib-youtube: https://sphinxcontrib-youtube.readthedocs.io/

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

This uses the ``youtube`` directive provided by ``sphinxcontrib-youtube``.

.. youtube:: YE7VzlLtp-4
    :width: 480
    :height: 320

oembedpy
========

This uses the ``oembed`` directive provided by ``oembedpy``.

.. oembed:: https://www.youtube.com/watch?v=YE7VzlLtp-4
    :maxwidth: 480
    :maxheight: 320

.. tip::

    `oEmbedPy`_, as the name suggests, can render `oEmbed`_ information provided
    by any HTML page, for example Bluesky, Reddit, Twitter/X, and many more.
    Registered oEmbed providers can be explored per `providers.json`_.


.. _oEmbed: https://oembed.com/
.. _oembedpy: https://oembedpy.readthedocs.io/
.. _providers.json: https://oembed.com/providers.json
.. _sphinxcontrib-youtube: https://sphinxcontrib-youtube.readthedocs.io/

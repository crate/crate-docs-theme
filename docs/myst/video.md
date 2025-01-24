# Videos

Videos, for example from YouTube or Vimeo, can be embedded using inline
HTML, [sphinxcontrib-youtube], or [oembedpy].

## Inline HTML

This uses a basic `<iframe ...></iframe>` HTML markup, just written down
into the Markdown file. Voilà.

<iframe width="480" height="320" src="https://www.youtube-nocookie.com/embed/YE7VzlLtp-4" title="Big Buck Bunny" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## sphinxcontrib-youtube

This uses the `youtube` directive provided by `sphinxcontrib-youtube`.

:::{youtube} YE7VzlLtp-4
:width: 480
:height: 320
:::

## oembedpy

This uses the `oembed` directive provided by `oembedpy`.

:::{oembed} https://www.youtube.com/watch?v=YE7VzlLtp-4
:maxwidth: 480
:maxheight: 320
:::

:::{tip}
[oEmbedPy], as the name suggests, can render [oEmbed] information provided
by any HTML page, for example Bluesky, Reddit, Twitter/X, and many more.
Registered oEmbed providers can be explored per [providers.json].
:::


[oEmbed]: https://oembed.com/
[oembedpy]: https://oembedpy.readthedocs.io/
[providers.json]: https://oembed.com/providers.json
[sphinxcontrib-youtube]: https://sphinxcontrib-youtube.readthedocs.io/

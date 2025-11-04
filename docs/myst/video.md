# Videos

Videos, for example from YouTube or Vimeo, can be embedded using inline
HTML, or [sphinxcontrib-youtube].

## Inline HTML

This uses a basic `<iframe ...></iframe>` HTML markup, just written down
into the Markdown file. Voilà.

<iframe width="480" height="320" src="https://www.youtube-nocookie.com/embed/YE7VzlLtp-4" title="Big Buck Bunny" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## sphinxcontrib-youtube

This uses the `youtube` and `vimeo` directives provided by `sphinxcontrib-youtube`.

:::{rubric} YouTube
:::
:::{youtube} YE7VzlLtp-4
:::

:::{rubric} Vimeo
:::
:::{vimeo} 1084537
:::


[sphinxcontrib-youtube]: https://sphinxcontrib-youtube.readthedocs.io/

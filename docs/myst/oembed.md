(oembed-md)=

# oEmbed widgets


## About

[oEmbed] is a format for allowing an embedded representation of a URL on
third party sites. The simple API allows a website to display embedded
content (such as photos or videos) when a user posts a link to that
resource, without having to parse the resource directly.

Client-side implementations of oEmbed, like [oEmbedPy], can render
[oEmbed] information provided by any HTML page, for example Bluesky,
Reddit, Twitter/X, and many more. Registered oEmbed providers can be
explored per [providers.json].


## Examples

### Bluesky
:::{oembed} https://bsky.app/profile/simonprickett.dev/post/3lgizsidy722u
:::

### Reddit
:::{oembed} https://www.reddit.com/r/Database/comments/1i6umke/comment/m8pptia/
:::

### Twitter/X
:::{oembed} https://x.com/simon_prickett/status/1882858717571641581
:::

### YouTube
:::{oembed} https://www.youtube.com/watch?v=YE7VzlLtp-4
:maxwidth: 480
:maxheight: 320
:::


[oEmbed]: https://oembed.com/
[oEmbedPy]: https://oembedpy.readthedocs.io/
[providers.json]: https://oembed.com/providers.json

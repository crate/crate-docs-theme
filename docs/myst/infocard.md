# Info Card


## About

The [](inv:sde#infocard-directive) is a composite web element from [](inv:sde:*:label#index).

It is a composite component offering a title, description text, and both verbose
and short tags, or other toolkit elements. It is suitable for authoring pages
enumerating items with dense information, without the maintenance nightmares of tables.


## Examples

### Example 1

::::{info-card}

:::{grid-item}
:columns: 8
[example.org/beagles](https://example.org/beagles)

A module for collecting votes from beagles, \
and for consolidating them.

**Author:** C. Schultz, Universal Features Syndicate \
**Contact:** Los Angeles, CA; <cschultz@peanuts.example.org>
:::

:::{grid-item}
:columns: 4

{tags-primary}`foo, bar`

{tags-success}`baz`

{tags-secondary}`qux`

{tags-info}`anything`
:::

::::


### Example 2

::::{info-card}

:::{grid-item}
:columns: 8
[multihop-firmware](https://hiveeyes.org/docs/arduino/firmware/backdoor/multihop/README.html)

A flexible software breadboard for ISM RF packet radio nodes, relays, and gateways.

| **Date:** 2015
| **Source:** multihop.ino
:::

:::{grid-item}
:columns: 4

{tags-primary}`rf69, rf96, lora, beradio`

{tags-success}`hx711, ds18b20, dht22`

{tags-secondary}`ATmega328`

{tags-info}`low-power`
:::

::::


### Example 3

:::::{info-card}

::::{grid-item}
:columns: 8
:class: sd-align-major-spaced
#### Curated picture of the day

A mountain goat with long horns standing on a grassy hill.

:::{div} text-small

**Author:** Jaromír Kalina, Czech Republic, [@jkalina](https://unsplash.com/@jkalina) \
**Exposé:** https://unsplash.com/photos/spdQ1dVuIHw \
**Source:** [Unsplash -- The internet’s source for visuals](https://unsplash.com/)
:::
::::

::::{grid-item}
:columns: 4

[![](https://unsplash.com/photos/spdQ1dVuIHw/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjg5Nzg4MTEzfA&force=true&w=640)](https://unsplash.com/photos/spdQ1dVuIHw)
::::

:::::

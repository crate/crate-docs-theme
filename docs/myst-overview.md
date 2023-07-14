# Overview about MyST - Markedly Structured Text

## About

> A Sphinx and Docutils extension to parse MyST, a rich and extensible flavour
> of Markdown for authoring technical and scientific documentation.
>
> -- https://myst-parser.readthedocs.io/

[MyST](https://myst-parser.readthedocs.io/) is a strict superset of the 
[CommonMark syntax specification](https://spec.commonmark.org/).
It adds features focussed on scientific and technical documentation authoring. {fas}`star2`


### Details

Roles and directives provide a way to extend the syntax of MyST in an unbound 
manner, by interpreting a chunk of text as a specific type of markup, according
to its name.
Directives syntax is defined with triple-backticks and curly-brackets, effectively
a Markdown code fence.

-– [Roles and Directives](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html)

**Example**

> ![image|297x168](https://global.discourse-cdn.com/business7/uploads/crate/original/1X/d61bae27e7ce2ca04ab7ba78954153b885f2548e.png)


## Overview

### Inline quotes / citations

> This text should be quoted.

### Cross-references

Being able to use cross-references appropriately, i.e. optimally linking between
documentation resources, even across projects, is important for documentation
authoring. Please refer to [MyST cross-references](inv:myst#syntax/referencing),
in order to learn about how this works using the Markdown markup language.

By using cross-references properly, maintenance efforts regarding broken links will
be greatly reduced, because all target references will be validated at build time.
See also [How to use cross-references with Sphinx].

[How to use cross-references with Sphinx]: https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html


### Images and figures

#### Documentation
- [sphinx{design} » Images and figures](inv:myst#syntax/images_and_figures)
- {doc}`sphinx{design} » Images and figures <myst:syntax/images_and_figures>`

#### Standard

The standard Markdown syntax for images.

![MyST logo](_static/myst-logo-wide.svg)

#### Adjusting attributes
The `attrs_inline` extension can be used to add attributes to an inline image,
for example, to resize/scale it.

![MyST logo](_static/myst-logo-wide.svg){.bg-warning w=100px align=center}

#### Block level
To create a block image, use the `image` directive.
```{image} https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg
:alt: fishy
:class: bg-primary
:width: 200px
:align: center
```


#### Figures (images with captions)

To create a figure, use the `figure` directive.

```{figure} _static/myst-logo-wide.png
:scale: 50 %
:alt: The MyST logo.

This is the caption of the figure (a simple paragraph).

The legend consists of all elements after the caption. In this
case, the legend consists of this paragraph and the following
table:

| Symbol | Meaning |
| ------ | ------- |
| :logo: | MyST    |
```


### Subfigures

Documentation: https://sphinx-subfigure.readthedocs.io/

:::{subfigure} AA|BC
:layout-sm: A|B|C
:gap: 8px
:subcaptions: above
:name: myfigure
:class-grid: outline

```{image} https://sphinx-subfigure.readthedocs.io/en/latest/_images/A.png
:height: 100px
:alt: Image A
```

```{image} https://sphinx-subfigure.readthedocs.io/en/latest/_images/B.png
:height: 100px
:alt: Image B
```

```{image} https://sphinx-subfigure.readthedocs.io/en/latest/_images/C.png
:height: 100px
:alt: Image C
```

:::


## History - The great dilemma

For a long time, the power of the Sphinx documentation generator was only available
to people writing documentation in reStructuredText. Because Markdown gained
significant popularity in recent years, the community was in a big dilemma, and
surely there have been endless Programming Language Wars-style discussions about
using reStructuredText vs. Markdown for documentation authoring.

This dilemma has come to an end with MyST now, aiming to follow up on the success 
of MySQL and mypy – naming-wise.

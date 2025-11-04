# Images and figures

## Documentation
- [sphinx{design} » Images and figures](inv:myst#syntax/images_and_figures)
- {doc}`sphinx{design} » Images and figures <myst:syntax/images_and_figures>`

## Standard

The standard Markdown syntax for images.

![MyST logo](../_static/myst-logo-wide.svg)

## Adjusting attributes
The `attrs_inline` extension can be used to add attributes to an inline image,
for example, to resize/scale it.

![MyST logo](../_static/myst-logo-wide.svg){.bg-warning w=100px align=center}

## Block level
To create a block image, use the `image` directive.
```{image} https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg
:alt: fishy
:class: bg-primary
:width: 200px
:align: center
```


## Figures (images with captions)

To create a figure, use the `figure` directive.

```{figure} ../_static/myst-logo-wide.png
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

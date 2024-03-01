(crossref)=
(linking)=
(rst-linking)=

# Linking and Referencing with Sphinx

A primer with examples. Enjoy reading.


:::{card}
If you are in a hurry, and just want to have quick access to the link labels
used throughout the documentation of CrateDB, because you are working on a
document where you need it, here you go:
[Crate.io Sphinx Inventory Labels].
:::


## Introduction

Sphinx provides powerful cross-referencing and -linking capabilities on top
of vanilla reStructuredText and Markdown/CommonMark/MyST, mainly on behalf of
its reference subsystem.

The [Sphinx Getting Started] document illustrates the background of Sphinx'
design, and why it is so focused on those references, and the cross-referencing
concept:

> Sphinx is a documentation generator or a tool that translates a set of plain
> text source files into various output formats, automatically producing
> cross-references, indices, etc.
> 
> That is, if you have a directory containing a bunch of reStructuredText or
> Markdown documents, Sphinx can generate a series of HTML files, a PDF file
> (via LaTeX), man pages and much more.
> 
> Sphinx focuses on documentation, in particular handwritten documentation,
> however, Sphinx can also be used to generate blogs, homepages and even books.
> Much of Sphinx’s power comes from the richness of its default plain-text
> markup format, reStructuredText, along with its significant extensibility
> capabilities.

Well, it's like the Web, but much better.


## Reflections

More often than not, you will find yourself in a situation where you can't
exactly remember the right syntax to use efficient linking and cross-referencing
in your favorite markup language, so you are gravitating towards WYSIWYG
authoring tools again, only to realize soon that it does not work too well for
technical writing.

Mostly, it is because the canonical documentation about the markup language
is too thin or scattered, and you just can't figure out how to properly run
a link, referencing either internal references, project-wide references, or
just plain HTTP links.

Well, rest assured, it is not so easy as it sounds, as there are multiple
ways to run links, and you can use all of them, depending on your specific
use-case. Also, because non-standard extensions influence the crossref syntax,
there is no standard for this area of content authoring, so it is easy to get
confused about the topic when not using it on a daily basis. 

This page intends to present the most prominent variants of linking and
referencing in a cheat-sheet-like style, so you can cherry-pick the most
appropriate variant easily.


## Features

Let's get familiar with different ways to run links, also introducing you
to the terms and jargon of Sphinx and its supported markup languages.

:Direct vs. indirect links:

  Direct links define the link target inlined into the markup text.
  Indirect links refer to link labels instead, which can be defined out-of-band,
  for example at the bottom of the file.

:Linking to references:

  With Sphinx, by default, you can link to _documents_, custom _labels_ defined
  in markup text, and labels derived from _code symbols_ when using Sphinx
  autodoc.

:Linking to HTTP:

  Other than Sphinx references, you can also use arbitrary HTTP or other links
  as link targets.

:Linking to other documentations:
  
  In order to run cross-references between different Sphinx projects, or to use
  the compiled index of references for other means, the [intersphinx] feature
  will accompany each documentation with a corresponding inventory file called
  `objects.inv`.

:Custom titles:

  By default, Sphinx will automatically read the link title from the title
  of the target reference. If that isn't what you want, you can specify an
  explicit title.

:HTML links:

  When it comes to markup syntax, you don't necessarily have to use Markdown or
  reStructuredText. In one way or another, you can also use plain HTML to run
  links.

:Links within toctrees:

  Within a [toctree] directive, you can exclusively reference **documents**
  within the **local scope** of your Sphinx project. You can not reference
  any other objects or labels.


## Synopsis

A quick demonstration how defining and using custom link labels in markup text
works.

::::{tab-set}

:::{tab-item} CommonMark/MyST
:sync: md
Define a label.
```markdown
(quick-fox)=

# A quick brown fox
```
Reference a label.
```markdown
Somewhere where [](#quick-fox) and rabbit.
```
:::

:::{tab-item} reStructuredText
:sync: rst
Define a label.
```rst
.. _quick-fox:

=================
A quick brown fox
=================
```
Reference a label.
```rst
Somewhere where :ref:`quick-fox` and rabbit.
```
:::

::::


## Examples

The variety of linking options is best explained by example.

:::{contents}
:local:
:::

### Direct links

Direct links define the link target inlined into the markup text.
See [](#synopsis).


### Indirect links

Indirect links refer to link labels, which can be defined out-of-band,
for example at the bottom of the file. Indirect links to Sphinx references
only work when using MyST.
::::{tab-set}

:::{tab-item} CommonMark/MyST
:sync: md
Define a label.
```markdown
(quick-fox)=

# A quick brown fox
```
Reference a label.
```markdown
Somewhere where [fox] and rabbit.

[fox]: #quick-fox
```
:::

:::{tab-item} reStructuredText
:sync: rst
Indirect links to Sphinx references using reStructuredText are not possible,
or unknown.
:::

::::


### Linking to HTTP

When referencing HTTP links, Sphinx can't read the target title, so you will
need to explicitly define the link title.

::::{tab-set}

:::{tab-item} CommonMark/MyST
:sync: md
A direct link, defined inline.
```markdown
Somewhere where [the quick brown fox](https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog).
```
An indirect link, defined out-of-band.
```markdown
Somewhere where [the quick brown fox].

[the quick brown fox]: https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog
```
:::

:::{tab-item} reStructuredText
:sync: rst
A direct link, defined inline.
```rst
Somewhere where `the quick brown fox <https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog>`_.
```
An indirect link, defined out-of-band.
```rst
Somewhere where `the quick brown fox`_.

.. _the quick brown fox: https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog
```
:::

::::


### Linking to other documentations
[Intersphinx] enables referencing objects in other Sphinx documentations.
Imagine you are on a different project where you can reference objects
from the main project using the inventory label `main-book`.

::::{tab-set}

:::{tab-item} CommonMark/MyST
:sync: md
Reference a label using the `inv` prefix, referencing another "inventory".
```markdown
Somewhere where [](inv:main-book#quick-fox) and rabbit.
```
:::

:::{tab-item} reStructuredText
:sync: rst
Reference a label using the `:ref:` syntax.
```rst
Somewhere where :ref:`main-book:quick-fox` and rabbit.
```
:::

::::


### Custom titles
You can specify an explicit title for a link if you don't want that
Sphinx automatically uses the target headline as title.
::::{tab-set}

:::{tab-item} CommonMark/MyST
:sync: md
Define a label.
```markdown
(quick-fox)=

# A quick brown fox
```
Reference a label.
```markdown
Somewhere [over the rainbow](#quick-fox).
```
:::

:::{tab-item} reStructuredText
:sync: rst
Define a label.
```rst
.. _quick-fox:

=================
A quick brown fox
=================
```
Reference a label using the `:ref:` syntax.
```rst
Somewhere :ref:`over the rainbow <quick-fox>`.
```
:::

::::


### HTML links

If you are not bothering about writing links in any markup syntax, or if you
have special formatting requirements, you can also use HTML if you absolutely
have to.

::::{tab-set}

:::{tab-item} CommonMark/MyST
:sync: md
A HTML link, defined in Markdown.
Just write it down.
```markdown
Somewhere where <a href="https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog">the quick brown fox</a>.
```
:::

:::{tab-item} reStructuredText
:sync: rst
A HTML link, defined in reStructuredText.
Needs corresponding markup.
```rst
.. raw:: html

    Somewhere where <a href="https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog">the quick brown fox</a>.
```
:::

::::

:::{note}
Please note markup like this will not be available to alternative renderers
other than the HTML renderer, so it should only be used in emergency
situations.
Naturally, when using this feature, you don't have any capacities to run links
which are targeting Sphinx references, as it is truly plain HTML only.
:::


### Links within toctrees

:::{todo}
Write it down.
:::




[Crate.io Sphinx Inventory Labels]: https://github.com/crate/crate-docs/issues/105
[intersphinx]: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
[Sphinx Getting Started]: https://www.sphinx-doc.org/en/master/usage/quickstart.html
[toctree]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree

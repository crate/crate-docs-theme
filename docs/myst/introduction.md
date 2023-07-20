# MyST introduction


## About

> A Sphinx and Docutils extension to parse MyST, a rich and extensible flavour
> of Markdown for authoring technical and scientific documentation.
>
> -- https://myst-parser.readthedocs.io/

[MyST](https://myst-parser.readthedocs.io/) is a strict superset of the
[CommonMark syntax specification](https://spec.commonmark.org/).
It adds features focussed on scientific and technical documentation authoring. {fas}`star2`


## Details

Roles and directives provide a way to extend the syntax of MyST in an unbound
manner, by interpreting a chunk of text as a specific type of markup, according
to its name.
Directives syntax is defined with triple-backticks and curly-brackets, effectively
a Markdown code fence.

-– [Roles and Directives](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html)

**Example**

> ![image|297x168](https://global.discourse-cdn.com/business7/uploads/crate/original/1X/d61bae27e7ce2ca04ab7ba78954153b885f2548e.png)


## History - The great dilemma

For a long time, the power of the Sphinx documentation generator was only available
to people writing documentation in reStructuredText. Because Markdown gained
significant popularity in recent years, the community was in a big dilemma, and
surely there have been endless Programming Language Wars-style discussions about
using reStructuredText vs. Markdown for documentation authoring.

This dilemma has come to an end with MyST now, aiming to follow up on the success
of MySQL and mypy – naming-wise.

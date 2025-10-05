# Authoring Guide

Set up a development sandbox suitable for convenient editing with live
reloading, i.e. just type `make dev`.

:::{card}
This document primarily illustrates the editing workflow in downstream
documentation projects, and can be used as a general guideline to support
your technical writing.
:::


## What's Inside

- Documentation is written in [Markdown], more specifically
  the [MyST] CommonMark dialect, or [reStructuredText].

- The documentation system is based on [Sphinx], [MyST], [sphinx-design],
  [sphinx-design-elements], and many other Sphinx addons and plugins.

- The documentation theme is [crate-docs-theme].

- The documentation projects use [Read the Docs] for publishing.


## Prerequisites

For running the documentation build and sandbox, you will need an installation
of Python on your workstation.

For convenient ad hoc searching within the content of the working tree from the
command line, the authors also recommend to install the [ripgrep] or [The
Silver Searcher] program.

For converting reStructuredText to Markdown, please have a look at the [Pandoc]
universal document converter, and the [rst-to-myst] program.


## Setup

In order to spin up a development environment for live editing, based on
[crate-docs], in turn using [sphinx-autobuild], acquire the sources, and
invoke `make dev`.

```shell
git clone https://github.com/crate/cratedb-guide
cd cratedb-guide/docs
```

:::{note}
Please adjust the repository URL when targeting other documentation projects.
Note that you may not have `make dev` available on non-CrateDB projects, so
you will need to invoke [sphinx-autobuild] on your own behalf.
:::


## Operations

### Live Reloading
When invoking the live editing mode, the documentation will be compiled and
served by a development web server.
```shell
make dev
```
When connecting to it using a browser, and editing the files using the editor
of your choice, filesystem changes will be detected, documentation will be
recompiled, and a refresh event will be propagated to the browser.

### Link Checker
To invoke the link checker, which is also part of the PR validation on CI.
```shell
make check
```

### Rendering
To render the documentation, one-shot, without live editing.
```shell
make html
```

### Reset
Reset the embedded `docs/.crate-docs` directory, in order to fetch a new
version next time.
```shell
make reset
```


## Previews

If you submit a pull request to the project on GitHub, a corresponding CI job
will provide you a rendered preview version to inspect your changes like they
would be published after integrating your patch.


## Contributing

Interested in contributing to this or any other documentation project?
Thank you so much!

As an open-source project, we are always looking for improvements in form of
contributions, whether it be in the form of a new feature, improved
infrastructure, or better documentation.

Your bug reports, feature requests, and patches are highly appreciated.


## Acknowledgements

Thanks to the team at [Read the Docs] for providing the excellent service.



[crate-docs]: https://github.com/crate/crate-docs
[crate-docs-theme]: https://crate-docs-theme.readthedocs.io/
[Markdown]: https://daringfireball.net/projects/markdown/
[MyST]: https://myst-parser.readthedocs.io/
[Pandoc]: https://pandoc.org/
[Read the Docs]: https://about.readthedocs.com/
[reStructuredText]: https://docutils.sourceforge.io/rst.html
[ripgrep]: https://github.com/burntsushi/ripgrep
[rst-to-myst]: https://github.com/executablebooks/rst-to-myst
[Sphinx]: https://www.sphinx-doc.org/
[sphinx-autobuild]: https://pypi.org/project/sphinx-autobuild/
[sphinx-design]: https://sphinx-design.readthedocs.io/
[sphinx-design-elements]: https://sphinx-design-elements.readthedocs.io/
[The Silver Searcher]: https://github.com/ggreer/the_silver_searcher

# Authoring Guide

Set up a development sandbox suitable for convenient editing with live
reloading, i.e. just type `make dev`.

:::{card}
This document primarily illustrates the editing workflow in downstream
documentation projects, and can be used as a general guideline to support
your technical writing.
:::


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


## Publishing

This project uses [Read the Docs] for publishing, thanks to their team for
the excellent service.

If you submit a pull request to the project on GitHub, a corresponding CI job
will provide you a rendered preview version to inspect your changes like they
would be published after integrating your patch.


[crate-docs]: https://github.com/crate/crate-docs
[Pandoc]: https://pandoc.org/
[Read the Docs]: https://about.readthedocs.com/
[ripgrep]: https://github.com/burntsushi/ripgrep
[rst-to-myst]: https://github.com/executablebooks/rst-to-myst
[sphinx-autobuild]: https://pypi.org/project/sphinx-autobuild/
[The Silver Searcher]: https://github.com/ggreer/the_silver_searcher

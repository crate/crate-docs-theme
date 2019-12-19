===============
Developer Guide
===============


Prerequisites
=============

You must have Python 3.7 installed.


Documentation
=============

The documentation is written using `Sphinx`_ and `ReStructuredText`_.


Working on the documentation
----------------------------

Python 3.7 is required.

Change into the ``docs`` directory:

.. code-block:: console

    $ cd docs

For help, run:

.. code-block:: console

    $ make

    Crate Docs Utils

    Run `make <TARGET>`, where <TARGET> is one of:

      dev     Run a Sphinx development server that builds and lints the
              documentation as you edit the source files

      html    Build the static HTML output

      check   Build, test, and lint the documentation

      delint  Remove any `*.lint` files

      reset   Reset the build cache

You must install `fswatch`_ to use the ``dev`` target.


Continuous integration and deployment
-------------------------------------

|pypi| |style| |travis| |rtd|

Travis CI is `configured`_ to run ``make check`` from the ``docs`` directory.
Please do not merge pull requests until the tests pass.

`Read the Docs`_ automatically deploys the documentation whenever a configured
branch is updated.


Development
===========

The best way to test the theme is to build the docs for this project. The docs
build system installs the ``crate-docs-theme`` package from your local files
(instead of fetching a previously released version from PyPI).

Because the Python virtual environment is then cached, if you want the docs
build system to pick up changes you have made to the theme, you will have to
reset it each time, like so::

    $ make reset

Making changes
==============

If you have made changes to the Crate.io website and want to see those
changes reflected in the docs, you must make the same changes to this
theme.

To make changes to this them, follow this process:

1. `Make changes`_
2. `Prepare a release`_
3. `Upload to PyPI`_
4. `Rebuild the docs`_

Make changes
------------

Prepare your changes on a branch. Be sure to update the ``CHANGES.rst``
file with a description of what you changed.

When you're ready, create a new pull request. Once the pull request has
been approved by an appropriate reviewer, merge to the `master` branch.

Prepare a release
-----------------

To create a new release:

- Update ``__version__`` in ``src/crate/theme/rtd/__init__.py``

- Add a section for the new version in the ``CHANGES.rst`` file

- Commit your changes with a message like "Prepare release x.y.z"

- Push to origin

- Create a tag by running ``./devtools/create_tag.sh``


Upload to PyPI
--------------

You must switch to the project root directory for the following commands.

Build the package::

    $ make build

Upload the package to `PyPI`_::

    $ make upload

For this to work, you will need a personal PyPI account that is set up as as an
admin for this project on PyPI.

You'll also need to create a ``~/.pypirc`` file, like so::

    [distutils]
    index-servers =
      pypi

    [pypi]
    username=<USERNAME>
    password=<PASSWORD>

Here, ``<USERNAME>`` and ``<PASSWORD>`` should be replaced with your PyPI
username and password, respectively.

To see a list of other build options, run:

.. code:: console

    $ make


Rebuild the docs
----------------

See the internal documentation for how to `rebuild the docs`_.


.. _configured: https://github.com/crate/crate-docs-theme/blob/master/.travis.yml
.. _fswatch: https://github.com/emcrisostomo/fswatch
.. _PyPI: https://pypi.python.org/pypi
.. _Read the Docs: http://readthedocs.org
.. _rebuild the docs: https://github.com/crate/distribute/blob/master/REBUILD_DOCS.rst
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org/

.. |pypi| image:: https://badge.fury.io/py/crate-docs-theme.svg
    :alt: PyPI version
    :target: https://badge.fury.io/py/crate-docs-theme

.. |style| image:: https://img.shields.io/endpoint.svg?color=blue&url=https%3A%2F%2Fraw.githubusercontent.com%2Fcrate%2Fcrate-docs-theme%2Fmaster%2Fdocs%2Fstyle.json
    :alt: Style version
    :target: https://github.com/crate/crate-docs-style

.. |travis| image:: https://img.shields.io/travis/crate/crate-docs-theme.svg?style=flat
    :alt: Travis CI status
    :target: https://travis-ci.org/crate/crate-docs-theme

.. |rtd| image:: https://readthedocs.org/projects/crate-docs-theme/badge/
    :alt: Read the Docs status
    :target: https://readthedocs.org/projects/crate-docs-theme/

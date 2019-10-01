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

|utils| |travis| |rtd|

Travis CI is `configured`_ to run ``make check`` from the ``docs`` directory.
Please do not merge pull requests until the tests pass.

`Read the Docs`_ automatically deploys the documentation whenever a configured
branch is updated.


Development
===========

The best way to test the theme is to build the docs for this project. The docs
build system installs the crate-docs-theme package from your local files
(instead of fetching a previously released version from PyPI).

Because the Python virtual environment is then cached, if you want the docs
build system to pick up changes you have made to the theme, you will have to
reset it each time, like so::

    $ make reset


Preparing a Release
===================

To create a new release, you must:

- Update ``__version__`` in ``src/crate/theme/rtd/__init__.py``

- Add a section for the new version in the ``CHANGES.rst`` file

- Commit your changes with a message like "Prepare release x.y.z"

- Push to origin

- Create a tag by running ``./devtools/create_tag.sh``


PyPI Deployment
===============

You must switch to the project root directory for the following commands.

Build the package:

    $ make build

Upload the package to PyPI_::

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

.. _configured: https://github.com/crate/crate-docs-theme/blob/master/.travis.yml
.. _fswatch: https://github.com/emcrisostomo/fswatch
.. _PyPI: https://pypi.python.org/pypi
.. _Read the Docs: http://readthedocs.org
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org/


.. |utils| image:: https://img.shields.io/endpoint.svg?color=blue&url=https%3A%2F%2Fraw.githubusercontent.com%2Fcrate%2Fcrate-docs-theme%2Fmaster%2Fdocs%2Futils.json
    :alt: Utils version
    :target: https://github.com/crate/crate-docs-theme/blob/master/docs/utils.json

.. |travis| image:: https://img.shields.io/travis/crate/crate-docs-theme.svg?style=flat
    :alt: Travis CI status
    :target: https://travis-ci.org/crate/crate-docs-theme

.. |rtd| image:: https://readthedocs.org/projects/crate-docs-theme/badge/?version=latest
    :alt: Read The Docs status
    :target: https://readthedocs.org/projects/crate-docs-theme

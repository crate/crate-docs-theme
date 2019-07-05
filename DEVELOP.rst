===============
Developer Guide
===============


Prerequisites
=============

You must have Python 3.7 installed.


Development
===========

The best way to test the theme is to build the docs for this project. The docs
build system installs the crate-docs-theme package from your local files
(instead of fetching a previously released version from PyPI).

Change into the `docs` directory:

.. code:: console

    $ cd docs

Build and run the docs using this command:

.. code:: console

    $ make dev

Afterwards, visit ``127.0.0.1:8000`` in your browser.

Because the Python virtual environment is then cached, if you want the docs
build system to pick up changes you have made to the theme, you will have to
reset it each time, like so::

    $ make reset

To see a list of other docs build options, run:

.. code:: console

    $ make

Preparing a Release
===================

To create a new release, you must:

- Update ``__version__`` in ``src/crate/theme/rtd/__init__.py``

- Add a section for the new version in the ``CHANGES.txt`` file

- Commit your changes with a message like "prepare release x.y.z"

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

.. _PyPI: https://pypi.python.org/pypi

===============
Developer Guide
===============

Prerequisites
=============

This project requires Python 3.4 or greater for development.

To make releases, will need `wheel` installed::

    $ pip install wheel

Setup
=====

To setup the project for local development use virtualenv.

To start things off, run::

    $ python -m venv env
    $ source env/bin/activate

Then, run::

    $ pip install -e .

Testing
=======

To test the theme, copy some docs into the ``docs`` directory.

Once your docs are in place, run this::

    $ sphinx-build -n -W -b html -E `pwd`/docs `pwd`/out/html

If you want to build the documentation of CrateDB you will need to install
the ``sphinx-csv-filter`` package upfront::

    $ pip install sphinx-csv-filter

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

First, clean the ``dist`` directory::

    $ rm dist/*

To create the package use::

    $ bin/py setup.py sdist bdist_wheel

Then, use twine_ to upload the package to PyPI_::

    $ bin/twine upload dist/*

For this to work, you will need a personal PyPI account that is set up as a project admin.

You'll also need to create a ``~/.pypirc`` file, like so::

    [distutils]
    index-servers =
      pypi

    [pypi]
    repository=https://pypi.python.org/pypi
    username=<USERNAME>
    password=<PASSWORD>

Here, ``<USERNAME>`` and ``<PASSWORD>`` should be replaced with your username and password, respectively.

If you want to check the PyPI description before uploading, run this::

    $ bin/py setup.py check --strict --restructuredtext

.. _buildout: https://pypi.python.org/pypi/zc.buildout
.. _Grunt: https://gruntjs.com/
.. _PyPI: https://pypi.python.org/pypi
.. _twine: https://pypi.python.org/pypi/twine

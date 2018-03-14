===============
Developer Guide
===============

Prerequisites
=============

This project requires Python 3.4 or greater for development.

Setup
=====

To setup the project for local development use virtualenv.

To start things off, run::

    $ python3 -m venv env
    $ source env/bin/activate

*NOTE: you must run these two commands every time you want to build the docs.
If you don't, the* ``sphinx-build`` *command will fail.*

Then, run::

    $ pip install -U setuptools
    $ pip install -e .

Testing
=======

Mirror the documentation from `the CrateDB repository`_::

    $ ln -s ../crate/sql
    $ ln -s ../crate/blackbox

These commands assume that your clone of the CrateDB repository is located at
``../crate``, relative to your clone of the docs theme repository. If this
isn't true, adjust the paths.

Now, fake an install of the ``sphinx-csv-filter`` package::

    $ ln -s ../../../sphinx_csv_filter/src/crate/sphinx src/crate/sphinx

These command assume that your clone of the `Sphinx CSV Filter`_ repository is
located at ``../sphinx_csv_filter``, relative to your clone of the docs theme
repository. If this isn't true, clone the repository, or adjust the paths.

To build the docs, run::

    $ sphinx-build -n -b html -E `pwd`/blackbox/docs `pwd`/out/html

You should now be able to view the built docs, like so::

    $ open out/html/index.html

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

To make releases, will need `wheel` installed::

    $ pip install wheel

Clean the ``dist`` directory::

    $ rm dist/*

To create the package use::

    $ python setup.py sdist bdist_wheel

Then, use twine_ to upload the package to PyPI_::

    $ twine upload dist/*

For this to work, you will need a personal PyPI account that is set up as a project admin.

You'll also need to create a ``~/.pypirc`` file, like so::

    [distutils]
    index-servers =
      pypi

    [pypi]
    username=<USERNAME>
    password=<PASSWORD>

Here, ``<USERNAME>`` and ``<PASSWORD>`` should be replaced with your username and password, respectively.

If you want to check the PyPI description before uploading, run this::

    $ bin/py setup.py check --strict --restructuredtext

.. _buildout: https://pypi.python.org/pypi/zc.buildout
.. _Grunt: https://gruntjs.com/
.. _PyPI: https://pypi.python.org/pypi
.. _Sphinx CSV Filter: https://github.com/crate/sphinx_csv_filter
.. _the CrateDB repository: https://github.com/crate/crate
.. _twine: https://pypi.python.org/pypi/twine

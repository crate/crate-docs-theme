===============
Developer Guide
===============

Setup
=====

This project uses buildout_ to set up the development environment.

To start things off, run::

    $ python bootstrap.py

Then, run::

    $ ./bin/buildout -N

*Note*: this project no longer uses Grunt_, but some Grunt files remain for the time being. These files can be safely ignored.

Testing
=======

To test the theme, copy some docs into the ``docs`` directory.

Once your docs are in place, run this::

    $ bin/sphinx

Preparing a Release
===================

To create a new release, you must:

- Update ``__version__`` in ``src/crate/theme/rtd/__init__.py``

- Update the version in ``package.json``

- Add a section for the new version in the ``CHANGES.txt`` file

- Commit your changes with a message like "prepare release x.y.z"

- Push to origin

- Create a tag by running ``./devtools/create_tag.sh``

PyPI Deployment
===============

To create the packages, run this::

    $ bin/py setup.py sdist bdist_wheel

Then, use twine_ to upload the packages::

    $ bin/twine upload dist/*

This last command builds the package and uploads it to PyPI_.

For that to work you will need a personal PyPI account that is set up as a project admin.

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

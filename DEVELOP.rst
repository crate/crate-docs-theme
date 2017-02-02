Development
-----------

Prerequisites
=============

Be sure have Python 2.7 installed.

Set Up From Source
==================

This project uses buildout to set up all requirements::

    python bootstrap.py
    bin/buildout -N

*Note*: if you get an error running ``bin/buildout``, try running ``python bin/buildout`` instead.

To build the app, run::

    bin/npm install

Start the file watchers for LESS and Sphinx like so::

    bin/grunt watch

Or, compile on demand like so::

    bin/grunt recess

That will compile the ``.less`` files into
``src/crate/theme/rtd/crate/static/css/main.css``.

*Note*: this project no longer uses LESS files and these instructions are out of date.

To test the theme, copy some Sphinx docs into the ``docs`` directory.

Once your docs are in place, run::

    bin/sphinx

Distributing
============

To create a release, you must:

- Update the version in ``src/crate/theme/rtd/__init__.py``
- Update the version in ``package.json``
- Add section to the ``CHANGES.txt`` file
- Commit your changes with a message like "prepare release x.x.x"
- Push to origin on the master branch
- Run ``./devtools/create_tag.sh``
- Run ``bin/twine upload dist/*``

This last command builds the package and uploads it to PyPI. For that to work you will need to have a PyPI account, and you'll need to be added as a project admin.

You'll also need to create the ``~/.pypirc`` file like so::

    [distutils]
    index-servers =
      pypi

    [pypi]
    repository=https://pypi.python.org/pypi
    username=your_username
    password=your_password

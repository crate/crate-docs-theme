===========
DEVELOPMENT
===========

Prerequisites
=============

This project uses buildout to manage its dependencies.
Be sure have a working ``python 2.7`` installed.

Set up from source
==================

This project uses buildout to set up all requirements::

    python bootstrap.py
    bin/buildout -N

To build the app simply run ``npm`` in this crate-docs-theme folder::

    bin/npm install

To test the theme you need to copy your docs into the ``docs`` folder.

Start the file watchers for LESS_ and Sphinx_::

    bin/grunt watch

To build a documentation with the theme run::

    bin/sphinx


Distributing
============

Before creating a new distribution, a new version and tag should be created:

 - Add a new version to ``src/crate/theme/rtd/__init__.py`` and ``package.json``.

 - Add a note for the new version at the ``CHANGES.txt`` file.

 - Commit e.g. using message 'prepare release x.x.x'.

 - Push to origin on the master branch.

 - Create a tag using the ``create_tag.sh`` script
   (run ``./devtools/create_tag.sh``).

 - Build and upload to PyPi: ``bin/py setup.py sdist upload``


.. _Sphinx: http://sphinx-doc.org/

.. _LESS: http://lesscss.org/

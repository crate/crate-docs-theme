===========
DEVELOPMENT
===========

Prerequisites
=============

This project uses buildout to manage its dependencies.
Be sure have a working ``python 2.7`` installed.

Set up from source
==================

This project uses buildout to set up all requirements.

To build the app simply run ``npm`` in this crate-docs-theme folder::

    bin/npm install

Copy your docs into ``_docs`` folder.

Start the file watchers::

    bin/grunt watch

To build the theme run::

    bin/sphinx


Distributing
============

Before creating a new distribution, a new version and tag should be created:

 - Add a new version to ``setup.py`` and ``package.json``.

 - Add a note for the new version at the ``CHANGES.txt`` file.

 - Commit e.g. using message 'prepare release x.x.x'.

 - Push to origin on the master branch.

 - Create a tag using the ``create_tag.sh`` script
   (run ``./devtools/create_tag.sh``).

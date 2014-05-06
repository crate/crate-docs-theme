crate-docs-theme
================

This project provides a Sphinx theme support for ReadTheDocs for the Crate documentation.


Local Theme Development
-----------------------

Run buildout::

    python bootstrap.py

    bin/buildout -N

Install Node packages::

    bin/npm install

Copy documentation files into ``docs`` folder.

Build documentation using theme::

    bin/sphinx

Watchers
--------

There are 2 watchers, one for LESS_ and one for the Sphinx_::

    bin/grunt watch:less
    bin/grunt watch:sphinx

or simply watch::

    bin/grunt watch


.. _Sphinx: http://sphinx-doc.org/

.. _LESS: http://lesscss.org/

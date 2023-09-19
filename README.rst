================
Crate Docs Theme
================

|tests| |rtd| |build| |pypi|


About
=====

A `Sphinx`_ theme for the `Crate documentation`_.

*Note: This theme is tightly integrated into the Crate.io website and is
not intended for general use.*

For making changes to the theme, see the `developer docs`_.


Preview
=======

The demo/preview project is rendered and published to https://crate-docs-theme.readthedocs.io/.


Using the theme
===============

Prerequisites
-------------

The documentation can include UML diagrams which will be rendered using
`sphinxcontrib-plantuml`_. In order to satisfy its requirements, run::

    # On Linux
    apt-get install plantuml

    # On macOS
    brew install plantuml

.. _sphinxcontrib-plantuml: https://pypi.org/project/sphinxcontrib-plantuml/

Installation
------------

The Crate docs theme is available as a package on `PyPI`_. However, there is no
need to install it yourself. Crate projects that use the theme should install
it automatically.


Configuration
-------------

The Crate.io documentation is composed of multiple separate documentation
projects, seamlessly interlinked via the Crate docs theme.

To use the theme, add this line to your Sphinx ``conf.py`` file::

   from crate.theme.rtd.conf.foo import *

Here, replace ``foo`` with the appropriate module for your documentation
project.


Contributing
============

This project is primarily maintained by `Crate.io`_, but we welcome community
contributions!

See the `developer docs`_ and the `contribution docs`_ for more information.


Help
====

Looking for more help?

- Check out our `support channels`_


.. _contribution docs: CONTRIBUTING.rst
.. _Crate.io: https://cratedb.com
.. _Crate documentation: https://cratedb.com/docs/
.. _developer docs: DEVELOP.rst
.. _PyPI: https://pypi.python.org/
.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _support channels: https://cratedb.com/support/


.. |tests| image:: https://github.com/crate/crate-docs-theme/workflows/docs/badge.svg
    :alt: CI status
    :target: https://github.com/crate/crate-docs-theme/actions?workflow=docs

.. |rtd| image:: https://readthedocs.org/projects/crate-docs-theme/badge/
    :alt: Read the Docs status
    :target: https://readthedocs.org/projects/crate-docs-theme/

.. |build| image:: https://img.shields.io/endpoint.svg?color=blue&url=https%3A%2F%2Fraw.githubusercontent.com%2Fcrate%2Fcrate-docs-theme%2Fmain%2Fdocs%2Fbuild.json
    :alt: crate-docs version
    :target: https://github.com/crate/crate-docs-theme/blob/main/docs/build.json

.. |pypi| image:: https://badge.fury.io/py/crate-docs-theme.svg
    :alt: PyPI version
    :target: https://badge.fury.io/py/crate-docs-theme

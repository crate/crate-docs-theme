================
Crate Docs Theme
================

|pypi|

A `Sphinx`_ theme for the `Crate documentation`_.

*Note: This theme is tightly integrated into the Crate.io website and is
not intended for general use.*

For help making changes to the theme, see the `developer docs`_.


Using the theme
===============

Installation
------------

The Crate docs theme is available as a package on `PyPI`_. However, there is no
need to install it yourself. Crate projects that use the theme should install
it automatically.


Configuration
-------------

The Crate documentation is composed of multiple separate documentation
projects, seemlessly interlinked via the Crate docs theme.

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
.. _Crate.io: https://crate.io
.. _Crate documentation: https://crate.io/docs/
.. _developer docs: DEVELOP.rst
.. _PyPI: https://pypi.python.org/
.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _support channels: https://crate.io/support/


.. |pypi| image:: https://badge.fury.io/py/crate-docs-theme.svg
    :alt: PyPI version
    :target: https://badge.fury.io/py/crate-docs-theme

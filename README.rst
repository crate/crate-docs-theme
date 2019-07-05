================
Crate Docs Theme
================

|pypi| |travis| |rtd|

A `Sphinx`_ theme for the `Crate documentation`_.

*Note: This theme is not intended for general use. You may want to use this
theme as an inspiration if you are building your own theme. However, this theme
is designed for Crate projects with documentation that is tightly integrated
into the Crate.io` website.*


Installation
============

The Crate docs theme is available as a package on `PyPI`_. However, there is no
need to install it yourself. Crate projects that use the theme should install
it automatically.


Configuration
=============

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

.. |travis| image:: https://img.shields.io/travis/crate/crate-docs-theme.svg?style=flat
    :alt: Travis CI status
    :target: https://travis-ci.org/crate/crate-docs-theme

.. |rtd| image:: https://readthedocs.org/projects/crate-docs-theme/badge/
    :alt: Read the Docs status
    :target: https://readthedocs.org/projects/crate-docs-theme/

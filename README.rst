================
crate-docs-theme
================

This project provides a Sphinx theme for Crate's documentation
that is compatible with ReadTheDocs.

Using the theme
---------------

In your docs ``conf.py`` import the settings from the theme::

   from crate.rtd_theme.conf import *

or if you want to use a specific configuration::

   from crate.rtd_theme.conf.crate_server import *

That's all!


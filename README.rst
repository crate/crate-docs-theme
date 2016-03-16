================
crate-docs-theme
================

This project provides a Sphinx theme for Crate's documentation
that is compatible with ReadTheDocs.

Using the theme
---------------

In your docs ``conf.py`` import the settings from the theme::

   from crate.theme.rtd.conf import *

or if you want to use a specific configuration::

   from crate.theme.rtd.conf.crate_server import *

That's all!

Development
-----------

The project uses buildout to bootstrap::

    python bootstrap.py

    bin/buildout -N

This will install ``NodeJs`` and the required modules.

There is a watcher that compiles ``.less`` files into ``.css``::

    bin/grunt watch

or compile on demand with the ``recess`` command::

    bin/grunt recess

That will compile the ``.less`` files into
``src/crate/theme/rtd/crate/static/css/main.css``

In order to build a documentation for testing purposes,
place your rst files into the ``docs/`` folder
and use ``sphinx`` to build the docs with the theme::

    bin/sphinx

Distribute
----------

Change the version number in ``package.json`` and
``src/crate/theme/rtd/__init__.py``.

Create new section in ``CHANGES.txt`` with version number
and release date.

Commit to master with message ``prepare release x.x.x``.

Run ``./devtools/crate_tag.sh`` to create a new tag.




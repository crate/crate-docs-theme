===============
Developer Guide
===============


Introduction
============

To make changes to this theme, follow this process:

1. `Making changes to the theme`_
2. `Prepare a release`_
3. `Upload to PyPI`_
4. `Rebuild all Crate docs`_

*Note*: If you have made changes to the Crate.io website and want to see those
changes reflected in the docs, you must make the same changes to this
theme.


Making changes to the theme
===========================

HTML templates
--------------

Create a branch for your changes.

Once you have a branch, the basic workflow goes like this:

1. Modify the theme files
2. Build the project docs to test what the theme looks like
3. If you need to make additional changes, reset the build environment
   and go back to step one

The best way to test your changes is to build the sample docs for this
project. See the `Documentation`_ section below for details. The command
to use for this is ``make dev``.

Once the webserver is running, you can view your local copy of the docs
by visiting http://127.0.0.1:8000 in a web browser.

For all other Crate projects, ``make dev`` fetches a released version of
the theme from `PyPI`_. However, this project is different. When you run
``make dev``, the build system creates a mock release of the theme using
your local files and installs it into the Python virtual environment
used by the build system. This trick allows you to preview what the theme
would look like if it were released.

The Python virtual environment caches packages, including the mock one
you use for testing. Accordingly, you must reset the cache every time
you make a change to the theme that you want to preview. You can do that
like so::

    $ make reset

When you're ready, create a pull request.

*Note*: Be sure to update the ``CHANGES.rst`` file with a description of
what you changed. (Be sure to add your change items to the *Unreleased*
section.)

Once an appropriate reviewer has approved the pull request, merge your
changes to the ``master`` branch.

A project admin should be asked to complete the remaining steps.


JavaScript, CSS and asset files
-------------------------------

Add new JavaScript and CSS to ``custom.css`` and ``custom.js`` respectively.
In order to run the bundling process, invoke those commands::

    yarn install
    npx webpack --mode=development

Those commands might need some prerequisites installed on your machine. In
order to run the setup on, e.g., Linux, invoke those commands - YMMV::

    sudo apt update
    curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
    sudo apt-get install -y nodejs
    sudo npm install --global yarn


Release
=======

Prepare a release
-----------------

To create a new release from the ``master`` branch:

- Add a new version section to the ``CHANGES.txt`` file

  - Please honor `SemVer`_ when choosing the new version number. If this
    release includes breaking changes, please add the boilerplate notice to the
    top of the changelog entry.

  - Please separate out the changes into sections where it makes sense. Consult
    previous releases for an idea of how to do this.

- Update ``__version__`` in ``src/crate/theme/rtd/__init__.py``

- Commit your changes with a message like "Prepare release x.y.z"

- Push to ``origin``

- Run ``./devstools/create_tag.sh``

- Visit the `releases page`_ and select the version you just released

- Select *Edit tag*

- Copy and paste the changelog notes for this release (be sure to remove the
  hard line breaks)

- Check the *Preview* tab for display errors and fix if necessary

- Select *Publish release*


Upload to PyPI
--------------

To build and upload the package, you must have `Yarn`_ (the package manager)
installed on your system. The `Makefile`_ uses Yarn to install the dependencies
necessary to compile the JavaScript and CSS assets.

Switch to the project root directory for the following commands.

Build the package::

    $ make build

**TIP**
  If you encounter a Ruby error when running `make`, it is likely because you
  have the `yarn gem`_ installed and its executable appears first your
  ``PATH``. To fix this issue, uninstall the yarn gem, or reconfigure your
  ``PATH``.

Upload the package to `PyPI`_::

    $ make upload

For this to work, you will need a personal PyPI account and that account
must be an admin for this project on PyPI.

You'll also need to create a ``~/.pypirc`` file, like so::

    [distbuild]
    index-servers =
      pypi

    [pypi]
    username=<USERNAME>
    password=<PASSWORD>

Here, ``<USERNAME>`` and ``<PASSWORD>`` should be replaced with your PyPI
username and password, respectively.

To see a list of other build options, run:

.. code:: console

    $ make


Rebuild all Crate docs
----------------------

Once the theme is released, you must rebuild all of the Crate docs so
that they pick up the changes. Consult the internal documentation for
help `rebuilding the docs`_.


Documentation
=============

We write the documentation with `Sphinx`_ and `ReStructuredText`_.


Working on the documentation
----------------------------

Python >= 3.7 is required.

Change into the ``docs`` directory:

.. code-block:: console

    $ cd docs

For help, run:

.. code-block:: console

    $ make

    Crate Docs Build

    Run `make <TARGET>`, where <TARGET> is one of:

      dev     Run a Sphinx development server that builds and lints the
              documentation as you edit the source files

      html    Build the static HTML output

      check   Build, test, and lint the documentation

      reset   Reset the build cache


Testing on mobile
-----------------

If you want to test the theme on a mobile device, you can run the dev server on
``0.0.0.0:8000`` instead of ``127.0.0.1:8000``. When you bind to ``0.0.0.0``,
devices on your local network can access the dev server by connecting to your
machine's IP address on port ``8000``.

Bind the dev server to ``0.0.0.0`` like this::

    $ make SPHINX_OPTS='-W -n --host 0.0.0.0' dev


Continuous integration and deployment
=====================================

This project uses GitHub Actions to run ``make check`` from the ``docs``
directory.

Also, `Read the Docs`_ automatically rebuilds the documentation whenever an
active docs branch is updated.

To make changes to the RTD configuration (e.g., to activate or deactivate a
release version), please contact an admin.


.. _Makefile: https://github.com/crate/crate-docs-theme/blob/master/Makefile
.. _PyPI: https://pypi.python.org/pypi
.. _Read the Docs: http://readthedocs.org
.. _rebuilding the docs: https://github.com/crate/distribute/blob/master/REBUILD_DOCS.rst
.. _releases page: https://github.com/crate/crate-docs-theme/releases
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org/
.. _yarn gem: https://rubygems.org/gems/yarn
.. _Yarn: https://yarnpkg.com/

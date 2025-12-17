# -*- coding: utf-8; -*-
#
# Licensed to Crate (https://crate.io) under one or more contributor
# license agreements.  See the NOTICE file distributed with this work for
# additional information regarding copyright ownership.  Crate licenses
# this file to you under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.  You may
# obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#
# However, if you have executed another commercial license agreement
# with Crate these terms will supersede the license and you may use the
# software solely pursuant to the terms of the relevant commercial agreement.

"""CrateDB Sphinx theme for Read the Docs"""

import os
from .sidebartoc import generate_crate_navigation_html

VERSION = (0, 43, 0)

__version__ = ".".join(str(v) for v in VERSION) # + ".dev0"
__version_full__ = __version__


def get_version():
    return __version__

def current_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_html_theme_path():
    """Return list of HTML theme paths."""
    return [current_dir()]

def get_html_static_path():
    """Return list of HTML static paths."""
    return [os.path.join(current_dir(), "crate", "static")]

def get_html_template_path():
    """Return list of HTML template paths."""
    return [os.path.join(current_dir(), "crate")]


def _add_crate_navigation(app, pagename, templatename, context, doctree):
    """
    Sphinx event handler: Add enhanced navigation to template context.

    Generates multi-project navigation HTML and processes it through
    Furo's navigation enhancer to add collapsible icons and checkboxes.
    """

    from furo.navigation import get_navigation_tree

    navigation_html = generate_crate_navigation_html(context)

    # Process through Furo's navigation enhancer
    enhanced_navigation = get_navigation_tree(navigation_html)

    # Add to context for use in templates
    context["crate_navigation_tree"] = enhanced_navigation

def setup(app):
    """
    Registers event handlers to setup navigation.
    """
    app.connect("html-page-context", _add_crate_navigation)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

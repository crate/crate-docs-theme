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

from crate.theme import rtd as theme
from os import environ

source_suffix = '.rst'

master_doc = 'index'

exclude_patterns = ['.*', '*.lint', 'README.rst', 'requirements.txt']
exclude_trees = ['pyenv', 'tmp', 'out', 'parts', 'clients', 'eggs']

extensions = ['sphinx_sitemap']

# Configure the theme
html_theme = 'crate'
html_theme_path = theme.get_html_theme_path()
nitpicky = True
html_show_sourcelink = False
html_sidebars = {'**': ['sidebar.html', 'sourcelink.html']}
html_theme_options = {
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': 'navbar navbar-inverse',

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': 'false',

    'globaltoc_includehidden': 'true',

    # The URL path is required because RTD does only allow root as a canonical
    # url
    'canonical_url_path': '',
    'canonical_url': 'https://crate.io/',

    # segment analytics configuration
    'tracking_segment_id': environ.get('TRACKING_SEGMENT_ID', ''),
    'tracking_project': '',

    # Can be used the query string of a resource URL for HTTP cache busting
    "ver": theme.get_version(),
}
html_extra_path = ["_extra"]
sitemap_filename = "site.xml"
# These variables are overridden by Read The Docs
language = "en"
version = "latest"
sitemap_url_scheme = "{lang}{version}{link}"

def setup(app):
    # Force the canonical URL in multiple ways
    #
    # This gets around several points where the canonical_url override might be
    # disregarded or performed out of order.
    #
    # This module should be star imported into `create_*.py`, and thus star
    # imported into the base `conf.py`. Sphinx will automatically use a `setup()`
    # in `conf.py` as an extension.
    def force_canonical_url(app_inited):
        from sphinx.builders.html import StandaloneHTMLBuilder
        from sphinx.builders.epub3 import Epub3Builder
        if (isinstance(app_inited.builder, StandaloneHTMLBuilder)
                and not isinstance(app_inited.builder, Epub3Builder)):
            try:
                canonical_url = app_inited.builder.theme_options['canonical_url']
                canonical_url_path = app_inited.builder.theme_options['canonical_url_path']
            except KeyError:
                return
            canonical_url = canonical_url + canonical_url_path
            app_inited.env.config.html_context['canonical_url'] = canonical_url
            app_inited.builder.config.html_context['canonical_url'] = canonical_url
    app.connect('builder-inited', force_canonical_url)


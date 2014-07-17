# -*- coding: utf-8; -*-
#
# Licensed to CRATE Technology GmbH ("Crate") under one or more contributor
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

copyright = u'2014, CRATE Technology GmbH'

# The suffix of source filenames.
source_suffix = '.txt'
exclude_patterns = ['requirements.txt']

# The master toctree document.
master_doc = 'index'
exclude_trees = ['pyenv', 'tmp', 'out', 'parts', 'clients', 'eggs']
extensions = ['sphinx.ext.autodoc']

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
    'navbar_fixed_top': 'true',

    'globaltoc_includehidden': 'true',

    # The URL path is required because RTD does only allow
    # root as a cannonical url.
    'cannonical_url_path': '',

    # segment.io tracking configuration
    'tracking_segment_io_id': 'vd4x4hv637',
}

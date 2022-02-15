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

source_suffix = ".rst"

master_doc = "index"

exclude_patterns = [".*", "*.lint", "README.rst", "requirements.txt"]
exclude_trees = ["pyenv", "tmp", "out", "parts", "clients", "eggs"]

extensions = [
    "sphinx_sitemap",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.plantuml",
    "sphinxext.opengraph",
    "sphinx_copybutton",
]

# Configure the theme
html_theme = "crate"
html_theme_path = theme.get_html_theme_path()
nitpicky = True
html_show_sourcelink = False
html_sidebars = {"**": ["sidebar.html", "sourcelink.html"]}
html_theme_options = {
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    "navbar_class": "navbar navbar-inverse",
    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    "navbar_fixed_top": "false",
    "globaltoc_includehidden": "true",
    # The URL path is required because RTD does only allow root as a canonical
    # url
    "canonical_url_path": "",
    "canonical_url": "https://crate.io/",
    # segment analytics configuration
    "tracking_segment_id": environ.get("TRACKING_SEGMENT_ID", ""),
    "tracking_hubspot_id": environ.get("TRACKING_HUBSPOT_ID", ""),
    "tracking_project": "",
    # Google custom search engine
    "google_search_api_key": environ.get("GOOGLE_SEARCH_API_KEY", ""),
    "google_search_cx_id": environ.get("GOOGLE_SEARCH_CX_ID", ""),

    # Can be used the query string of a resource URL for HTTP cache busting
    "ver": theme.get_version(),
}
html_extra_path = ["_extra"]
sitemap_filename = "site.xml"
# These variables are overridden by Read The Docs
language = "en"
version = "latest"
sitemap_url_scheme = "{lang}{version}{link}"

# Configure intersphinx mapping
intersphinx_mapping = {

    # CrateDB core
    'crate-reference': ('https://crate.io/docs/crate/reference/en/latest/', None),
    'crate-tutorials': ('https://crate.io/docs/crate/tutorials/en/latest/', None),
    'crate-howtos': ('https://crate.io/docs/crate/howtos/en/latest/', None),

    # CrateDB clients
    'crate-admin-ui': ('https://crate.io/docs/crate/admin-ui/en/latest/', None),
    'crate-crash': ('https://crate.io/docs/crate/crash/en/latest/', None),
    'crate-clients-tools': ('https://crate.io/docs/crate/clients-tools/en/latest/', None),
    'crate-jdbc': ('https://crate.io/docs/jdbc/en/latest/', None),
    'crate-npgsql': ('https://crate.io/docs/npgsql/en/latest/', None),
    'crate-dbal': ('https://crate.io/docs/dbal/en/latest/', None),
    'crate-pdo': ('https://crate.io/docs/pdo/en/latest/', None),
    'crate-python': ('https://crate.io/docs/python/en/latest/', None),

    # CrateDB Cloud
    'cloud-reference': ('https://crate.io/docs/cloud/reference/en/latest/', None),
    'cloud-tutorials': ('https://crate.io/docs/cloud/tutorials/en/latest/', None),
    'cloud-howtos': ('https://crate.io/docs/cloud/howtos/en/latest/', None),
    'cloud-cli': ('https://crate.io/docs/cloud/cli/en/latest/', None),

    # Misc
    'sql-99': ('https://crate.io/docs/sql-99/en/latest/', None),

    # CrateDB Docs
    'crate-docs': ('https://crate-docs.readthedocs.io/en/latest/', None),
    'crate-docs-theme': ('https://crate-docs-theme.readthedocs.io/en/latest/', None),
}

# Configure OpenGraph extension
ogp_site_url = "https://crate.io/"
ogp_description_length = 300
ogp_site_name = "CrateDB documentation"
ogp_image = "https://user-images.githubusercontent.com/453543/119536319-3c9ca480-bd89-11eb-908d-3da78e55f17b.png"
ogp_image_alt = False
ogp_use_first_image = True
ogp_type = "website"

# Configure Sphinx-copybutton
copybutton_remove_prompts = True
copybutton_prompt_text = r">>> |\.\.\. |\$ |sh\$ |PS> |cr> |mysql> |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# Configure linkchecker
linkcheck_ignore = [
    # Breaks accessibility via JS ¯\_(ツ)_/¯
    "https://www.iso.org/obp/ui/.*"
]
linkcheck_retries = 3
linkcheck_timeout = 15

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

        if isinstance(app_inited.builder, StandaloneHTMLBuilder) and not isinstance(
            app_inited.builder, Epub3Builder
        ):
            try:
                canonical_url = app_inited.builder.theme_options["canonical_url"]
                canonical_url_path = app_inited.builder.theme_options[
                    "canonical_url_path"
                ]
            except KeyError:
                return
            canonical_url = canonical_url + canonical_url_path
            app_inited.env.config.html_context["canonical_url"] = canonical_url
            app_inited.builder.config.html_context["canonical_url"] = canonical_url

    app.connect("builder-inited", force_canonical_url)

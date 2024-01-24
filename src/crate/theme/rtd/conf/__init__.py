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
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_design_elements",
    "sphinx_inline_tabs",
    "sphinx_sitemap",
    "sphinx_subfigure",
    "sphinx_togglebutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.graphviz",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.plantuml",
    "sphinxext.opengraph",
]

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# When not run on RTD, "html_context" is missing as a global variable
if "html_context" not in globals():
    html_context = {}
if "html_context_custom" not in globals():
    html_context_custom = {}

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
    "canonical_url": "https://cratedb.com/",
    # HubSpot analytics configuration
    "tracking_hubspot_id": environ.get("TRACKING_HUBSPOT_ID", ""),
    "tracking_project": "",
    # Google custom search engine
    "google_search_api_key": environ.get("GOOGLE_SEARCH_API_KEY", ""),
    "google_search_cx_id": environ.get("GOOGLE_SEARCH_CX_ID", ""),

    # Can be used the query string of a resource URL for HTTP cache busting
    "ver": theme.get_version(),
}
# https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html#fontawesome-icons
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

html_extra_path = ["_extra"]
sitemap_filename = "site.xml"
# These variables are overridden by Read The Docs
language = "en"
version = "latest"
sitemap_url_scheme = "{lang}{version}{link}"

# Configure intersphinx mapping
intersphinx_mapping = {

    # CrateDB Core
    'crate-reference': ('https://cratedb.com/docs/crate/reference/en/latest/', None),
    'crate-tutorials': ('https://cratedb.com/docs/crate/tutorials/en/latest/', None),
    'crate-howtos': ('https://cratedb.com/docs/crate/howtos/en/latest/', None),

    # CrateDB Clients and Integrations
    'crate-admin-ui': ('https://cratedb.com/docs/crate/admin-ui/en/latest/', None),
    'crate-clients-tools': ('https://cratedb.com/docs/crate/clients-tools/en/latest/', None),
    'crate-crash': ('https://cratedb.com/docs/crate/crash/en/latest/', None),
    'crate-dbal': ('https://cratedb.com/docs/dbal/en/latest/', None),
    'crate-jdbc': ('https://cratedb.com/docs/jdbc/en/latest/', None),
    'crate-npgsql': ('https://cratedb.com/docs/npgsql/en/latest/', None),
    'crate-operator': ('https://crate-operator.readthedocs.io/en/latest/', None),
    'crate-pdo': ('https://cratedb.com/docs/pdo/en/latest/', None),
    'crate-python': ('https://cratedb.com/docs/python/en/latest/', None),

    # CrateDB Cloud
    'cloud': ('https://cratedb.com/docs/cloud/en/latest/', None),
    'cloud-cli': ('https://cratedb.com/docs/cloud/cli/en/latest/', None),

    # Misc
    'sql-99': ('https://sql-99.readthedocs.io/en/latest/', None),

    # CrateDB Docs
    'crate-docs': ('https://crate-docs.readthedocs.io/en/latest/', None),
    'crate-docs-theme': ('https://crate-docs-theme.readthedocs.io/en/latest/', None),
}

# Configure OpenGraph extension
#
# When making changes, check them using the RTD PR preview URL on https://www.opengraph.xyz/.
#
# About text lengths
#
# Original documentation says:
# - ogp_description_length
#   Configure the amount of characters taken from a page. The default of 200 is probably good
#   for most people. If something other than a number is used, it defaults back to 200.
#   -- https://sphinxext-opengraph.readthedocs.io/en/latest/#options
#
# Other people say:
# - og:title 40 chars
# - og:description has 2 max lengths:
#   When the link is used in a Post, it's 300 chars. When a link is used in a Comment, it's 110 chars.
#   So you can either treat it as 110, or, write your Descriptions to 300 but make sure the first 110
#   is the critical part and still makes sense when it gets cut off.
#   -- https://stackoverflow.com/questions/8914476/facebook-open-graph-meta-tags-maximum-content-length
ogp_site_url = "https://cratedb.com/docs/"
ogp_description_length = 300
ogp_site_name = "CrateDB Documentation"
ogp_image = "https://crate-docs-theme.readthedocs.io/en/latest/_static/images/cratedb-logo-h630.png"
ogp_image_alt = False
ogp_use_first_image = False
ogp_type = "website"
ogp_enable_meta_description = True

# Configure Sphinx-copybutton
copybutton_remove_prompts = True
copybutton_line_continuation_character = "\\"
copybutton_prompt_text = r">>> |\.\.\. |\$ |sh\$ |PS> |cr> |mysql> |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# Configure linkchecker
linkcheck_ignore = [
    # Breaks accessibility via JS ¯\_(ツ)_/¯
    "https://www.iso.org/obp/ui/.*",
    "https://example.org/.*",
]
linkcheck_retries = 3
linkcheck_timeout = 15

# -- Options for MyST -------------------------------------------------
myst_heading_anchors = 3
myst_enable_extensions = [
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
]

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

    # Dynamically set the `proxied_api_host` context variable on a per-project level.
    def set_proxied_api_host(app_inited):
        try:

            # Compute appropriate per-project `proxied_api_host`.
            html_baseurl = app_inited.env.config.html_baseurl.strip("/")
            proxied_api_host = html_baseurl + "/_"

            # Propagate the `proxied_api_host` to different contexts by trial-and-error.
            app_inited.env.config.proxied_api_host = proxied_api_host
            app_inited.builder.config.proxied_api_host = proxied_api_host
            app_inited.env.config.html_context["proxied_api_host"] = proxied_api_host
            app_inited.builder.config.html_context["proxied_api_host"] = proxied_api_host
            print(f"INFO: Adjusted `proxied_api_host` to {proxied_api_host}")

        except Exception as ex:
            print(f"ERROR: Unable to adjust `proxied_api_host`. Reason: {ex}")

    # Dynamically adjust the `proxied_static_path` context variable on a per-project level.
    # https://github.com/crate/crate-docs-theme/issues/342
    def set_proxied_static_path(app_inited):
        try:

            # The default is `'proxied_static_path': "/_/static/"`.
            # However, we want it to be, e.g., https://cratedb.com/docs/crate/howtos/_/static/
            html_baseurl = app_inited.env.config.html_baseurl.strip("/")
            proxied_static_path = f"{html_baseurl}/_/static/"

            # Propagate the `proxied_api_host` to different contexts by trial-and-error.
            app_inited.env.config.html_context["proxied_static_path"] = proxied_static_path
            app_inited.builder.config.html_context["proxied_static_path"] = proxied_static_path

            print(f"INFO: Adjusted `proxied_static_path` to {proxied_static_path}")

        except Exception as ex:
            print(f"ERROR: Unable to adjust `proxied_static_path`. Reason: {ex}")

    # Apply all attributes from `html_context_custom` to `html_context`.
    def apply_html_context_custom(app_inited):
        try:
            if html_context_custom:
                app_inited.env.config.html_context.update(html_context_custom)
                app_inited.builder.config.html_context.update(html_context_custom)
                print(f"INFO: Adjusted `html_context` with {html_context_custom}")
            else:
                print(f"INFO: No adjustments to `html_context`")

        except Exception as ex:
            print(f"ERROR: Unable to adjust `html_context`. Reason: {ex}")

    app.connect("builder-inited", force_canonical_url)
    app.connect("builder-inited", set_proxied_api_host)
    app.connect("builder-inited", set_proxied_static_path)
    app.connect("builder-inited", apply_html_context_custom)

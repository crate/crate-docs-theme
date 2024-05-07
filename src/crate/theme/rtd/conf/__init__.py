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
    # HubSpot analytics configuration
    "tracking_hubspot_id": environ.get("TRACKING_HUBSPOT_ID", ""),
    "tracking_project": "",

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

sitemap_excludes = [
   "search.html",
   "genindex.html",
]

# Configure intersphinx mapping
intersphinx_mapping = {

    # CrateDB General
    'guide': ('https://cratedb.com/docs/guide/', None),
    'crate-reference': ('https://cratedb.com/docs/crate/reference/en/latest/', None),

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

    # Configure Sphinx/RTD to host projects on a custom domain, but also on a non-root resource.
    def configure_self_hosted_on_path(app_inited):
        """
        By default, Sphinx is agnostic, and RTD only supports custom domains,
        without support for hosting on non-root resources.

        In order to get things in order, this routine configures:

        - `ogp_site_url` Sphinx setting
          Configures the `sphinxext.opengraph` Sphinx addon.

        - `custom_baseurl` HTML context variable
          Configures the version chooser defined in `version_chooser.html`.
        """

        config = app_inited.env.config
        html_baseurl = config["html_baseurl"]

        if html_baseurl is None:
            return

        # A little heuristic to consider a project as "not versioned",
        # and process it accordingly, when the value of the "version"
        # setting is empty.
        rtd_language = config["language"]
        rtd_version = config["version"]
        if rtd_version:
            rtd_lang_slug = f"{rtd_language}/{rtd_version}/"
        else:
            rtd_lang_slug = ""

        # Resolve an intertwingulation between vanilla Sphinx and RTD.
        # CrateDB docs are hosted on a custom domain behind Nginx.
        html_baseurl_real = html_baseurl + rtd_lang_slug

        # Configure `sphinxext.opengraph`.
        config.ogp_site_url = html_baseurl_real

        # Properly render rel="canonical" links.
        # Because RTD does something silly with `index` page names,
        # render it in `base.html` manually.
        config.html_context["custom_baseurl"] = html_baseurl_real

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

    app.connect("builder-inited", configure_self_hosted_on_path)
    app.connect("builder-inited", set_proxied_api_host)
    app.connect("builder-inited", set_proxied_static_path)
    app.connect("builder-inited", apply_html_context_custom)

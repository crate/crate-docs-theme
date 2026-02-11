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

from furo.navigation import get_navigation_tree
from datetime import datetime
import os
import re

from crate.theme.rtd.icons import ICON_BUILD, ICON_OPERATIONS, ICON_REFERENCE, ICON_TOOLS


def _slugify_id(text):
    """Normalize text to a safe HTML ID: alphanumerics and hyphens only."""
    s = re.sub(r'[^a-z0-9-]', '-', text.lower())
    s = re.sub(r'-{2,}', '-', s)  # collapse multiple hyphens
    return s.strip('-')


class _NavBuilder:
    """Helper to build navigation HTML."""

    def __init__(self, parts, project, master_path, toctree_fn):
        self.parts = parts
        self.project = project
        self.master_path = master_path
        self.toctree = toctree_fn

    def add_nav_link(self, entry_name, entry_url, li_base_class='toctree-l1', border_top=False):
        """Add a cross-project navigation link with expand icon.

        Includes an empty <ul> so Furo's get_navigation_tree() adds the
        checkbox/icon structure. Since cross-project TOC content isn't
        available, clicking the icon navigates to that project instead
        of expanding (handled by JS in custom.js).
        """
        border = " border-top" if border_top else ""
        li_class = f'{li_base_class}{border}'
        self.parts.append(f'<li class="{li_class}">')
        self.parts.append(f'<a href="{entry_url}">{entry_name}</a>')
        # Empty <ul> triggers Furo to add has-children class and icon structure
        self.parts.append('<ul></ul>')
        self.parts.append('</li>')

    def add_project_nav_item(
        self,
        project_name,
        display_name,
        url_if_not_current,
        border_top=False,
        public_docs=True
    ):
        """Add a navigation item in left navbar for a project."""
        border = " border-top" if border_top else ""
        if self.project == project_name:
            self.parts.append(f'<li class="current{border}">')
            self.parts.append(f'<a class="current-active" href="{self.master_path}">{display_name}</a>')
            self.parts.append(self.toctree())
            self.parts.append('</li>')
            return

        if public_docs:
            self.add_nav_link(display_name, url_if_not_current, 'navleft-item', border_top)


def _generate_crate_navigation_html(context):
    """
    Generate multi-project navigation HTML structure, so we can process it
    through Furo's navigation enhancer.
    """
    toctree = context.get("toctree")
    if not toctree:
        return ""

    theme_globaltoc_includehidden = context.get("theme_globaltoc_includehidden", True)
    def _get_toctree(maxdepth=-1, titles_only=True, collapse=False):
        return toctree(
            maxdepth=maxdepth,
            titles_only=titles_only,
            collapse=collapse,
            includehidden=theme_globaltoc_includehidden
        )

    project = context.get("project", "")
    pagename = context.get("pagename", "")
    master_doc = context.get("master_doc", "index")
    master_path = context["pathto"](master_doc)

    parts = ['<ul class="toctree nav nav-list">']
    builder = _NavBuilder(parts, project, master_path, _get_toctree)


    # Special project used standalone
    if project == 'SQL 99':
        current_class = ' class="current"' if pagename == master_doc else ''
        parts.append(f'<li{current_class}>')
        parts.append(f'<a class="current-active" href="{master_path}">SQL-99 Complete, Really</a>')
        parts.append(_get_toctree(maxdepth=2))
        parts.append('</li>')
        return ''.join(parts)

    # Driver projects use a standalone primary navigation
    if project in ['CrateDB JDBC', 'CrateDB Npgsql', 'CrateDB DBAL', 'CrateDB PDO', 'CrateDB Python', 'SQLAlchemy Dialect']:
        current_class = ' class="current"' if pagename == master_doc else ''
        parts.append(f'<li{current_class}>')
        parts.append(f'<a class="current-active" href="{master_path}">Documentation</a>')
        parts.append(_get_toctree())
        parts.append('</li>')
        parts.append('<li class="navleft-item border-top"><a href="https://cratedb.com/docs/guide/connect/">All database drivers</a></li>')
        return ''.join(parts)


    # Start CrateDB docs TOC with a Search box
    parts.append('<li>')
    parts.append('<div class="search-link">')
    parts.append('<div id="docsearch" style="min-height: 36px; margin-bottom: 20px;"></div>')
    parts.append('</div>')
    parts.append('</li>')

    # Add Guide's toctree entries (Overview, Getting Started, captions, etc.)
    if project == 'CrateDB: Guide':
        toctree_html = _get_toctree()
        # Rewrite the Overview sidebar link to point to root (index.md)
        # instead of overview/. The overview content lives in index.md;
        # overview/index.md is only kept for toctree structure.
        toctree_html = re.sub(
            r'href="([^"]*overview/(?:index\.html)?)"',
            f'href="{master_path}"',
            toctree_html
        )
        # Add icons to captions
        toctree_html = toctree_html.replace(
            '<span class="caption-text">Build</span>',
            f'{ICON_BUILD}<span class="caption-text">Build</span>'
        )
        toctree_html = toctree_html.replace(
            '<span class="caption-text">Operations</span>',
            f'{ICON_OPERATIONS}<span class="caption-text">Operations</span>'
        )
        parts.append(toctree_html)
    else:
        # Show Guide's navigation structure when viewing other projects
        # This must be kept in sync with the Guide's index.md toctree
        builder.add_nav_link('Overview', '/docs/guide/')
        builder.add_nav_link('Getting Started', '/docs/guide/start/')

        # BUILD section
        parts.append(f'<p class="caption" role="heading">{ICON_BUILD}<span class="caption-text">Build</span></p>')
        builder.add_nav_link('Load data into CrateDB', '/docs/guide/ingest/')
        builder.add_nav_link('Connect / Drivers', '/docs/guide/connect/')
        builder.add_nav_link('Integrations', '/docs/guide/integrate/')
        builder.add_nav_link('All Features', '/docs/guide/feature/')

        # OPERATIONS section
        parts.append(f'<p class="caption" role="heading">{ICON_OPERATIONS}<span class="caption-text">Operations</span></p>')
        builder.add_nav_link('Installation', '/docs/guide/install/')
        builder.add_nav_link('Administration', '/docs/guide/admin/')
        builder.add_nav_link('Performance guides', '/docs/guide/performance/')

    # Add Reference section with caption
    parts.append(f'<p class="caption" role="heading">{ICON_REFERENCE}<span class="caption-text">References</span></p>')
    builder.add_project_nav_item('CrateDB Cloud', 'CrateDB Cloud', '/docs/cloud/')
    builder.add_project_nav_item('CrateDB: Reference', 'CrateDB', '/docs/crate/reference/')

    # Add Tools section with caption
    parts.append(f'<p class="caption" role="heading">{ICON_TOOLS}<span class="caption-text">Tools</span></p>')
    builder.add_project_nav_item('CrateDB: Admin UI', 'Admin UI', '/docs/crate/admin-ui/')
    builder.add_project_nav_item('CrateDB: Crash CLI', 'CrateDB CLI', '/docs/crate/crash/')
    builder.add_project_nav_item('CrateDB Cloud: Croud CLI', 'Cloud CLI', '/docs/cloud/cli/')

    # Add Support and Community links section after a border
    parts.append('<li class="navleft-item border-top"><a class="external-link" target="_blank" href="/support/">Support</a></li>')
    parts.append('<li class="navleft-item"><a class="external-link" target="_blank" href="https://community.cratedb.com/">Community</a></li>')

    # Other internal docs projects only included in special builds
    builder.add_project_nav_item('CrateDB documentation theme', 'Documentation theme', '', border_top=True, public_docs=False)
    builder.add_project_nav_item('Doing Docs', 'Doing Docs at CrateDB', '', public_docs=False)

    # Show build timestamp for local development (not on Read the Docs)
    if not os.environ.get('READTHEDOCS'):
        build_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        parts.append(f'<li class="navleft-item border-top" style="font-size: 0.75em; color: #888; padding-top: 1em;">')
        parts.append(f'Built: {build_time}')
        parts.append('</li>')

    parts.append('</ul>')
    return ''.join(parts)


def add_crate_navigation(app, pagename, templatename, context, doctree):
    """
    Sphinx event handler: Add enhanced navigation to template context.

    Generates multi-project navigation HTML and processes it through
    Furo's navigation enhancer to add collapsible icons and checkboxes.

    Note: Signature matches Sphinx's html-page-context event handler requirements.
    """
    # Unused parameters required by Sphinx event signature
    _ = app, pagename, templatename, doctree

    navigation_html = _generate_crate_navigation_html(context)

    # Process through Furo's navigation enhancer
    enhanced_navigation = get_navigation_tree(navigation_html)

    # Make checkbox IDs unique per project to prevent localStorage state collision.
    # Furo generates sequential IDs (toctree-checkbox-1, toctree-checkbox-2, etc.)
    # which collide across projects. Add project slug prefix to make them unique.
    project_slug = _slugify_id(context.get("project", ""))
    if project_slug:
        enhanced_navigation = re.sub(
            r'toctree-checkbox-(\d+)',
            f'toctree-checkbox-{project_slug}-\\1',
            enhanced_navigation
        )

    # Add to context for use in templates
    context["crate_navigation_tree"] = enhanced_navigation

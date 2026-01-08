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


def _generate_crate_navigation_html(context):
    """
    Generate multi-project navigation HTML structure, so we can process it
    through Furo's navigation enhancer.
    """
    toctree = context.get("toctree")
    if not toctree:
        return ""

    theme_globaltoc_includehidden = context.get("theme_globaltoc_includehidden", True)
    def get_toctree(maxdepth=-1, titles_only=True, collapse=False):
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

    def _add_project_nav_item(
        project_name,
        display_name,
        url_if_not_current,
        border_top=False,
        include_toctree=True,
        only_if_current_project=False
    ):
        """Add a navigation item in left navbar for a specific project."""
        border = " border-top" if border_top else ""
        if project == project_name:
            parts.append(f'<li class="current{border}">')
            parts.append(f'<a class="current-active" href="{master_path}">{display_name}</a>')
            if include_toctree:
                parts.append(get_toctree())
            parts.append('</li>')
        else:
            if only_if_current_project:
                return
            parts.append(f'<li class="navleft-item{border}"><a href="{url_if_not_current}">{display_name}</a></li>')


    # Special project used standalone
    if project == 'SQL 99':
        current_class = ' class="current"' if pagename == master_doc else ''
        parts.append(f'<li{current_class}>')
        parts.append(f'<a class="current-active" href="{master_path}">SQL-99 Complete, Really</a>')
        parts.append(get_toctree(maxdepth=2))
        parts.append('</li>')
        return ''.join(parts)


    # Start CrateDB docs TOC with a Search box
    parts.append('<li>')
    parts.append('<div class="search-link">')
    parts.append('<div id="docsearch" style="min-height: 36px; margin-bottom: 20px;"></div>')
    parts.append('</div>')
    parts.append('</li>')

    # Add Overview and top level entries defined in the Guide's toctree
    if project == 'CrateDB: Guide':
        if pagename == 'index':
            parts.append('<li class="current">')
            parts.append(f'<a class="current-active" href="{master_path}">Overview</a>')
            parts.append('</li>')
        else:
            parts.append('<li class="navleft-item">')
            parts.append(f'<a href="{master_path}">Overview</a>')
            parts.append('</li>')
        parts.append(get_toctree())
    else:
        parts.append('<li class="current"><a class="current-active" href="#">Overview</a></li>')

    # Add individual projects
    _add_project_nav_item('CrateDB Cloud', 'CrateDB Cloud', '/docs/cloud/')
    _add_project_nav_item('CrateDB: Reference', 'Reference Manual', '/docs/crate/reference/')

    # Start new section with a border
    _add_project_nav_item('CrateDB: Admin UI', 'Admin UI', '/docs/crate/admin-ui/', border_top=True)
    _add_project_nav_item('CrateDB: Crash CLI', 'CrateDB CLI', '/docs/crate/crash/')
    _add_project_nav_item('CrateDB Cloud: Croud CLI', 'Cloud CLI', '/docs/cloud/cli/')

    # Add all Driver projects
    parts.append('<li class="navleft-item">')
    parts.append('<a href="/docs/guide/connect/drivers.html">Database Drivers</a>')
    parts.append('</li>')

    _DRIVER_CONFIGS = [
        ('CrateDB JDBC', 'JDBC', '/docs/jdbc/'),
        ('CrateDB DBAL', 'PHP DBAL', '/docs/dbal/'),
        ('CrateDB PDO', 'PHP PDO', '/docs/pdo/'),
        ('CrateDB Python', 'Python', '/docs/python/'),
        ('SQLAlchemy Dialect', 'SQLAlchemy', '/docs/sqlalchemy-cratedb/'),
    ]
    driver_projects = [config[0] for config in _DRIVER_CONFIGS]
    if project in driver_projects or (project == 'CrateDB: Guide' and pagename.startswith('connect')):
        parts.append('<li><ul>')
        for proj_name, display_name, url in _DRIVER_CONFIGS:
            _add_project_nav_item(proj_name, display_name, url)
        parts.append('</ul></li>')

    # Add Support and Community links section after a border
    parts.append('<li class="navleft-item border-top"><a target="_blank" href="/support/">Support</a></li>')
    parts.append('<li class="navleft-item"><a target="_blank" href="https://community.cratedb.com/">Community</a></li>')


    # Other internal docs projects only included in special builds
    _add_project_nav_item('CrateDB documentation theme', 'Documentation theme', '',
                          border_top=True, only_if_current_project=True)
    _add_project_nav_item('Doing Docs', 'Doing Docs at CrateDB', '',
                          only_if_current_project=True)

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

    # Add to context for use in templates
    context["crate_navigation_tree"] = enhanced_navigation

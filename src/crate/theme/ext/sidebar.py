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

import typing as t

from sphinx.builders.html import StandaloneHTMLBuilder

from sphinx_design_elements.lib.linktree import LinkTree


def make_primary_tree(builder: StandaloneHTMLBuilder, context: t.Dict[str, t.Any]) -> LinkTree:
    """
    A navigation tree demo defined with Python code.

    It includes two sections:

    - The vanilla toctree of the project at hand..
    - A linktree composed of Sphinx references or URLs.
    """
    project_name = context["project"]

    # Create LinkTree component.
    linktree = LinkTree.from_context(builder=builder, context=context)
    linktree.remove_from_title("CrateDB")
    doc = linktree.api.doc
    ref = linktree.api.ref
    link = linktree.api.link

    # Add section about project (self).
    project = \
        linktree \
            .project(docname=project_name, title=project_name)

    # .title("Customized TocTree") \

    # 1. On specific projects, add the vanilla toctree.
    #    Here, also customize it for demonstration purposes.
    if project_name == "CrateDB documentation theme":

        # Add vanilla project toctree.
        project.toctree()

        # Add custom navigation items.
        # TODO: Find a way to pull additional navigation hints from project
        #       markup itself, in order to get rid of this anomaly.
        project.add(
            doc(name="admonitions", label="Admonitions"),
            doc(name="codesnippets", label="Code snippets"),
            doc(name="myst/mermaid", label="Mermaid diagrams, written in Markdown"),
        )

    # 2. Add section with links to intersphinx targets.

    # CrateDB Database.
    linktree \
        .title("CrateDB Database") \
        .add(
            ref(target="crate-reference:index", label="CrateDB Reference"),
            ref(target="crate-tutorials:index", label="Install CrateDB"),
            ref(target="crate-howtos:index", label="Getting started"),
        )

    # CrateDB Cloud.
    linktree \
        .title("CrateDB Cloud") \
        .add(
            ref("cloud-reference:index"),
            ref("cloud-tutorials:index"),
            ref("cloud-howtos:index"),
            ref("cloud-cli:index"),
        )

    # CrateDB clients.
    linktree \
        .title("Clients") \
        .add(
            ref("crate-admin-ui:index"),
            ref("crate-crash:index"),
            ref("crate-clients-tools:index"),
            ref("crate-jdbc:index"),
            ref("crate-npgsql:index"),
            ref("crate-dbal:index"),
            ref("crate-pdo:index"),
            ref("crate-python:index"),
        )

    # Other links.
    linktree \
        .title("Miscellaneous") \
        .add(
            link(uri="https://crate.io/support/", label="Support"),
            link(uri="https://community.crate.io/", label="Community"),
            link(uri="https://community.crate.io/t/overview-of-cratedb-integration-tutorials/1015", label="Integration tutorials"),
            link(uri="https://github.com/crate/cratedb-examples", label="Stacks and examples"),
            link(uri="https://github.com/crate/crate-sample-apps", label="Sample applications"),
            ref("sql-99:index"),
            # ref("crate-docs-theme:index"),
            # ref("crate-docs:index"),
    )

    return linktree

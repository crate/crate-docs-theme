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

import logging
import typing as t

from sphinx.application import Sphinx

from crate.theme.ext.sidebar import make_primary_tree
from crate.theme.rtd import __version__
from sphinx.builders.html import StandaloneHTMLBuilder

logger = logging.getLogger(__name__)


def html_page_context(
        app: Sphinx,
        pagename: str,
        templatename: str,
        context: t.Dict[str, t.Any],
        doctree: t.Any,
) -> None:
    """
    Sphinx HTML page context provider.
    """
    if not isinstance(app.builder, StandaloneHTMLBuilder):
        raise Exception(
            "Theme is being used with a non-HTML builder. "
            "If you're seeing this error, it is a symptom of a mistake in your "
            "configuration."
        )

    # Basic constants
    context["theme_version"] = __version__

    # Navigation tree component from `sphinx-design-elements`.
    try:
        primary_tree = make_primary_tree(builder=app.builder, context=context)
        context["ng_navigation_tree"] = primary_tree.render()
    except Exception as ex:
        logger.exception("Unable to compute primary navigation tree")

"""
Vendored version of Furo's navigation tree component.

https://github.com/pradyunsg/furo/blob/main/src/furo/navigation.py
"""
import sphinx
import typing as t

from furo import get_navigation_tree

from crate.theme.rtd import __version__
from sphinx.builders.html import StandaloneHTMLBuilder


def furo_compute_navigation_tree(context: t.Dict[str, t.Any]) -> str:
    """
    The navigation tree, generated from the sphinx-provided ToC tree.
    """
    if "toctree" in context:
        toctree = context["toctree"]
        toctree_html = toctree(
            collapse=False,
            titles_only=True,
            maxdepth=-1,
            includehidden=True,
        )
    else:
        toctree_html = ""

    return get_navigation_tree(toctree_html)


def _html_page_context(
    app: sphinx.application.Sphinx,
    pagename: str,
    templatename: str,
    context: t.Dict[str, t.Any],
    doctree: t.Any,
) -> None:
    """
    HTML page context provider.
    """
    if not isinstance(app.builder, StandaloneHTMLBuilder):
        raise Exception(
            "Theme is being used with a non-HTML builder. "
            "If you're seeing this error, it is a symptom of a mistake in your "
            "configuration."
        )

    # Basic constants
    context["theme_version"] = __version__

    # Values computed from page-level context.
    context["ng_navigation_tree"] = furo_compute_navigation_tree(context)

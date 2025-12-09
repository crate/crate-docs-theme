from crate.theme.rtd.conf.theme import *

# Note: TOC toggle icons are enabled by default in the theme.
# To disable: html_theme_options["toc_toggle_icons"] = "false"

# Mimic some bits of the RTD context being propagated to its Sphinx builder.
# https://github.com/readthedocs/readthedocs.org/blob/main/readthedocs/doc_builder/backends/sphinx.py
html_context.update({

    # Generic settings.
    "conf_py_path": "/docs/",
    "source_suffix": source_suffix,

    # Enable version chooser.
    "display_version": True,
    "current_version": "foobar",
    "versions": [("foobar", None), ("bazqux", None)],

    # Enable feedback widget and source/edit links.
    "display_github": True,
    "github_user": "crate",
    "github_repo": "crate-docs-theme",
    "github_version": "main",
})


# `html_context_custom` will be applied to the HTML context after the RTD
# builder was initialized.

# This snippet disables the GitHub feedback area for demonstration purposes.
# It can be used on individual projects where this is needed.
html_context_custom.update({
    #"display_github": False,
})


intersphinx_mapping["myst"] = ("https://myst-parser.readthedocs.io/en/latest/", None)
intersphinx_mapping["sd"] = ("https://sphinx-design.readthedocs.io/en/latest/", None)
intersphinx_mapping["sde"] = ("https://sphinx-design-elements.readthedocs.io/en/latest/", None)

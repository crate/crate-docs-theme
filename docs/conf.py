from crate.theme.rtd.conf.fake import *

# Mimic some bits of the RTD context to be propagated to its Sphinx builder.
# https://github.com/readthedocs/readthedocs.org/blob/main/readthedocs/doc_builder/backends/sphinx.py
html_context.update({
    "display_github": True,
    "github_user": "crate",
    "github_repo": "crate-docs-theme",
    "github_version": "main",
    "conf_py_path": "/docs/",
    "source_suffix": source_suffix,
})


# `html_context_custom` will be applied to the HTML context after the RTD
# builder was initialized.

# This snippet disables the GitHub feedback area for demonstration purposes.
# It can be used on individual projects where this is needed.
html_context_custom.update({
    #"display_github": False,
})

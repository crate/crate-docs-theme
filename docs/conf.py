from crate.theme.rtd.conf.fake import *

html_context = {
    "display_github": True,
    "github_user": "crate",
    "github_repo": "crate-docs-theme",
    "github_version": "main",
    "conf_py_path": "/docs/",
    "source_suffix": source_suffix,
}


# Enable version chooser element `version-select-container` by providing
# corresponding attributes as propagated by readthedocs.
html_context.update({

    # Turn on versioning and announce the current version the user is displaying.
    "versioning": True,
    "current_version": "2.2",

    # List of available versions, for populating the version chooser.
    # Tuples of `slug, url`, but `slug` is not used.
    "versions": [
        ["latest", None],
        ["older", None],
        ["2.4", None],
        ["2.2", None],
        ["1.2", None],
    ],

    # Needed for computing the appropriate URL, see `layout.html`.
    "rtd_language": "en",
})

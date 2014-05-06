import crate.rtd_theme

copyright = u'2014, CRATE Technology GmbH'

# The suffix of source filenames.
source_suffix = '.txt'
exclude_patterns = ['requirements.txt']

# The master toctree document.
master_doc = 'index'
exclude_trees = ['pyenv', 'tmp', 'out', 'parts', 'clients', 'eggs']
extensions = ['sphinx.ext.autodoc']

# Configure the theme
html_theme = 'crate'
html_theme_path = crate.rtd_theme.get_html_theme_path()
nitpicky = True
html_show_sourcelink = False
html_sidebars = {'**': ['sidebar.html', 'sourcelink.html']}
html_theme_options = {
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': 'navbar navbar-inverse',

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': 'true',

    'globaltoc_includehidden': 'true',

    'cannonical_url_path': '',
}

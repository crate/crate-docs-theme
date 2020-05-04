from crate.theme.rtd.conf.standalone import *

source_suffix = '.rst'

exclude_patterns = ['.*', '*.lint', 'README.rst']

master_doc = 'index'

extensions = ['sphinx_sitemap']
site_url = 'https://crate-docs-theme.readthedocs.io/en/latest/'

html_context = {
  "display_github": True,
  "github_user": "crate",
  "github_repo": "crate-docs-theme",
  "github_version": "master",
  "conf_py_path": "/docs/",
  "source_suffix": source_suffix,
}

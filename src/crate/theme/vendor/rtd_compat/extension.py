import os

from sphinx import version_info
from sphinx.util import logging

import requests

from .utils import get_github_username_repo, get_bitbucket_username_repo, get_gitlab_username_repo


logger = logging.getLogger(__name__)


# https://www.sphinx-doc.org/en/stable/extdev/appapi.html#event-html-page-context
def manipulate_config(app, config):
    logger.info(
        'Running "manipulate_config" from Read the Docs "sphinx_build_compatibility" extension. '
        'Consider removing it from your requirements and migrating your documentation accordingly. '
        'This extension is useful only as a transition but it will not be maintained.'
    )

    # Add Read the Docs' static path.
    # Add to the end because it overwrites previous files.
    if not hasattr(config, "html_static_path"):
        config.html_static_path = []
    if os.path.exists('_static'):
        config.html_static_path.append('_static')

    # Define this variable in case it's not defined by the user.
    # It defaults to `alabaster` which is the default from Sphinx.
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme
    if not hasattr(config, "html_theme"):
        config.html_theme = 'alabaster'

    # Example: ``/docs/``
    conf_py_path = "/"
    conf_py_path += os.path.relpath(
            str(app.srcdir),
            os.environ.get("READTHEDOCS_REPOSITORY_PATH"),
        ).strip("/")
    conf_py_path += "/"

    git_clone_url = os.environ.get("READTHEDOCS_GIT_CLONE_URL")
    github_user, github_repo = get_github_username_repo(git_clone_url)
    bitbucket_user, bitbucket_repo = get_bitbucket_username_repo(git_clone_url)
    gitlab_user, gitlab_repo = get_gitlab_username_repo(git_clone_url)

    project_slug = os.environ.get("READTHEDOCS_PROJECT")
    version_slug = os.environ.get("READTHEDOCS_VERSION")
    production_domain = os.environ.get("READTHEDOCS_PRODUCTION_DOMAIN", "readthedocs.org")

    scheme = "https"
    if production_domain.startswith("devthedocs"):
        scheme = "http"

    # We are using APIv2 to pull active versions, downloads and subprojects
    # because APIv3 requires a token.
    try:
        response_project = requests.get(
            f"{scheme}://{production_domain}/api/v3/projects/{project_slug}/",
            timeout=2,
        ).json()
        language = response_project["language"]["code"]
    except Exception:
        logger.warning(
            "An error ocurred when hitting API to fetch project language. Defaulting to 'en'.",
            exc_info=True,
        )
        language = "en"

    try:
        response_versions = requests.get(
            f"{scheme}://{production_domain}/api/v3/projects/{project_slug}/versions/?active=true",
            timeout=2,
        ).json()
        versions = [
            (version["slug"], f"/{language}/{version['slug']}/")
            for version in response_versions["results"]
        ]
    except Exception:
        logger.warning(
            "An error ocurred when hitting API to fetch active versions. Defaulting to an empty list.",
            exc_info=True,
        )
        versions = []

    try:
        downloads = []
        for version in response_versions["results"]:
            if version["slug"] != version_slug:
                continue

            for key, value in version["downloads"]:
                downloads.append(
                    (
                        key,
                        value,
                    ),
                )
    except Exception:
        logger.warning(
            "An error ocurred when generating the list of downloads. Defaulting to an empty list.",
            exc_info=True,
        )
        downloads = []

    try:
        subprojects = []
        response_project = requests.get(
            f"{scheme}://{production_domain}/api/v2/project/?slug={project_slug}",
            timeout=2,
        ).json()
        project_id = response_project["results"][0]["id"]

        response_subprojects = requests.get(
            f"{scheme}://readthedocs.org/api/v2/project/{project_id}/subprojects/",
            timeout=2,
        ).json()
        for subproject in response_subprojects["subprojects"]:
            subprojects.append(
                (
                    subproject["slug"],
                    subproject["canonical_url"],
                ),
            )
    except Exception:
        logger.warning(
            "An error ocurred when hitting API to fetch project/subprojects. Defaulting to an empty list.",
            exc_info=True,
        )
        subprojects = []

    # Add project information to the template context.
    context = {
        'html_theme': config.html_theme,
        'current_version': os.environ.get("READTHEDOCS_VERSION_NAME"),
        'version_slug': version_slug,

        # NOTE: these are used to dump them in some JS files and to build the URLs in flyout.
        # However, we are replacing them with the new Addons.
        # I wouldn't include them in the first version of the extension.
        # We could hardcode them if we want, tho.
        #
        # 'MEDIA_URL': "{{ settings.MEDIA_URL }}",
        # 'STATIC_URL': "{{ settings.STATIC_URL }}",
        # 'proxied_static_path': "{{ proxied_static_path }}",

        'PRODUCTION_DOMAIN': production_domain,
        'versions': versions,
        "downloads": downloads,
        "subprojects": subprojects,

        'slug': project_slug,
        'rtd_language': os.environ.get("READTHEDOCS_LANGUAGE"),
        'canonical_url': os.environ.get("READTHEDOCS_CANONICAL_URL"),

        # NOTE: these seem to not be used.
        # 'name': u'{{ project.name }}',
        # 'analytics_code': '{{ project.analytics_code }}',
        # 'single_version': {{ project.is_single_version }},
        # 'programming_language': u'{{ project.programming_language }}',

        'conf_py_path': conf_py_path,
        # Used only for "readthedocs-sphinx-ext" which we are not installing anymore.
        # 'api_host': '{{ api_host }}',
        # 'proxied_api_host': '{{ project.proxied_api_host }}',

        'github_user': github_user,
        'github_repo': github_repo,
        'github_version': os.environ.get("READTHEDOCS_GIT_IDENTIFIER"),
        'display_github': github_user is not None,
        'bitbucket_user': bitbucket_user,
        'bitbucket_repo': bitbucket_repo,
        'bitbucket_version': os.environ.get("READTHEDOCS_GIT_IDENTIFIER"),
        'display_bitbucket': bitbucket_user is not None,
        'gitlab_user': gitlab_user,
        'gitlab_repo': gitlab_repo,
        'gitlab_version': os.environ.get("READTHEDOCS_GIT_IDENTIFIER"),
        'display_gitlab': gitlab_user is not None,
        'READTHEDOCS': True,
        'using_theme': (config.html_theme == "default"),
        'new_theme': (config.html_theme == "sphinx_rtd_theme"),
        'source_suffix': ".rst",
        'ad_free': False,
        'docsearch_disabled': False,

        # We don't support Google analytics anymore.
        # See https://github.com/readthedocs/readthedocs.org/issues/9530
        'user_analytics_code': "",
        'global_analytics_code': None,

        'commit': os.environ.get("READTHEDOCS_GIT_COMMIT_HASH")[:8],
    }

    # For sphinx >=1.8 we can use html_baseurl to set the canonical URL.
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl
    if version_info >= (1, 8):
        if not hasattr(config, 'html_baseurl'):
            config.html_baseurl = context['canonical_url']
        context['canonical_url'] = None


    if hasattr(config, 'html_context'):
        for key in context:
            if key not in config.html_context:
                config.html_context[key] = context[key]
    else:
        config.html_context = context

    project_language = os.environ.get("READTHEDOCS_LANGUAGE")

    # User's Sphinx configurations
    language_user = config.language
    latex_engine_user = config.latex_engine
    latex_elements_user = config.latex_elements

    # Remove this once xindy gets installed in Docker image and XINDYOPS
    # env variable is supported
    # https://github.com/rtfd/readthedocs-docker-images/pull/98
    latex_use_xindy = False

    chinese = any([
        language_user in ('zh_CN', 'zh_TW'),
        project_language in ('zh_CN', 'zh_TW'),
    ])

    japanese = any([
        language_user == 'ja',
        project_language == 'ja',
    ])

    if chinese:
        config.latex_engine = latex_engine_user or 'xelatex'

        latex_elements_rtd = {
            'preamble': '\\usepackage[UTF8]{ctex}\n',
        }
        config.latex_elements = latex_elements_user or latex_elements_rtd
    elif japanese:
        config.latex_engine = latex_engine_user or 'platex'

    # Make sure our build directory is always excluded
    if not hasattr(config, "exclude_patterns"):
        config.exclude_patterns = []
    config.exclude_patterns.extend(['_build'])


def setup(app):
    app.connect('config-inited', manipulate_config)

    return {
        'version': "0.0.0",
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

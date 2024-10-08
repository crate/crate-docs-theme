import re

# Borrowed from
# https://github.com/readthedocs/readthedocs.org/blob/25e697f1ee63828bba65f41d0c8724769d70402f/readthedocs/projects/constants.py#L345-L366
GITHUB_REGEXS = [
    re.compile(r"github.com/(.+)/(.+)(?:\.git){1}$"),
    # This must come before the one without a / to make sure we don't capture the /
    re.compile(r"github.com/(.+)/(.+)/"),
    re.compile(r"github.com/(.+)/(.+)"),
    re.compile(r"github.com:(.+)/(.+)\.git$"),
]
BITBUCKET_REGEXS = [
    re.compile(r"bitbucket.org/(.+)/(.+)\.git$"),
    re.compile(r"@bitbucket.org/(.+)/(.+)\.git$"),
    # This must come before the one without a / to make sure we don't capture the /
    re.compile(r"bitbucket.org/(.+)/(.+)/"),
    re.compile(r"bitbucket.org/(.+)/(.+)"),
    re.compile(r"bitbucket.org:(.+)/(.+)\.git$"),
]
GITLAB_REGEXS = [
    re.compile(r"gitlab.com/(.+)/(.+)(?:\.git){1}$"),
    # This must come before the one without a / to make sure we don't capture the /
    re.compile(r"gitlab.com/(.+)/(.+)/"),
    re.compile(r"gitlab.com/(.+)/(.+)"),
    re.compile(r"gitlab.com:(.+)/(.+)\.git$"),
]


# Borrowed from
# https://github.com/readthedocs/readthedocs.org/blob/25e697f1ee63828bba65f41d0c8724769d70402f/readthedocs/builds/utils.py#L24-L48
def get_github_username_repo(url):
    if "github" in url:
        for regex in GITHUB_REGEXS:
            match = regex.search(url)
            if match:
                return match.groups()
    return (None, None)


def get_bitbucket_username_repo(url=None):
    if "bitbucket" in url:
        for regex in BITBUCKET_REGEXS:
            match = regex.search(url)
            if match:
                return match.groups()
    return (None, None)


def get_gitlab_username_repo(url=None):
    if "gitlab" in url:
        for regex in GITLAB_REGEXS:
            match = regex.search(url)
            if match:
                return match.groups()
    return (None, None)

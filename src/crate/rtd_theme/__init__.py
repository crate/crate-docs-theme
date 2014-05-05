"""Crate Theme"""
import os

VERSION = (0, 6, 1)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__

def current_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_html_theme_path():
    """Return list of HTML theme paths."""
    return [current_dir()]

def get_html_static_path():
    """Return list of HTML static paths."""
    cur_dir = current_dir()
    return [
        os.path.join(cur_dir, 'crate', 'static'),
    ]

def get_html_template_path():
    """Return list of HTML template paths."""
    cur_dir = current_dir()
    return [
        os.path.join(cur_dir, 'crate'),
    ]

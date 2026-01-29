"""Configuration file for Sphinx."""

# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

import pathlib

import toml

THIS_DIR = pathlib.Path(__file__).absolute().parent


def read_version() -> str:
    """Read the version from the pyproject.toml file."""
    config_path = THIS_DIR.parent.parent / "pyproject.toml"
    config = toml.load(str(config_path))
    return config["project"]["version"]


# -- Project information -----------------------------------------------------

project = "OKPaletteLab"
copyright = "2026, Kenta Kabashima"
author = "Kenta Kabashima"
release = read_version()

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
templates_path: list[str] = []
exclude_patterns: list[str] = []

autodoc_default_options = {
    "no-value": True,
}

# -- Options for Myst-NB -----------------------------------------------------

extensions += ["myst_nb"]  # This will automatically include myst_parser

myst_heading_anchors = 4

nb_execution_mode = "cache"
nb_execution_cache_path = str(THIS_DIR.parent / "jupyter_cache")

# setting of MathJax
# Extension for MathJax is already enabled by myst_nb.
# MathJax URL working with Plotly was written in https://www.npmjs.com/package/plotly.js/v/3.0.1.
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_orange_book_theme"
html_title = project
html_logo = "../icon/icon_for_docs.svg"
html_favicon = "../icon/icon.svg"
html_theme_options = {
    "show_prev_next": False,
    "logo": {
        "text": html_title,
    },
    "pygments_light_style": "gruvbox-light",
    "pygments_dark_style": "native",
    "repository_url": "https://gitlab.com/MusicScience37Projects/utility-libraries/OKPaletteLab",
    "use_repository_button": True,
}

html_static_path: list[str] = []

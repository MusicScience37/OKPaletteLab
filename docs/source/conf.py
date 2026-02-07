"""Configuration file for Sphinx."""

# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

import pathlib

THIS_DIR = pathlib.Path(__file__).absolute().parent


# -- Project information -----------------------------------------------------

project = "OKPaletteLab"
copyright = "2026, Kenta Kabashima"
author = "Kenta Kabashima"
release = "dev"

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
html_favicon = "../icon/icon.svg"
html_theme_options = {
    "show_prev_next": False,
    "logo": {
        "image_light": "../icon/icon_for_docs.svg",
        "image_dark": "../icon/icon_for_docs_dark.svg",
        "text": html_title,
    },
    "pygments_light_style": "gruvbox-light",
    "pygments_dark_style": "native",
    "repository_url": "https://gitlab.com/MusicScience37Projects/utility-libraries/OKPaletteLab",
    "use_repository_button": True,
}

html_static_path: list[str] = ["_static"]
html_css_files = [
    "ok_palette_lab_custom.css",
]

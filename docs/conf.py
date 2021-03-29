# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

file_loc = os.path.split(__file__)[0]
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(file_loc), ".")))

# -- Project information -----------------------------------------------------

project = "ColorDetect"
copyright = "2020, Marvin Kweyu"
author = "Marvin Kweyu"

# The full version, including alpha/beta/rc tags
release = "1.4.3"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # grab documentation from docstrings
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",  # package rst sources with docs
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

html_logo = "../img/ColorDetect.png"

html_theme_options = {
    "description": "Recognize and identify different colors in an image or video.",
    "fixed_sidebar": True,
    "logo_text_align": "justify",
    "show_relbar_bottom": True,
    'github_user': 'MarvinKweyu',
    'github_repo': 'ColorDetect',
    "github_button": True,
    # "show_related": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

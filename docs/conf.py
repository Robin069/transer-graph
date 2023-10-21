# flake8: noqa

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
from typing import List

sys.path.append(os.path.abspath("../.."))
sys.path.append(os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "transfer_graph"
copyright = "2022, statworx"
author = "statworx"

# The full version, including alpha/beta/rc tags
release = "0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # Core Sphinx library for auto html doc generation from docstrings
    "sphinx.ext.viewcode",  # Add a link to the Python source code for classes, functions etc.
    "sphinx.ext.napoleon",
    "myst_parser",
    "matplotlib.sphinxext.plot_directive",  # include plots
    "sphinx.ext.githubpages",
]

autodoc_inherit_docstrings = True  # If no docstring, inherit from base class
add_module_names = False  # Remove namespaces from class/method signatures

# Add any paths that contain templates here, relative to this directory.
templates_path: List[str] = []


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "furo"

html_theme_options = {
    "light_logo": "statworx-Logo-White.png",
    "dark_logo": "statworx-Logo-White.png",
    "light_css_variables": {
        "color-brand-primary": "white",
        "color-brand-content": "#283440",
        "color-content-foreground": "black",
        "color-sidebar-caption-text": "white",
        "color-sidebar-background": "black",
        "color-sidebar-search-foreground": "white",
        "color-sidebar-link-text": "#EBF0F2",
        "color-sidebar-search-border": "#303335",
        "color-background-hover": "#1c1c1c",
        "color-toc-item-text--active": "black",
        "color-admonition-title-background--note": "rgba(0,0,255,.1)",
        "color-admonition-title--note": "#0000FF",
        "color-api-keyword": "black",
        "color-api-pre-name": "#FE0D6C",
        "color-api-name": "#FE0D6C",
        "color-api-overall": "#283440",
    },
    "dark_css_variables": {
        "color-background-primary": "black",
        "color-brand-primary": "white",
        "color-brand-content": "white",
        "color-content-foreground": "white",
        "color-sidebar-caption-text": "white",
        "color-sidebar-background": "black",
        "color-sidebar-search-foreground": "white",
        "color-sidebar-link-text": "#EBF0F2",
        "color-background-hover": "#1c1c1c",
        "color-toc-item-text--active": "white",
        "color-admonition-background": "#1c1c1c",
        "color-admonition-title-background--note": "rgba(68,127,207,.1)",
        "color-admonition-title--note": "rgb(68,127,207)",
        "color-api-keyword": "white",
        "color-api-pre-name": "#FE0D6C",
        "color-api-name": "#FE0D6C",
        "color-api-overall": "white",
    },
    "sidebar_hide_name": True,
    "footer_icons": [
        {
            "name": "Linkedin",
            "url": "https://www.linkedin.com/company/statworx/",
            "html": """
                <svg height="72" viewBox="0 0 72 72" width="72" xmlns="http://www.w3.org/2000/svg">
                    <g fill="none" fill-rule="evenodd"><path d="M36,72 L36,72 C55.882251,72 72,55.882251 72,36 L72,36 C72,16.117749 55.882251,-3.65231026e-15 36,0 L36,0 C16.117749,3.65231026e-15 -2.4348735e-15,16.117749 0,36 L0,36 C2.4348735e-15,55.882251 16.117749,72 36,72 Z" fill="#007EBB"/><path d="M59,57 L49.959375,57 L49.959375,41.6017895 C49.959375,37.3800228 48.3552083,35.0207581 45.0136719,35.0207581 C41.3785156,35.0207581 39.4792969,37.4759395 39.4792969,41.6017895 L39.4792969,57 L30.7666667,57 L30.7666667,27.6666667 L39.4792969,27.6666667 L39.4792969,31.6178624 C39.4792969,31.6178624 42.0989583,26.7704897 48.3236979,26.7704897 C54.5455729,26.7704897 59,30.5699366 59,38.4279486 L59,57 Z M20.372526,23.8257036 C17.4048177,23.8257036 15,21.4020172 15,18.4128518 C15,15.4236864 17.4048177,13 20.372526,13 C23.3402344,13 25.7436198,15.4236864 25.7436198,18.4128518 C25.7436198,21.4020172 23.3402344,23.8257036 20.372526,23.8257036 Z M15.8736979,57 L24.958724,57 L24.958724,27.6666667 L15.8736979,27.6666667 L15.8736979,57 Z" fill="#FFF"/>
                    </g>
                </svg>
            """,
            "class": "",
        },
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "custom.css",
]


# -- Options for Latex output -------------------------------------------------

latex_engine = "xelatex"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
# latex_documents = [("index", "main.tex", project, author, "report")]

latex_maketitle = r"""
\begin{figure}[t!]
    \centering
    \includepdf[scale=1.1]{../../_static/landing_page.pdf}
\end{figure}
"""

latex_toc = r"""
{
  \hypersetup{linkcolor=black}
  \tableofcontents
}
"""

latex_printindex = r"""
\printindex

\begin{figure}[t!]
    \centering
    \includepdf[scale=1.1]{../../_static/last_page.pdf}
\end{figure}
"""

latex_elements = {
    "sphinxsetup": "TitleColor={RGB}{0,0,255}",
    "preamble": r"\usepackage{pdfpages} \usepackage{fontspec} \setmainfont{Arial} \usepackage{titlesec} \titleformat{\chapter}[hang] {\normalfont\LARGE\bfseries\color{blue}}{\thechapter.}{0.4em}{} ",
    "maketitle": latex_maketitle,
    "tableofcontents": latex_toc,
    "fncychap": "",
    "printindex": latex_printindex,
}

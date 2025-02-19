# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

import datetime

import xanimations


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

current_year = datetime.datetime.now().year
project = "xanimations"
copyright = f"2018\u2013{current_year}, xanimations maintainers"
author = "Julius Busecke"

# The short X.Y version
version = ".".join(xanimations.__version__.split(".")[:2])
# The full version, including alpha/beta/rc tags
release = xanimations.__version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.coverage',
    # 'sphinx.ext.mathjax',
    "sphinx-prompt",
    "sphinx_copybutton",
    "nbsphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Extension configuration -------------------------------------------------

autodoc_typehints = "description"
autodoc_default_options = {
    "members": True,
}

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

extlinks = {
    "issue": ("https://github.com/jbusecke/xanimations/issues/%s", "GH#"),
    "pull": ("https://github.com/jbusecke/xanimations/pull/%s", "PR#"),
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "xarray": ("https://xarray.pydata.org/en/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "dask": ("https://docs.dask.org/en/latest", None),
}

napoleon_numpy_docstring = True
napoleon_preprocess_types = True
napoleon_use_param = False
napoleon_use_rtype = False

napoleon_type_aliases = {
    "DataArray": "~xarray.DataArray",
    "Figure": "~matplotlib.figure.Figure",
    "Axes": "~matplotlib.axes.Axes",
    "Callable": "~typing.Callable",
}


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_book_theme"

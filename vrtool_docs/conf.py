# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'vrtool_docs'
copyright = '2023, Deltares'
author = 'Carles S. Soriano Perez'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


html_context = {
    "github_url": "https://github.com",  # or your GitHub Enterprise interprise
    "github_user": "Deltares",
    "github_repo": "VrtoolDocumentation",
    "github_version": "main",  # FIXME
    "doc_path": "docs",
    "default_mode": "light",
}
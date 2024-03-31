# Configuration file for the Sphinx documentation builder.

# -- Project information

# import os
# import sys

# import subprocess, os

# def configureDoxyfile(input_dir, output_dir):
#     with open('Doxyfile.in', 'r') as file :
#         filedata = file.read()

#     filedata = filedata.replace('@DOXYGEN_INPUT_DIR@', input_dir)
#     filedata = filedata.replace('@DOXYGEN_OUTPUT_DIR@', output_dir)
#     print('Here')

#     with open('Doxyfile', 'w') as file:
#         file.write(filedata)

# # Check if we're running on Read the Docs' servers
# read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

# breathe_projects = {}

# if True: #read_the_docs_build:
#     input_dir = '../CatCutifier'
#     output_dir = 'build'
#     configureDoxyfile(input_dir, output_dir)
#     subprocess.call('doxygen', shell=True)
#     breathe_projects['CatCutifier'] = output_dir + '/xml'

# sys.path.insert(0, os.path.abspath('../'))

project = 'RL Code'
copyright = '2024, Junxi'
author = 'Junxi'

release = ''
version = ''

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'breathe',
    'sphinx_copybutton',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'
html_title = "RL Code"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    'custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# # Breathe Configuration
# breathe_default_project = "CatCutifier"
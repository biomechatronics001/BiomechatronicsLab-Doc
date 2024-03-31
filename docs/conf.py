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

project = 'Test'
copyright = '2024, Junxi'
author = 'Junxi'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'breathe',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# # Breathe Configuration
# breathe_default_project = "CatCutifier"
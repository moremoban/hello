# -*- coding: utf-8 -*-
DESCRIPTION = (
    'demonstrate yehua usage' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'hello'
copyright = u'2017 your org'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'hellodoc'
latex_elements = {}
latex_documents = [
    ('index', 'hello.tex',
     'hello Documentation',
     'your org', 'manual'),
]
man_pages = [
    ('index', 'hello',
     'hello Documentation',
     [u'your org'], 1)
]
texinfo_documents = [
    ('index', 'hello',
     'hello Documentation',
     'your org', 'hello',
     DESCRIPTION,
     'Miscellaneous'),
]

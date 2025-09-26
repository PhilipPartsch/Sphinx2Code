# Configuration file for the Sphinx documentation builder.

import os
import sys
from sphinx_needs import __version__
print ('sphinx-needs version: ' + str(__version__))
from sphinx_needs.api import add_dynamic_function

sys.path.append(os.path.abspath('.'))

sys.path.append(os.path.abspath('./scripts'))
# For autodoc

# For merge_dicts and other scripts on this level:
sys.path.append(os.path.abspath('..'))


# -- Project information

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

project = 'Sphinx2Code'
copyright = f'2025 - {date.year}, PhilipPartsch'
author = 'PhilipPartsch'

release = '0.1'
version = '0.1.0'

# -- General configuration
on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.doctest',
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.test_reports',
    'sphinxcontrib.jquery', # https://github.com/sphinx-contrib/jquery
    'sphinx_preview',
]

templates_path = ['_templates']

exclude_patterns = ['_tools/*',]

# -- intersphinx

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']


# -- Sphinx-Preview

# The config for the preview features, which allows to "sneak" into a link.
# Docs: https://sphinx-preview.readthedocs.io/en/latest/#configuration
preview_config = {
    # Add a preview icon only for this type of links
    # This is very theme and HTML specific. In this case "div-mo-content" is the content area
    # and we handle all links there.
    "selector": "div.rst-content a",
    #"selector": "div.body a",
    # A list of selectors, where no preview icon shall be added, because it makes often no sense.
    # For instance the own ID of a need object, or the link on an image to open the image.
    #"not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a, a.paginate_button",
    "not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a, a.paginate_button, a.sd-btn",
    #"not_selector": "div.needs_head a, h1 a, h2 a",
    "set_icon": True,
    "icon_only": True,
    "icon_click": True,
    "icon": "🔎",
    #"icon": "icon:search",
    "width": 600,
    "height": 400,
    "offset": {
        "left": 0,
        "top": 0
    },
    "timeout": 0,
}

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_immaterial'
#html_theme = 'alabaster' # Sphinx Defaul Theme

# If we do perform a PDF build, we have to switch to alabaster
if os.environ.get("PDF", 0) == 1:
    html_theme = 'alabaster' # Sphinx Defaul Theme


#configure design according to sphinx_rtd_theme theme
if html_theme == 'sphinx_rtd_theme':
    preview_config["selector"] = "div.rst-content a"
    preview_config["not_selector"] = "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a, a.paginate_button, a.sd-btn"


#configure design according to sphinx_immaterial theme
if html_theme == 'sphinx_immaterial':
    extensions.append("sphinx_immaterial")

    preview_config["selector"] = "div.md-content a"
    preview_config["not_selector"] = "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a, a.paginate_button, a.sd-btn"

    html_theme_options = {
        "font": False,
        "icon": {
            "repo": "fontawesome/brands/github",
            "edit": "material/file-edit-outline",
        },
        "site_url": "https://philippartsch.github.io/Sphinx2Code",
        "repo_url": "https://github.dev/PhilipPartsch/Sphinx2Code",
        "repo_name": "Sphinx2Code",
        "edit_uri": "blob/main/docs",
        "globaltoc_collapse": True,
        "features": [
            "navigation.expand",
            # "navigation.tabs",
            # "toc.integrate",
            "navigation.sections",
            # "navigation.instant",
            # "header.autohide",
            "navigation.top",
            # "navigation.tracking",
            "search.highlight",
            "search.share",
            "toc.follow",
            "toc.sticky",
            "content.tabs.link",
            "announce.dismiss",
        ],
        "palette": [
            {
                "media": "(prefers-color-scheme: light)",
                "scheme": "default",
                "primary": "blue",
                "accent": "light-cyan",
            },
        ],
        "toc_title_is_page_title": True,
    }

html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'


# sphinxcontrib.plantuml configuration
local_plantuml_path = os.path.join(os.path.dirname(__file__), "_tools", "plantuml.jar")

if on_rtd:
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

print('plantuml path: ' + str(plantuml))

plantuml_output_format = 'svg'

# sphinx_needs configuration

# -- Sphinx-Needs

needs_from_toml = "ubproject.toml"

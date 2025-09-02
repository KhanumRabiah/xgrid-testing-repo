project = 'RstDoc Project'
author = project+' Xgrid Team'
copyright = '2025, '+author
version = '1.0'
release = '1.0.0'
try:
    #import sphinx_bootstrap_theme
    #html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
    html_theme = 'sphinx_rtd_theme'
except:
    pass
#these are enforced by rstdoc, but keep them for sphinx-build
numfig = 0
smartquotes = 0
source_suffix = '.rst'
templates_path = []
language = 'en'
#highlight_language = "none"
default_role = 'math'
pygments_style = 'sphinx'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'
#html_extra_path=['doc/_traceability_file.svg'] #relative to 
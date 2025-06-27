AUTHOR = 'Taniomi'
SITENAME = "Taniomi's Notebook"
SITEURL = "https://taniomi.github.io/taniomis_notebook"

PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("Pelican Themes", "https://pelicanthemes.com/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/taniomi"),
    ("LinkedIn", "https://linkedin.com/in/taniomi"),
)

DEFAULT_PAGINATION = 10

# Theme
THEME = "themes/blue-penguin-dark"
THEME_STATIC_DIR = 'static'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

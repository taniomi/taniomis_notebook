# ======================
# Basic site settings
# ======================
AUTHOR = 'Taniomi'
SITENAME = "Taniomi's Notebook"
SITEURL = "https://taniomi.github.io/taniomis_notebook"

# ======================
# Paths and i18n
# ======================
PATH = "content"
OUTPUT_PATH = "output/"
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

# ======================
# Theme and appearance
# ======================
# THEME = "themes/blue-penguin-dark"
THEME_STATIC_DIR = 'static'

# Theme-specific options
SITELOGO = 'images/taniomi_logo.png'  # or '' if not used
SITEDESCRIPTION = ''

DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME = True
DISPLAY_MENU = True
DARK_LIGHT_SWITCHING_OFF = True

MENU_INTERNAL_PAGES = (
    ('Tags', 'tags', 'tags/index.html'),
    ('Authors', 'authors', 'authors/index.html'),
    ('Categories', 'categories', 'categories/index.html'),
    ('Archives', 'archives', 'archives/index.html'),
)
MENUITEMS = (
    ('Home', '/'),
)

# Pagination URLs
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# ======================
# Feeds (disabled in dev)
# ======================
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ======================
# Blogroll and Social
# ======================
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("Pelican Themes", "https://pelicanthemes.com/"),
)
SOCIAL = (
    ("GitHub", "https://github.com/taniomi"),
    ("LinkedIn", "https://linkedin.com/in/taniomi"),
)

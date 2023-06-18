AUTHOR = 'Ashley'
SITENAME = 'Illemont'
SITEURL = 'https://ashuuuriii.github.io/illemont-quickref/'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extras', 'rules', 'items']

EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
}

THEME = 'themes/illemont-custom'
THEME_STATIC_DIR = "themes"
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'bootstrap.min.css'
# THEME = 'notmyidea'
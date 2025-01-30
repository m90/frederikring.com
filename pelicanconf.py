from datetime import datetime
from pelican_decorate_content import decorate_content

RELATIVE_URLS = False

AUTHOR = 'Frederik Ring'
PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# If your site is available via HTTPS, make sure SITEURL begins with https://
# This gets overridden on build
SITEURL = 'http://localhost:8080'

THEME = './theme'

# Delete the output directory before generating new files.
DELETE_OUTPUT_DIRECTORY = True
CACHE_CONTENT = True

# dont create following standard pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

PAGE_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = []
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['webassets', decorate_content]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}

DECORATE_CONTENT = {
    'h2': ['f4'],
    'h3': ['mb0', 'f5', 'dib'],
    'h3 > em': ['f6', 'normal'],
}

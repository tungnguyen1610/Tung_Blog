AUTHOR = 'Tung Nguyen'
SITENAME = 'Tung Nguyen'
SITEURL=''
PATH = 'content'
TIMEZONE = 'Asia/Ho_Chi_Minh'
DEFAULT_LANG = 'en'
IGNORE_FILES = ['digital_design/general_knowledge.md']
ARTICLE_PATHS = ['embedded_systems', 'digital_design', 'automotive','programming']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'md5'
GZIP_CACHE = False
CONTENT_CACHING_LAYER = 'generator'
WITH_FUTURE_DATES = False
THEME = 'themes/notmyidea'
THEME_TEMPLATES_OVERRIDES = ['templates']
STATIC_PATHS = ['images']
DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

SOCIAL = (
    ('<i class="fab fa-github"></i> GitHub', 'https://github.com/tungnguyen1610'),
    ('<i class="fab fa-linkedin"></i> LinkedIn', 'https://www.linkedin.com/in/tungbud/'),
    ('<i class="fas fa-envelope"></i> Email', 'mailto:nguyenhoangtung1610@gmail.com'),
)


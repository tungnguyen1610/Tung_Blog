AUTHOR = 'Tung Nguyen'
SITENAME = 'T_Blog'
SITEURL = 'https://tungnguyen1610.github.io/Tung_Blog/'

PATH = 'content'
TIMEZONE = 'Asia/Ho_Chi_Minh'
DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['embedded_systems', 'digital_design', 'automotive']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

THEME = 'notmyidea'
THEME_TEMPLATES_OVERRIDES = ['templates']
DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

SOCIAL = (
    ('GitHub', 'https://github.com/yourusername'),
    ('LinkedIn', 'https://www.linkedin.com/in/yourusername'),
    ('Facebook', 'https://www.facebook.com/yourusername'),
)
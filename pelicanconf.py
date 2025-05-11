AUTHOR = 'Tung Nguyen'
SITENAME = 'T_Blog'
SITEURL = 'https://tungnguyen1610.github.io/Tung_Blog/'
#SITEURL=''
PATH = 'content'
TIMEZONE = 'Asia/Ho_Chi_Minh'
DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['embedded_systems', 'digital_design', 'automotive','programming']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

THEME = 'notmyidea'
THEME_TEMPLATES_OVERRIDES = ['templates']
DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

SOCIAL = (
    ('<i class="fab fa-github"></i> GitHub', 'https://github.com/tungnguyen1610'),
    ('<i class="fab fa-linkedin"></i> LinkedIn', 'https://www.linkedin.com/in/tungbud/'),
    ('<i class="fas fa-envelope"></i> Email', 'mailto:nguyenhoangtung1610@gmail.com'),
)

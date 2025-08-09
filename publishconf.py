import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://tungnguyen1610.github.io/Tung_Blog'
RELATIVE_URLS = False  # important for production so paths are absolute
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
DELETE_OUTPUT_DIRECTORY = True

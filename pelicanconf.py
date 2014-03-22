#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

STATIC_PATHS = ['images', 'files']

AUTHOR = u'Justin Hardcastle'
SITENAME = u'I Made a Beer'
SITEURL = 'http://imadeabeer.com'

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = u'en'
THEME = '/home/ramma/imadeabeer.com/pelican-bootstrap3'
BOOTSTRAP_THEME = 'slate'

#MENUITEMS = 'About, Categories'

TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Beer Smith', 'http://beersmith.com/'),
          ('Beer Recipes', 'http://beerrecipes.org/'),
          ('American Homebrewers Association', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/imadeabeer'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#comments - disqus
DISQUS_DISPLAY_COUNTS = True
DISQUS_SITENAME = 'imadeabeer'

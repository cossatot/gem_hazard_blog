#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'GEM Hazard Team'
SITENAME = 'Global Earthquake Model Hazard blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
TWITTER_USERNAME = 'gem_hazard'

# Page structure
SHOW_ARCHIVES = True
ABOUT_PAGE = '/about/'
GAF_PAGE = '/global-active-fault-viewer/'

# static page formatting
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# blog page formatting
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'


# plugin stuff
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_dynamic']

# static paths
STATIC_PATHS = ['images',
                #'html'
                ]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# THEME STUFF
THEME = 'themes/middle'


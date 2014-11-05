#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'iv-maksimov'
SITENAME = 'foo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Specify theme

THEME = r"c:\site\pelican-blog\theme"
BOOTSTRAP_THEME = "material"

STATIC_PATHS = ['images', 'pages',]
PLUGIN_PATHS = [r'c:\site\pelican-blog\plugins',]
PLUGINS = ['liquid_tags.notebook', 'liquid_tags.img']

GOOGLE_ANALYTICS = 'UA-55193702-1'

DISQUS_SITENAME = 'ivmaksimov'
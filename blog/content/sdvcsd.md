Title: python
Date: 2014-12-03 10:20
Category: blog
Tags: matplotlib, publishing
Author: Ivan Maksimov
Lang: en

##Matplotlib!!!dv
dfvds
 1. 1-й элемент нумерованного списка
 2. 2-й элемент нумерованного списка
 3. туда сюда


 * элемент маркированного списка
 * элемент маркированного списка

sdfv


{% notebook c:\site\pelican-blog\blog\content\images\Untitled1.ipynb %}

[![banner](images/1.JPG)](#)

{% img [class name(s)] images/2.JPG [200 [100]] [title text | "title text" ["alt text"]] %}



A block of text.

    :::python
    def register():
    """Plugin registration."""
    if webassets:
        signals.initialized.connect(add_jinja2_ext)
        signals.generator_init.connect(create_assets_env)
    else:
        logger.warning('`assets` failed to load dependency `webassets`.'
                       '`assets` plugin not loaded.')

test

	:::python
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

test
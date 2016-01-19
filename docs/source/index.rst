.. Grabfeed documentation master file, created by
   sphinx-quickstart on Tue Jan 19 09:26:38 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Grabfeed's documentation!
====================================
Python package to detect and return RSS feeds for a given website. It has been tested with major blogging platforms.

	1. You enter a URL.
	2. Grabfeed detects and returns RSS feed URL for the website.

Getting Started with Grabfeed
-------------------------------

Install it with pip::

	pip install grabfeed


Sample Code:
--------------

An example code to run Grabfeed and return RSS feed::

	from grabfeed.grabber import return_rss
	rss_feed = return_rss('http://techcrunch.com')
	print(rss_feed)
	# output: http://techcrunch.com/feed/


Tested platforms:
-------------------

  - Wordpress, Blogger, Tumblr, Ghost, Svbtle and Medium
  - Works with most of the blogs on the web even though they are not be built with above platforms.
  - Support for:
  	* Python 2.6
  	* Python 2.7
  	* Python 3.2
  	* Python 3.3
  	* Python3.4
  	* And even Pypy!
  - 100% test coverage
GrabFeed
========

[![Build Status](https://travis-ci.org/kaflesudip/grabfeed.svg?branch=master)](https://travis-ci.org/kaflesudip/grabfeed)
[![PyPI version](https://badge.fury.io/py/grabfeed.svg)](https://badge.fury.io/py/grabfeed)
[![PyPI Downloads](https://img.shields.io/pypi/dm/grabfeed.svg)](https://pypi.python.org/pypi/grabfeed)


Python package to detect and return RSS feeds for a given website. It has been tested with major blogging platforms.

1. You enter a URL.
2. Grafeed detects and returns RSS feed URL for the website.

Installation
============
    pip install grabfeed

Example Code
============

### Return RSS feed

```python
from grabfeed.grabber import return_rss
rss_feed = return_rss('http://techcrunch.com')
print(rss_feed)
```

Tested platforms:
=================
  - Wordpress, Blogger, Tumblr, Ghost, Svbtle and Medium
  - Works with most of the blogs on the web even though they are not be built with above platforms.
  - Supports Python 2.6, 2.7, 3.2, 3.3, 3.4 and pypy
 

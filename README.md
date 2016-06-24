GrabFeed
========

[![Build Status](https://travis-ci.org/kaflesudip/grabfeed.svg?branch=master)](https://travis-ci.org/kaflesudip/grabfeed)
[![Coverage Status](https://coveralls.io/repos/kaflesudip/grabfeed/badge.svg?branch=master&service=github)](https://coveralls.io/github/kaflesudip/grabfeed?branch=master)
[![PyPI version](https://badge.fury.io/py/grabfeed.svg)](https://badge.fury.io/py/grabfeed)
[![PyPI Downloads](https://img.shields.io/pypi/dm/grabfeed.svg)](https://pypi.python.org/pypi/grabfeed)
[![PyPI Downloads](https://readthedocs.org/projects/grabfeed/badge/?version=latest)](http://grabfeed.readthedocs.org/en/latest/)
[![Requirements Status](https://requires.io/github/kaflesudip/grabfeed/requirements.svg?branch=master)](https://requires.io/github/kaflesudip/grabfeed/requirements/?branch=master)



Python package to detect and return RSS feeds for a given website. It has been tested with major blogging platforms.

1. You enter a URL.
2. Grabfeed detects and returns RSS feed URL for the website.

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
# output: http://techcrunch.com/feed/
```

Tested platforms:
=================
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
 

GrabFeed
========

Python package to detect and return RSS / Atom feeds for a given website. It has been tested with major blogging platforms.

1. You enter a URL.
2. Grabfeed detects and returns RSS / Atom feed URL for the website.

Installation
============
    pip install grabfeed

Example Code
============

### Return RSS feed

```python
from grabfeed.grabber import return_feed
feed = return_feed('http://techcrunch.com')
print(feed.rss)
# output: http://techcrunch.com/feed/
```

### Return Atom feed

```python
from grabfeed.grabber import return_feed
feed = return_feed('https://google.blogspot.com/')
print(feed.atom)
# output: https://google.blogspot.com/feeds/posts/default
```

Tested platforms:
=================
  - Wordpress, Blogger, Tumblr, Ghost, Svbtle and Medium
  - Works with most of the blogs on the web even though they are not be built with above platforms.
  - Support for:
    * Python 2.7
    * Python 3.3
    * Python 3.4
    * Python 3.5
    * Python 3.6
  - 100% test coverage
 

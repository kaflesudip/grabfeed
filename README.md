GrabFeed
========

Python package to detect and return RSS feeds for a given website. It has been tested with major blogging platforms.

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

### Return RSS content

```python
from grabfeed.grabber import return_page_content
page_content= return_page_content('http://techcrunch.com')
print(page_content)
```

Tested platforms:
=================
  - Wordpress, Blogger, Tumblr, Ghost, Svbtle and Medium
  - Works with most of the blogs on the web even though they are not be built with above platforms.
 

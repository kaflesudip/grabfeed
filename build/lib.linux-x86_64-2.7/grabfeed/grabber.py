import requests
from bs4 import BeautifulSoup
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
import traceback


def return_page_content(page_url):
    # Use haders to avoid being blocked
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11'
        ' (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'
        ',*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    try:
        req = requests.get(page_url, headers=hdr)
        return req.text
    except Exception as err:
        traceback.print_tb(err.__traceback__)


def return_rss(page_url):
    # inpired from quora post: bit.ly/1jGKdMY
    page_content = return_page_content(page_url)
    rss_link = ''
    try:
        soup = BeautifulSoup(page_content, "html.parser")
        link = soup.find('link', type='application/rss+xml')
        rss_link = link['href']
    except Exception as err:
        traceback.print_tb(err.__traceback__)
    if not rss_link:
        raise Exception("The page has no RSS feed")
    # some website return absolute url while some have relative.
    if not urlparse(rss_link).netloc:
        if page_url not in rss_link:
            domain_parse = urlparse(
                '{0}'.format(page_url)
            )
            complete_domain = '{0}://{1}'.format(
                domain_parse.scheme, domain_parse.netloc
            )
            rss_link = (
                '{0}{1}'.format(complete_domain, rss_link)
            )
        else:
            rss_link = (
                '{0}{1}'.format('http://', rss_link)
            )
    return rss_link

import urllib2
from BeautifulSoup import BeautifulSoup
import urlparse


def return_rss(page_url):

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
    req = urllib2.Request(page_url, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    link = soup.find('link', type='application/rss+xml')
    rss_link = link['href']

    # some website return absolute url while some have relative.
    if not urlparse.urlparse(rss_link).netloc:
        if not page_url in rss_link:
            domain_parse = urlparse.urlparse(
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


def test():
    blog_list = [
        'http://joel.is',
        'http://cricketcurrent.blogspot.com',
        'http://technott.com',  # wordpress with cloudflare
        'http://labnol.org',  # wordpress normal
        'http://blog.kissmetrics.com',  # wordpress
        'http://blog.bufferapp.com',  # wordpress with some security
        'http://blog.audeet.com',  # ghost blog
        'http://manojghimire.com/',  # svbtle blog
        'https://medium.com/@felixsalmon',  # medium with relative
        'http://technott.com/2014/02/'
        'google-online-interactive-learning-tool-oppia/',  # wordpress relative
        'http://lifehacker.com',  # custom blog
    ]
    for item in blog_list:
        try:
            print(return_rss(item))
        except:
            print('could not find for {0}'.format(item))

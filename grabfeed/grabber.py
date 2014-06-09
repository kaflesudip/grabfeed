import urllib2
from BeautifulSoup import BeautifulSoup
import urlparse
import xmltodict


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
        req = urllib2.Request(page_url, headers=hdr)
        page = urllib2.urlopen(req)
        return page
    except:
        return ''


def return_rss(page_url):
    # inpired from quora post: bit.ly/1jGKdMY
    page_content = return_page_content(page_url)
    if page_content == '':
        return ''
    soup = BeautifulSoup(page_content)
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


def return_content(page_url, return_type='dict'):
    rss_page_url = return_rss(page_url)
    page_content = return_page_content(rss_page_url).read()
    if return_type == 'xml':
        return page_content
    else:
        content = xmltodict.parse(page_content)
        return content

print return_content('http://blog.flipkarma.com')

import requests
from bs4 import BeautifulSoup


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
        req = requests.get(
            page_url, headers=hdr)
        return req.text
    except:
        raise


def return_rss(page_url):
    # inpired from quora post: bit.ly/1jGKdMY
    page_content = return_page_content(page_url)
    rss_link = ''
    soup = BeautifulSoup(page_content, "html.parser")
    link = soup.find('link', type='application/rss+xml')
    if not link:
        link = soup.find('link',type='application/atom+xml')
        
    if not link:
        raise Exception("The page has no RSS feed")
    rss_link = link.get('href')
    return rss_link

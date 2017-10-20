import requests
from bs4 import BeautifulSoup

class Grabfeed:
    rss = None
    atom = None

    def __init__(self, rss, atom):
        self.rss = rss
        self.atom = atom

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
    rss_link = return_feed(page_url).rss
    if not rss_link:
        raise Exception("The page has no RSS feed")
    return rss_link

def return_atom(page_url):
    atom_link = return_feed(page_url).atom
    if not atom_link:
        raise Exception("The page has no Atom feed")
    return atom_link


def return_feed(page_url):
    page_content = return_page_content(page_url)
    atom_link = ''
    soup = BeautifulSoup(page_content, "html.parser")
    atom_link = soup.find('link',type='application/atom+xml')
        
    if not atom_link:
        atom_link = False
    else:
        atom_link = atom_link.get('href')
    rss_link = soup.find('link', type='application/rss+xml')        
    if not rss_link:
        rss_link = False
    else:
        rss_link = rss_link.get('href')
    return Grabfeed(rss=rss_link, atom=atom_link)

import urllib.request
from bs4 import BeautifulSoup, SoupStrainer

url_for_event = 'http://content.warframe.com/dynamic/rss.php'


def get_events():
    """[summary]

    Returns:
        [type]: [description]
    """
    value = ''
    remote_data = urllib.request.urlopen(url_for_event).read()
    parse_only = SoupStrainer('item')
    soup = BeautifulSoup(remote_data, "html.parser", parse_only=parse_only)
    for item in soup.children:
        value += item.title.text + '\n'
    return value

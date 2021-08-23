import datetime
import urllib.request
from bs4 import BeautifulSoup

url_for_baro = 'http://warframe.wikia.com/wiki/Baro_Ki%27Teer'
now_time = datetime.datetime.now()


def url_read():
    """
    Get html request
    """
    remote_data = urllib.request.urlopen(url_for_baro).read()
    return BeautifulSoup(remote_data, "html.parser")


def baroKi(timezone):
    """
    Bild message
    """
    body_url = url_read().find('span', {'class': 'countdown'})
    delta = datetime.timedelta(hours=timezone)
    countdowndate = body_url.span.text[:-5]
    countdowndate = datetime.datetime.strptime(countdowndate, "%B %d %Y %H:%M:%S")
    return str(countdowndate - now_time + delta)[:-7]

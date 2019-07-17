# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import sys

if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')


def polls():
    base = 'https://www.realclearpolitics.com'
    response = urlopen('%s/epolls/latest_polls/' % base)
    soup = BeautifulSoup(response, 'html.parser')
    fp = soup.find_all("table", {"class": 'sortable'})
    polling_data = []
    for l in fp:
        cols = l.find_all('tr')
        for col in cols:
            race = col.find('td', {'class': 'lp-race'})
            if not race:
                continue
            d = {
                'url': base + race.find('a')['href'],
                'title': race.find('a').text,
                'poll': col.find('td', {'class': 'lp-poll'}).find('a').text,
            }
            polling_data.append(d)

    return polling_data


def poll_data(pd):
    response = urlopen(pd)
    soup = BeautifulSoup(response, 'html.parser')
    fp = soup.find("div", {"id": 'polling-data-full'})
    if not fp:
        return
    rows = fp.find('table', {"class": 'data'})
    p = []
    for row in rows:
        cols = row.find_all(['th', 'td'])
        p.append([ele.text.strip() for ele in cols])
    return p


if __name__ == '__main__':
    d = polls()
    for p in d:
        print(p['url'], p['title'], p['poll'])

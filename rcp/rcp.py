# -*- coding: utf-8 -*-

import csv
from typing import List, Dict, Union, Any

import urllib3
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

base = "https://www.realclearpolitics.com"

ua = UserAgent()


def _html(url: str) -> BeautifulSoup:
    """
    Get the poll HTML.
    :param url: The url of the poll.
    :return: BeautifulSoup
    """
    with urllib3.PoolManager() as manager:
        res = manager.request("GET", url, headers={"User-Agent": ua.chrome})
        if res.status != 200:
            raise Exception(res.status)
        soup = BeautifulSoup(res.data, "html.parser")
        return soup


def create_table(p: list, html_format: bool = False) -> str:
    """
    Generate poll table.
    :param p: The poll data.
    :param html_format: Set to True to return HTML table.
    :return: str
    """
    from prettytable import PrettyTable

    x = PrettyTable()
    x.field_names = list(p[0]["data"][0].keys())
    x.align = "l"
    for row in p[0]["data"]:
        x.add_row(row.values())
    return x.get_html_string() if html_format else x


def get_polls(
    url: str = "%s/epolls/latest_polls/" % base,
    candidate: str = None,
    pollster: str = None,
    state: str = None,
) -> List[Dict[str, Union[str, Any]]]:
    """
    :param state: The state to get polling data for.
    :param url: The URL of the polls. By default this function will search the latest polls on RCP.
    :param candidate: The election candidate.
    :param pollster: The pollster, i.e. Fox, CNN, Politico, etc.
    :return: arr
    """
    soup = _html(url)

    fp = soup.find_all("div", {"class": "table-races"})

    polling_data = []

    for l in fp:
        cols = l.find_all("tr")
        for col in cols:
            race = col.find("td", {"class": "lp-race"})
            result = col.find("td", {"class": "lp-results"})
            spread = col.find("td", {"class": "lp-spread"})

            if not race:
                continue

            t = race.find("a").text
            n = col.find("td", {"class": "lp-poll"}).find("a").text

            if (
                (candidate and candidate.lower() not in t.lower())
                or (pollster and pollster.lower() not in n.lower())
                or (state and state.lower() not in t.lower())
            ):
                continue

            v = {
                "url": base + race.find("a")["href"],
                "title": t,
                "poll": n,
                "result": result.text,
                "spread": spread.text,
            }
            polling_data.append(v)

    return polling_data


def get_poll_data(poll: str, csv_output: bool = False) -> list:
    """
    :param poll: The URL of the poll.
    :param csv_output: Set to True to return a table like data structure if writing to CSV.
    :return: arr
    """
    if base not in poll:
        return []

    soup = _html(poll)
    fp = soup.find("div", {"id": "polling-data-full"})

    if not fp:
        return []

    rows = fp.find("table", {"class": "data"})

    p = []

    for row in rows:
        cols = row.find_all(["th", "td"])
        tmp = []
        for ele in cols:
            if ele.find("a", {"class": "normal_pollster_name"}):
                tmp.append(
                    ele.find("a", {"class": "normal_pollster_name"}).text.strip()
                )
            else:
                tmp.append(ele.text.strip())
        p.append(tmp)

    if csv_output:
        return p

    arr = [{"poll": poll, "data": []}]

    keys = p[0]

    for k in p[1:]:
        b = {}
        for i, n in enumerate(keys):
            b[n] = k[i]
        arr[0]["data"].append(b)

    return arr


def to_csv(filename: str, poll_data: list):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(poll_data)
    print("CSV created.")

from bs4 import BeautifulSoup
import csv
import argparse

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def main():
    response = urlopen(args.url)

    soup = BeautifulSoup(response, 'html.parser')

    fp = soup.find("div", {"id": 'polling-data-full'})
    rows = fp.find('table', {"class": 'data'})

    p = []
    for row in rows:
        cols = row.find_all(['th', 'td'])
        p.append([ele.text.strip() for ele in cols])

    with open(args.output, "w") as f:
        writer = csv.writer(f)
        writer.writerows(p)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The url of the polling data.")
    parser.add_argument('-o', "--output", nargs="?", help="The output file name. Defaults to output.csv", default="output.csv")
    args = parser.parse_args()
    main()

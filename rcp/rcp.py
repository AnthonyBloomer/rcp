from bs4 import BeautifulSoup
import csv
import argparse

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

parser = argparse.ArgumentParser()
parser.add_argument("url", nargs='+', help="The url of the polling data.")
parser.add_argument("--output", nargs="?", help="The output file name.")
args = parser.parse_args()

def main():
    for pd in args.url:
        response = urlopen(pd)
        soup = BeautifulSoup(response, 'html.parser')
        fp = soup.find("div", {"id": 'polling-data-full'})
        rows = fp.find('table', {"class": 'data'})
        p = []
        for row in rows:
            cols = row.find_all(['th', 'td'])
            p.append([ele.text.encode('utf-8').strip() for ele in cols])
        
        fn = args.output if args.output else pd.rsplit('/', 1)[-1][:-5] + ".csv"
        
        print("Downloading: %s" % fn)
        
        with open(fn, "w") as f:
            writer = csv.writer(f)
            writer.writerows(p)


if __name__ == '__main__':
    main()

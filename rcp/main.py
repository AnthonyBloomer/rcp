# -*- coding: utf-8 -*-

import csv
import argparse
import sys
from .rcp import get_poll_data

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
        fn = args.output if args.output else pd.rsplit('/', 1)[-1][:-5] + ".csv"
        p = get_poll_data(pd)
        if not p:
            sys.exit("No poll data found.")
        print("Downloading: %s" % fn)
        with open(fn, "w") as f:
            writer = csv.writer(f)
            writer.writerows(p)


if __name__ == '__main__':
    main()

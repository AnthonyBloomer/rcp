# -*- coding: utf-8 -*-

import argparse
import sys

from .rcp import get_poll_data, to_csv, create_table

parser = argparse.ArgumentParser()
parser.add_argument("url", nargs="+", help="The url of the polling data.")
parser.add_argument("--output", nargs="?", help="The output file name.")
parser.add_argument(
    "--generate-table",
    help="Pass this argument to generate a table.",
    dest="table",
    action="store_true",
)
args = parser.parse_args()


def generate_filename(url: str):
    return args.output if args.output else url.rsplit("/", 1)[-1][:-5] + ".csv"


def main():
    if args.table:
        x = get_poll_data(args.url[0])
        print(create_table(x))
        sys.exit(0)
    for url in args.url:
        filename = generate_filename(url)
        poll_data = get_poll_data(url, csv_output=True)
        if not poll_data:
            sys.exit("No poll data found.")
        print("Downloading: %s" % filename)
        to_csv(filename, poll_data)


if __name__ == "__main__":
    main()

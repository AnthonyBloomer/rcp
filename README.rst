rcp
===

Simple script to scrape polling data from RealClearPolitics and output
as .csv.

Install
^^^^^^^

::

    pip install realclearpolitics

Usage
^^^^^

::

    usage: rcp [-h] [--output [OUTPUT]] url [url ...]

    positional arguments:
      url                The url of the polling data.

    optional arguments:
      -h, --help         show this help message and exit
      --output [OUTPUT]  The output file name.


Examples
^^^^^^^^

Get the US general election results.

::

    rcp http://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html --output general.csv

Download multiple polls.

::  

    rcp http://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html \
    > https://www.realclearpolitics.com/epolls/other/president_trump_job_approval_economy-6182.html \
    > https://www.realclearpolitics.com/epolls/other/president_trump_job_approval_foreign_policy-6183.html




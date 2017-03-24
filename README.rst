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

    usage: rcp [-h] [-o [OUTPUT]] url

    positional arguments:
      url                   The url of the polling data.

    optional arguments:
      -h, --help            show this help message and exit
      -o [OUTPUT], --output [OUTPUT]
                            The output file name. Defaults to output.csv


Example
^^^^^^^

::

    python -m rcp http://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html --output general.csv



rcp
===

Python client for RealClearPolitics. 

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

API Usage
^^^^^^^^^

Search for Fox News poll numbers for Trump:

.. code-block:: python

    from rcp import get_polls, get_poll_data
    from pprint import pprint

    polls = get_polls(q="Trump", p="Fox")

    for poll in polls:
        td = get_poll_data(poll['url'])
        pprint(td)

The will return a dictionary structured like this:

.. code-block::


    [
        {
            'data': [{'Biden (D)': '49.6',
                    'Date': '3/27 - 7/9',
                    'MoE': '--',
                    'Poll': 'RCP Average',
                    'Sample': '--',
                    'Spread': 'Biden +8.5',
                    'Trump (R)': '41.1'},
            ...
            }],
        'poll': 'https://www.realclearpolitics.com/epolls/2020/president/us/general_election_trump_vs_biden-6247.html'

    ]

Write a poll to CSV:

.. code-block:: python

    from rcp import get_polls, get_poll_data, to_csv

    polls = get_polls(q="Biden")[0]
    data = get_poll_data(polls['url'])
    to_csv('output.csv', data)


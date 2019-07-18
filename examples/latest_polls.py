from rcp.rcp import get_polls, get_poll_data
from pprint import pprint

polls = get_polls(q="Trump", p="Fox")
for poll in polls:
    td = get_poll_data(poll['url'], json=True)
    pprint(td)

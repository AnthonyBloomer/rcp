from rcp import get_polls, get_poll_data
from pprint import pprint

polls = get_polls(candidate="Trump", pollster="Fox")
for poll in polls:
    td = get_poll_data(poll["url"])
    pprint(td)

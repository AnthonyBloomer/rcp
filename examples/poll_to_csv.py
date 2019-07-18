from rcp import get_polls, get_poll_data, to_csv

polls = get_polls(q="Biden")[0]
data = get_poll_data(polls['url'])
to_csv('output.csv', data)

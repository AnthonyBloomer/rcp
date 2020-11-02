from rcp import get_polls, get_poll_data, to_csv

polls = get_polls(candidate="Biden")[0]
data = get_poll_data(polls["url"], csv_output=True)
to_csv("output.csv", data)

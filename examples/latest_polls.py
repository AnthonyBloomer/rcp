from rcp.rcp import get_polls, get_poll_data

polls = get_polls(q="Trump", p="Rasmussen")
for poll in polls:
    td = get_poll_data(poll['url'], json=True)
    for data in td[0]['data']:
        print(data)

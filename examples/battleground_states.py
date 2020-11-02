from rcp import get_polls

battleground_states = [
    "Wisconsin",
    "Florida",
    "Michigan",
    "Pennsylvania",
    "North Carolina",
    "Arizona",
]

for state in battleground_states:
    polls = get_polls(candidate="Trump", state=state)
    for poll in polls:
        print(poll)

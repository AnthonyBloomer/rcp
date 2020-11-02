from rcp import get_poll_data, create_table

td = get_poll_data(
    "https://www.realclearpolitics.com/epolls/2020/president/me/maine_trump_vs_biden-6922.html"
)

print(create_table(td, html_format=True))

import os
import unittest

from rcp import get_poll_data, get_polls, to_csv, create_table


class RCPTest(unittest.TestCase):
    def test_get_polling_data(self):
        p = get_polls()
        polling_data = get_poll_data(p[0]["url"], csv_output=True)
        self.assertIsNotNone(polling_data)
        self.assertIn("Poll", polling_data[0])
        self.assertIn("Date", polling_data[0])

    def test_get_polling_data_by_name(self):
        polls = get_polls(candidate="trump")
        first = polls[0]
        for p in polls:
            self.assertIn("trump", p["title"].lower())
        td = get_poll_data(first["url"])
        self.assertIsNotNone(td)

    def test_to_csv(self):
        csv_file = "output.csv"
        success = False
        polls = get_polls(candidate="Biden")[0]
        data = get_poll_data(polls["url"], csv_output=True)
        to_csv("output.csv", data)
        cur_dir = os.getcwd()
        file_list = os.listdir(cur_dir)
        if csv_file in file_list:
            success = True
            os.remove(csv_file)
        self.assertTrue(success)

    def test_get_polling_data_by_poll(self):
        polls = get_polls(pollster="cnn")
        for p in polls:
            self.assertIn("cnn", p["poll"].lower())

    def test_get_polling_data_by_invalid_poll(self):
        polls = get_polls(pollster="wow")
        self.assertEqual(len(polls), 0)

    def test_get_polling_data_invalid_url(self):
        polling_data = get_poll_data("https://www.rcp.com")
        self.assertFalse(polling_data)

    def test_create_table(self):
        td = get_poll_data(
            "https://www.realclearpolitics.com/epolls/2020/president/me/maine_trump_vs_biden-6922.html"
        )

        self.assertIsNotNone(create_table(td, html_format=True))

    def test_write_to_csv(self):
        poll = "https://www.realclearpolitics.com/epolls/other/president_trump_job_approval_foreign_policy-6183.html"
        csv_file = "president_trump_job_approval_foreign_policy-6183.csv"
        cmd = os.system("python -m rcp %s" % poll)
        self.assertEqual(cmd, 0)
        success = False
        cur_dir = os.getcwd()
        file_list = os.listdir(cur_dir)
        if csv_file in file_list:
            success = True
            os.remove(csv_file)
        self.assertTrue(success)

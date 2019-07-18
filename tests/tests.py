import unittest

from rcp.rcp import get_poll_data, get_polls
import os


class RCPTest(unittest.TestCase):

    def test_get_polling_data(self):
        p = get_polls()
        polling_data = get_poll_data(p[0]['url'], json=True)
        self.assertIsNotNone(polling_data)
        self.assertIn('poll', polling_data[0])
        self.assertIn('data', polling_data[0])

    def test_get_polling_data_by_name(self):
        polls = get_polls(q='trump')
        for p in polls:
            self.assertIn('trump', p['title'].lower())

    def test_get_polling_data_by_poll(self):
        polls = get_polls(p='cnn')
        for p in polls:
            self.assertIn('cnn', p['poll'].lower())

    def test_get_polling_data_by_invalid_poll(self):
        polls = get_polls(p='wow')
        self.assertEqual(len(polls), 0)

    def test_get_polling_data_invalid_url(self):
        polling_data = get_poll_data('https://www.realclearpolitics.com')
        print(polling_data)
        self.assertIsNone(polling_data)

    def test_write_to_csv(self):
        poll = "https://www.realclearpolitics.com/epolls/other/president_trump_job_approval_foreign_policy-6183.html"
        csv_file = "president_trump_job_approval_foreign_policy-6183.csv"
        cmd = os.system("python -m rcp %s" % poll)
        self.assertEqual(cmd, 0)
        success = False
        cur_dir = os.getcwd()
        file_list = os.listdir(cur_dir)
        for f in file_list:
            if csv_file in f:
                success = True
                os.remove(f)
        self.assertTrue(success)

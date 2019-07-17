import unittest

from rcp.rcp import poll_data, polls


class RCPTest(unittest.TestCase):

    def test_get_polling_data(self):
        p = polls()
        polling_data = poll_data(p[0]['url'])
        print(polling_data)
        self.assertIsNotNone(polling_data)

    def test_get_polling_data_invalid_url(self):
        polling_data = poll_data('https://www.realclearpolitics.com')
        print(polling_data)
        self.assertIsNone(polling_data)

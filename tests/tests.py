import unittest

from rcp.rcp import poll_data_as_json, get_polls


class RCPTest(unittest.TestCase):

    def test_get_polling_data(self):
        p = get_polls()
        polling_data = poll_data_as_json(p[0]['url'])
        print(polling_data)
        self.assertIsNotNone(polling_data)

    def test_get_polling_data_invalid_url(self):
        polling_data = poll_data_as_json('https://www.realclearpolitics.com')
        print(polling_data)
        self.assertIsNone(polling_data)

import unittest
from unittest import mock

from finpy import yahoo as yh

class TestStocksClient(unittest.TestCase):
    def setUp(self):
        req_path = 'finpy.yahoo.market.requests.Session.get'
        self.mock_get_patcher = mock.patch(req_path)
        self.mock_get = self.mock_get_patcher.start()
        self.mock_get.return_value.text = r'{"some":"json"}'

        mock_key = '0000000000'
        self.client = yh.market.Client(mock_key)

    def test_get_mutual_funds(self):
        """ test that a valid mutual funds request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_mutual_funds('MSFT')
        self.assertEqual(data, expected)

    def test_get_top_gainers(self):
        """ test that a valid top gainers request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_top_gainers('MSFT')
        self.assertEqual(data, expected)

    def test_get_most_watched(self):
        """ test that a valid most watched request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_most_watched('MSFT')
        self.assertEqual(data, expected)

    def test_get_news(self):
        """ test that a valid news request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_news('MSFT')
        self.assertEqual(data, expected)

    def test_get_quotes(self):
        """ test that a valid quotes request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_quotes('MSFT')
        self.assertEqual(data, expected)

    def test_get_etfs(self):
        """ test that a valid etfs request will
        return data. """

        expected = self.mock_get.return_value.text
        data = self.client.get_mutual_funds('MSFT')
        self.assertEqual(data, expected)
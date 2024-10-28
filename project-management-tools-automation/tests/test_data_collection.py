# Tests for data collection script

import unittest
from automation.data_collection import fetch_jira_data, fetch_trello_data

class TestDataCollection(unittest.TestCase):

    def test_fetch_jira_data(self):
        data = fetch_jira_data()
        self.assertIsInstance(data, dict)
        self.assertIn('issues', data)

    def test_fetch_trello_data(self):
        data = fetch_trello_data('your_board_id')
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()

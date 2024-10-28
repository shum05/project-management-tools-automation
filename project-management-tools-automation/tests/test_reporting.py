# Tests for reporting script

import unittest
from automation.reporting import load_data, process_data

class TestReporting(unittest.TestCase):

    def test_load_data(self):
        data = load_data()
        self.assertIn('jira', data)
        self.assertIn('trello', data)

    def test_process_data(self):
        data = load_data()
        jira_df, trello_df = process_data(data)
        self.assertGreater(len(jira_df), 0)
        self.assertGreater(len(trello_df), 0)

if __name__ == '__main__':
    unittest.main()

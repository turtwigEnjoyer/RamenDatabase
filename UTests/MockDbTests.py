from distutils.core import setup

from Database import MockDatabase
from Database import MockData
import unittest

class MockDbTests(unittest.TestCase):
    """
    Checks MockDatabase can be created and loaded with new mock data.
    """
    def setUp(self):
        mock_data = MockData.MockData()
        self.MockDatabase = MockDatabase.MockDatabase( mock_data.RamenList)
        assert self.MockDatabase.ramen_list

    def testSimpleQuery(self):
        self.setUp()

        query_results = self.MockDatabase.simple_query(field= "Country", value="Spain")

        assert len(query_results) == 2


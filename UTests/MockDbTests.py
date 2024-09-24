from UTests import MockData, MockDatabase
from Entities import Ramen
import unittest

class MockDbTests(unittest.TestCase):
    """
    Checks MockDatabase can be created and loaded with new mock data.
    """
    def setUp(self):
        mock_data = MockData.MockData()
        self.MockDatabase = MockDatabase.MockDatabase(mock_data.RamenList)
        assert self.MockDatabase.ramen_list

    """ Test we can query by generic fields """
    def testSimpleQuery(self):
        self.setUp()

        query_results = self.MockDatabase.SimpleQuery(field="Country", value="Spain")

        assert len(query_results) == 2

    def testInsert(self):
        self.setUp()

        self.MockDatabase.insert( Ramen.Ramen( _id = 1,
                         brand = "Yatekomo",
                         variety = "a",
                         style = "Chicken",
                         stars = 5,
                         country = "Spain",
                         top_ten = "1") )

        assert len(self.MockDatabase.ramen_list) == 3
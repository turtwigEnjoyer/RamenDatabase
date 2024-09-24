import unittest

from Firebase import DbInterface
from Firebase.PrettyPrinter import PrettyPrinter
from Firebase.QueryFilter import QueryFilter

class DbInterfaceTests(unittest.TestCase):
    def setUp(self):
        self.db = DbInterface.DbInterface()
        self.printer = PrettyPrinter()
    """Test to assert simple queries work on all symbols and mapping is correct"""
    def testSimpleQuery(self):
        #Test equality
        filter1 = QueryFilter(
            field= "country",
            comparer= "==",
            value= "Japan"
        )
        result = self.db.SimpleQuery(filter1)
        self.printer.print(result)
        assert len(result) != 0
import unittest

from Firebase import DbInterface
from Firebase.PrettyPrinter import PrettyPrinter
from Firebase.QueryFilter import QueryFilter

class DbInterfaceTests(unittest.TestCase):
    db = DbInterface.DbInterface()

    def setUp(self):
        self.printer = PrettyPrinter()

    """Test to assert simple queries are sent and received on all symbols and class mapping is correct"""
    def testEqualitySimpleQuery(self):
        #Test equality
        filter1 = QueryFilter(
            field= "country",
            comparer= "==",
            value= "Japan"
        )
        result = self.db.Query([filter1])
        #self.printer.print(result)
        assert len(result) != 0

    def testGreaterOrEqualSimpleQuery(self):
        #Test equality
        filter1 = QueryFilter(
            field= "stars",
            comparer= ">=",
            value= 5
        )
        result = self.db.Query([filter1])
        #self.printer.print(result)
        assert len(result) != 0

    def testCompoundQueries(self):
        filter1 = QueryFilter(
            field="stars",
            comparer=">=",
            value=5
        )
        filter2 = QueryFilter(
            field="style",
            comparer="==",
            value="Cup"
        )
        result = self.db.Query([filter1, filter2])
        self.printer.print(result)
        assert len(result) != 0
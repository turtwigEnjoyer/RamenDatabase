import unittest
from distutils.core import setup

from Firebase import Ramen
from Firebase import PrettyPrinter


class PrettyPrinterTests(unittest.TestCase):
    def setUp(self):
        self.testData = [
            Ramen.Ramen(Id=1,
                        Brand="Yatekomo",
                        Variety="a",
                        Style="Chicken",
                        Stars=5,
                        Country="Spain",
                        TopTen=True),
            Ramen.Ramen(Id=2,
                        Brand="Yatekomo",
                        Variety="b",
                        Style="Beef And Egg",
                        Stars=4,
                        Country="Spain")
        ]
    def testPrinter(self):
        self.setUp()
        printer = PrettyPrinter.PrettyPrinter()

        printer.print(self.testData)




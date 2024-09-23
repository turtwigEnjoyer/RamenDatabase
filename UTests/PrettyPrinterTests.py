import unittest
from distutils.core import setup

from Firebase import Ramen
from Firebase import PrettyPrinter


class PrettyPrinterTests(unittest.TestCase):
    def setUp(self):
        self.testData = [
            Ramen.Ramen(_id=1,
                        brand="Yatekomo",
                        variety="a",
                        style="Chicken",
                        stars=5,
                        country="Spain",
                        top_ten="1"),
            Ramen.Ramen(_id=2,
                        brand="Yatekomo",
                        variety="b",
                        style="Beef And Egg",
                        stars=4,
                        country="Spain",
                        top_ten="2")
        ]
    def testPrinter(self):
        self.setUp()
        printer = PrettyPrinter.PrettyPrinter()

        printer.print(self.testData)




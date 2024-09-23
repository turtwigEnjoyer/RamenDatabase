import unittest
from Firebase import Ramen

class PrettyPrinterTests(unittest.TestCase):
    def setUp(self):
        self.data = [
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


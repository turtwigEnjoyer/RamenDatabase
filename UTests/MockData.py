from Entities import Ramen as Ramen

""" Class to initialize mock data for testing"""
class MockData:
    def __init__(self):
        #id_num, brand, variety, style, country, stars, top_ten
        self.RamenList = [
            Ramen.Ramen( _id = 1,
                         brand = "Yatekomo",
                         variety = "a",
                         style = "Chicken",
                         stars = 5,
                         country = "Spain",
                         top_ten = True),
            Ramen.Ramen(_id = 2,
                        brand = "Yatekomo",
                        variety = "b",
                        style = "Beef And Egg",
                        stars = 4,
                        country = "Spain",
                        top_ten = False)
        ]
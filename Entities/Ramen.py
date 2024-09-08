""" Class to map the JSON objects to python objects"""
class Ramen:
    """
    Ramen should have the following attributes:
        Id,Brand,Variety,Style,Country,Stars,Top Ten
    Also some other optional attribute
     Top ten could be the optional attribute, since it is an empty field on our dataset
    """
    #TODO add optional attribute
    def __init__(self, id_num: int, brand: str, variety: str, style: str, country: str, stars: int, top_ten: bool):
        self.Id = id_num,
        self.Brand = brand,
        self.Variety = variety,
        self.Style = style,
        self.Country = country,
        self.Stars = stars,
        self.Top_Ten = top_ten

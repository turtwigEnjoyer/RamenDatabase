""" Class to map the JSON objects to python objects"""
class Ramen:
    """
    Ramen has the following attributes:
        Id,Brand,Variety,Style,Country,Stars
        Top Ten is optional
    """
    def __init__(self, _id: int, brand: str, variety: str, style: str, country: str, stars: int, top_ten = None):
        self.Id = _id
        self.Brand = brand
        self.Variety = variety
        self.Style = style
        self.Country = country
        self.Stars = stars
        self.Top_Ten = top_ten

    def __init__(self, ramen: dict):
        self.Id = ramen["_id"]
        self.Brand = ramen["brand"]
        self.Variety = ramen["variety"]
        self.Style = ramen["style"]
        self.Country = ramen["country"]
        self.Stars = ramen["stars"]
        self.Top_Ten = ramen["top_ten"]

    def to_dict(self) -> dict:
        return {"_id": self.Id, "brand": self.Brand, "variety": self.Variety, "style": self.Style, "country": self.Country, "stars": self.Stars, "top_ten": self.Top_Ten}





        

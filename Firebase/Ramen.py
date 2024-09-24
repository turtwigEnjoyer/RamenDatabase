""" Class to map the JSON objects to python objects"""
class Ramen:
    """
    Ramen should have the following attributes:
        Id,Brand,Variety,Style,Country,Stars,Top Ten
    Also some other optional attribute
     Top ten could be the optional attribute, since it is an empty field on our dataset
    """
    #TODO add optional attribute
    def __init__(self, _id: int, brand: str, variety: str, style: str, country: str, stars: int, top_ten: str):
        self.Id = _id
        self.Brand = brand
        self.Variety = variety
        self.Style = style
        self.Country = country
        self.Stars = stars
        self.Top_Ten = top_ten
    
    def to_dict(self) -> dict:
        return {"_id": self.Id, "brand": self.Brand, "variety": self.Variety, "style": self.Style, "country": self.Country, "stars": self.Stars, "top_ten": self.Top_Ten}

    @classmethod
    def from_dict(self, ramen: dict):
        self.Id = ramen["_id"]
        self.Brand = ramen["brand"]
        self.Variety = ramen["variety"]
        self.Style = ramen["style"]
        self.Country = ramen["country"]
        self.Stars = ramen["stars"]
        self.Top_Ten = ramen["top_ten"]

        return self




        

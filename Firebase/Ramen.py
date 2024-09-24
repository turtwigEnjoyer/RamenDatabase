""" Class to map the JSON objects to python objects"""
class Ramen:
    """
    Ramen should have the following attributes:
        Id,Brand,Variety,Style,Country,Stars,Top Ten
    Also some other optional attribute
     Top ten could be the optional attribute, since it is an empty field on our dataset
    """
    #TODO add optional attribute
    def __init__(self, Id: int, Brand: str, Variety: str, Style: str, Country: str, Stars: int, TopTen = None):
        self.Id = Id
        self.Brand = Brand
        self.Variety = Variety
        self.Style = Style
        self.Country = Country
        self.Stars = Stars
        self.TopTen = TopTen
    
    def to_dict(self) -> dict:
        return {"Id": self.Id, "Brand": self.Brand, "Variety": self.Variety, "Style": self.Style, "Country": self.Country, "Stars": self.Stars, "TopTen": self.TopTen}

    @classmethod
    def from_dict(cls, ramen: dict):
        return cls(Id = ramen["Id"],
            Brand = ramen["Brand"],
            Variety = ramen["Variety"],
            Style = ramen["Style"],
            Country = ramen["Country"],
            Stars = ramen["Stars"],
            TopTen = ramen["TopTen"])




        

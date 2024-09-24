from Firebase.DbInterface import DbInterface
from Firebase.Ramen import Ramen
import json

PATH_TO_DATASET = "./files/ramen_ratings_short.json"

#code to populate the database and run a simple query

#Reads a json file and transforms into list
def JsonToRamenList(jsonFilename) -> list[Ramen]:
        ramenList = []
        with open(jsonFilename) as fileData:
            jsonData = fileData.read()
        data = json.loads(jsonData)
        for ramenString in data:
            ramenList.append( Ramen(**ramenString))
        return ramenList

db = DbInterface()

ramenList = JsonToRamenList(PATH_TO_DATASET)
db.ClearDatabase()

for ram in ramenList:
     db.insert(ram)

from Firebase.DbInterface import DbInterface
from Firebase.Ramen import Ramen
import json

PATH_TO_DATASET = "./files/ramen_ratings_short.json"

#code to populate the database and run a simple query

#Reads a json file and transforms into list
def json_to_ramen_list( json_filename) -> list[Ramen]:
        ramen_list = []
        with open(json_filename) as file_data:
            json_data = file_data.read()
        data = json.loads(json_data)
        for ramen_string in data:
            ramen_list.append( Ramen(**ramen_string))
        return ramen_list

db = DbInterface()

r_List = json_to_ramen_list(PATH_TO_DATASET)
db.ClearDatabase()

for ram in r_List:
     db.insert(ram)

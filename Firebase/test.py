import json
from DbInterface import DbInterface
from Ramen import Ramen
from QueryFilter import QueryFilter

#code to populate the database and run a simple query

def json_to_ramen_list( json_filename) -> list[Ramen]:
        ramen_list = []
        with open(json_filename) as file_data:
            json_data = file_data.read()
        data = json.loads(json_data)
        for ramen_string in data:
            ramen_list.append( Ramen(**ramen_string))
        return ramen_list

db = DbInterface(collection_name="ramen_ratings")


# Populates the DB:
# r_List = json_to_ramen_list("C:/Users/brado/Documents/Soft. Eng/RamenDatabase/files/ramen_ratings_short.json")

# for ram in r_List:
#     db.insert(ram)


# Runs a simple Query
# rate_list = db.simple_query(query_filter= QueryFilter("stars", ">=",2))
# print(len(rate_list))

# Runs complex Query
filter1 = QueryFilter("stars", "<", 3)
filter2 = QueryFilter("variety", "==", "Cup")
#filters = [filter1, filter2]
result = db.compound_query([filter1, filter2])
print(len(result))
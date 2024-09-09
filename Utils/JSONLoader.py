""" Should take an input JSON file and upload it to the cloud database """
import json

from Database.DbInterface import DbInterface
from Entities import Ramen

class JSONLoader:
    def __init__(self, database_context: DbInterface):
        self.DatabaseContext = database_context

    @staticmethod
    def json_to_ramen(json_string):
        return Ramen.Ramen(**json_string)

    @staticmethod
    def json_to_ramen_list( json_filename) -> list[Ramen]:
        ramen_list = []
        with open(json_filename) as file_data:
            json_data = file_data.read()
        data = json.loads(json_data)
        for ramen_string in data:
            ramen_list.append( JSONLoader.json_to_ramen(ramen_string) )
        return ramen_list

    def insert_ramen(self, ramen: Ramen):
        self.DatabaseContext.insert(ramen)
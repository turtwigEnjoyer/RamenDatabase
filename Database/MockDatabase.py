from Database.DbInterface import DbInterface
from Entities import Ramen

"""
Class used to mock a database functions without having a database
Instead of having the logic of the database in code we just call the insert or query
"""
class MockDatabase (DbInterface):
    def __init__(self, ramen_list: list):
        self.ramen_list = ramen_list

    """ 
    Mocks insertion of a ramen object into a database
    """
    def insert(self, ramen_object: Ramen):
        self.ramen_list.append(ramen_object)

    """
    Find all the objects matching a simple query
    """
    def simple_query(self, field: str, value: str):
        matching_objects = []
        for ramen in self.ramen_list:
            field_value = getattr(ramen, field, None)
            if field_value == value:
                matching_objects.append(ramen)
        return matching_objects

    #TODO AddComplexQueries
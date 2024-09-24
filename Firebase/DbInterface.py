from idlelib.query import Query

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore as firestore
from google.cloud.firestore_v1 import FieldFilter

from Firebase.QueryFilter import QueryFilter
from Firebase.AbstractDb import AbstractDb
from Firebase import Ramen

""" Class to create and control the database"""
class DbInterface(AbstractDb):
    """
        Creates a Database and then handles record insertion as well as query execution
    """
    def __init__(self):
        super().__init__()
        # Use a service account.
        cred = credentials.Certificate('./cs3050-warmup-project-17f83-firebase-adminsdk-1gomb-858737ebab.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection = self.db.collection("ramen_ratings")
    
    # Receives a Ramen object to insert to DB
    def insert(self, ramen_object: Ramen) -> None:
        # convert to dict to easily pass to DB, then pass to DB using _id as the unique id
        ram_obj_dict = ramen_object.to_dict()
        doc_ref = self.collection.document(str(ram_obj_dict.pop("_id")))
        doc_ref.set(ram_obj_dict) 

    # Executes queries to the DB using filtering to retrieve the desired data
    def simple_query(self, query_filter: QueryFilter) -> list[Ramen]:

        # Retrieve query with designated filtering
        firebase_filter = FieldFilter(query_filter.field, query_filter.comparer, query_filter.value)

        query_results=(self.collection.where(filter = firebase_filter).stream())

        return self.query_results_to_list(query_results)

    """
    Runs a query with unlimited AND statements. Takes in lists of filters
    Careful! Will throw exception if we attempt to run a compound query that uses operators other than ==
    on fields other than stars.
    If we dont want an exception we need to create an index manually 
    """
    def compound_query(self, query_filters: list[QueryFilter]) -> list[Ramen]:

        filtered_collection = self.collection
        for query_filter in query_filters:
            firebase_filter = FieldFilter(query_filter.field, query_filter.comparer, query_filter.value)
            filtered_collection = filtered_collection.where(filter = firebase_filter)

        query_results = filtered_collection.stream()
        return self.query_results_to_list(query_results)


    @staticmethod
    def query_results_to_list(query_results) -> list[Ramen]:
        ramen_list = list[Ramen]()

        for result in query_results:
            ramen_list.append(Ramen.from_dict({**{'_id': int(result.id)},**result.to_dict()}))

        return ramen_list

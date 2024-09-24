from idlelib.query import Query


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore as firestore
from google.cloud.firestore_v1 import FieldFilter

from Firebase.QueryFilter import QueryFilter
from Firebase.AbstractDb import AbstractDb
from Firebase.Ramen import Ramen


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
        doc_ref = self.collection.document(str(ram_obj_dict["_id"]))
        doc_ref.set(ram_obj_dict) 

    def ClearDatabase(self):
        for document in self.collection.list_documents():
            document.delete()

    """
    Runs a query with unlimited AND statements. Takes in lists of filters
    Careful! Will throw exception if we attempt to run a compound query that uses operators other than ==
    on fields other than stars.
    If we dont want an exception we need to create an index manually 
    """
    def Query(self, query_filters: list[QueryFilter]) -> list[Ramen]:

        filteredCollection = self.collection
        for query_filter in query_filters:
            firebaseFilter = FieldFilter(query_filter.field, query_filter.comparer, query_filter.value)
            filteredCollection = filteredCollection.where(filter = firebaseFilter)

        queryResults = filteredCollection.get()
        return self.queryResultsToList(queryResults)


    @staticmethod
    def queryResultsToList(query_results) -> list[Ramen]:
        ramen_list = list[Ramen]()

        for result in query_results:

            ramen = Ramen.from_dict( {**{'_id': int(result.id)},**result.to_dict()} )
            ramen_list.append( ramen )

        return ramen_list

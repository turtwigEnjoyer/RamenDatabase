import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore as firestore

from Firebase.QueryFilter import QueryFilter
from Firebase.AbstractDb import AbstractDb
from Ramen import Ramen

""" Class to create and control the database"""
class DbInterface(AbstractDb):
    """
        Creates a Database and then handles record insertion as well as query execution
    """
    def __init__(self):
        # Use a service account.
        cred = credentials.Certificate('./cs3050-warmup-project-17f83-firebase-adminsdk-1gomb-858737ebab.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
    
    # Receives a Ramen object to insert to DB
    def insert(self, ramen_object: Ramen) -> None:
        # convert to dict to easily pass to DB, then pass to DB using _id as the unique id
        ram_obj_dict = ramen_object.to_dict()
        doc_ref = self.db.collection("ramen_ratings").document(str(ram_obj_dict.pop("_id")))
        doc_ref.set(ram_obj_dict) 

    # Executes queries to the DB using filtering to retrieve the desired data
    def simple_query(self, filter: QueryFilter) -> list[Ramen]:
        ramen_list = []
        # Retrieve query with designated filtering
        firebase_filter = firestore.FieldFilter(filter.field, filter.comparer, filter.value)

        query_results=(self.db.collection("ramen_ratings").where(firebase_filter).stream())

        # convert into Ramen object
        for result in query_results:
            ramen_list.append(Ramen.from_dict({**{'_id': int(result.id)},**result.to_dict()}))

        return ramen_list


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore as firestore
from google.cloud.firestore_v1 import FieldFilter

from Firebase.QueryFilter import QueryFilter
from Firebase.Ramen import Ramen


KEY_FILE_NAME = ("cs3050-warmup-project-17f83-firebase-adminsdk-1gomb-798ef63fc5.json")
""" Class to create and control the database"""
class DbInterface():
    """
        Creates a Database and then handles record insertion as well as query execution
    """
    def __init__(self):
        # Use a service account.
        cred = credentials.Certificate(KEY_FILE_NAME)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection = self.db.collection("ramen_ratings")
    
    # Receives a Ramen object to insert to DB
    def insert(self, ramenObject: Ramen) -> None:
        # convert to dict to easily pass to DB, then pass to DB using _id as the unique id
        ramObjDict = ramenObject.ToDict()
        docRef = self.collection.document(str(ramObjDict["Id"]))
        docRef.set(ramObjDict) 

    def ClearDatabase(self):
        for document in self.collection.list_documents():
            document.delete()

    """
    Runs a query with unlimited AND statements. Takes in lists of filters
    Careful! Will throw exception if we attempt to run a compound query that uses operators other than ==
    on fields other than stars.
    If we dont want an exception we need to create an index manually 
    """
    def Query(self, queryFilters: list[QueryFilter]) -> list[Ramen]:

        filteredCollection = self.collection
        for queryFilter in queryFilters:
            firebaseFilter = FieldFilter(queryFilter.field, queryFilter.comparer, queryFilter.value)
            filteredCollection = filteredCollection.where(filter = firebaseFilter)

        queryResults = filteredCollection.get()
        return self.queryResultsToList(queryResults)


    @staticmethod
    def queryResultsToList(queryResults) -> list[Ramen]:
        ramenList = list[Ramen]()

        for result in queryResults:

            ramen = Ramen.FromDict(result.to_dict())
            ramenList.append( ramen )

        return ramenList

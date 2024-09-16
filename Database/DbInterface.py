import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys
sys.path.append('C:/Users/brado/Documents/Soft. Eng/RamenDatabase/')
from Entities.Ramen import Ramen as Ramen

""" Class to create and control the database"""
class DbInterface:
    """
        Creates a Database and then handles record insertion as well as query execution
    """
    def __init__(self):
        # Use a service account.
        cred = credentials.Certificate('./cs3050-warmup-project-17f83-firebase-adminsdk-1gomb-858737ebab.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def insert(self, ramen_object: Ramen) -> None:
        doc_ref = self.db.collection("ramen_ratings").document(str(ramen_object.Id))
        doc_ref.set({"brand": ramen_object.Brand, "variety": ramen_object.Variety, "style": ramen_object.Style, "country": ramen_object.Country, "stars": ramen_object.Stars, "top-ten": ramen_object.Top_Ten}) 

    def simple_query(self, field: str, value: str) -> list[Ramen]:
        pass


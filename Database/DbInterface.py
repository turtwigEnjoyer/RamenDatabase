import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from Entities.Ramen import Ramen

class DbInterface:
    def __init__(self):
        # Use a service account.
        cred = credentials.Certificate('./cs3050-warmup-project-17f83-firebase-adminsdk-1gomb-858737ebab.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def insert(self, ramen_object: Ramen) -> None:
        pass

    def simple_query(self, field: str, value: str) -> list[Ramen]:
        pass


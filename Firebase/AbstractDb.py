from Firebase import Ramen
from Firebase import QueryFilter
class AbstractDb:

    def __init__(self):
        pass

    # Receives a Ramen object to insert to DB
    def insert(self, ramen_object: Ramen) -> None:
        pass

    def simple_query(self, query_filter: QueryFilter) -> list[Ramen]:
        pass
from Entities import Ramen
class DbInterface:
    def insert(self, ramen_object: Ramen) -> None:
        pass

    def simple_query(self, field: str, value: str) -> list[Ramen]:
        pass


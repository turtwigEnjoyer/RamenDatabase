class QueryFilter:
    def __init__(self, field, comparer, value):
        self.field = field
        self.comparer = comparer
        self.value = value

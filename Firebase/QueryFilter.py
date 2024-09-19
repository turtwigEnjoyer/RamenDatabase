class QueryFilter:
    def __init__(self, field, comparer, value):
        self.field = field
        self.comparer = comparer
        self.value = value

    def __str__(self):
        return str(self.field) + " " + str(self.comparer) + " " + str(self.value)

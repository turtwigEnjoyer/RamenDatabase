from antlr4 import *
from QueryParser import QueryParser
from QueryLexer import QueryLexer
from QueryVisitor import QueryVisitor
from QueryListener import QueryListener
from Firebase.QueryFilter import QueryFilter
from Firebase.DbInterface import DbInterface
from query import MyVisitor


class Engine:
    def __init__(self):
        self.database = DbInterface()

    def query_engine(self, query):
        try:
            stream = InputStream(query)
            lexer = QueryLexer(stream)
            stream = CommonTokenStream(lexer)
            parser = QueryParser(stream)
            tree = parser.prog()
            visitor = MyVisitor()
            output = visitor.visit(tree)
            ramen_list = self.database.compound_query(output)
            ## Need to print ramen_list

            return 0
        except Exception as e:
            return str(e)






def menu():
    print("Welcome: To get information about various types of Ramen, enter a query such as 'Country == Japan and "
          "Stars: > 5'")
    print("Available filters are: Brand, Country, Style, Variety, Stars")
    print('Use "AND" to combine up to two filters')
    print("Type 'help' for full list of available commands")
    print("Type 'quit' to quit")

if __name__ == '__main__':
    engine = Engine()
    menu()
    query = str(input("Enter your query: "))
    while query != 'quit':
        if query == 'help':
            menu()
        else:
            engine.query_engine(query)
        query = str(input("Enter your query: "))
    print("Goodbye!")
    quit
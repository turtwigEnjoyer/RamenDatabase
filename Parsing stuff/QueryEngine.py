from antlr4 import *
from QueryParser import QueryParser
from QueryLexer import QueryLexer
from QueryVisitor import QueryVisitor
from QueryListener import QueryListener
from Firebase.QueryFilter import QueryFilter
from Firebase.DbInterface import DbInterface
from Firebase.PrettyPrinter import PrettyPrinter
from query import MyVisitor


class Engine:
    def __init__(self):
        self.database = DbInterface()
        self.prettyPrinter = PrettyPrinter()

    def query_engine(self, query):
        try:
            stream = InputStream(query)
            lexer = QueryLexer(stream)
            stream = CommonTokenStream(lexer)
            parser = QueryParser(stream)
            tree = parser.prog()
            visitor = MyVisitor()
            output = visitor.visit(tree)
            ramen_list = self.database.Query(output)
            ## Need to print ramen_list
            self.prettyPrinter.print(ramen_list)

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
    query = str(input("Enter your query: ") + "\n")
    while query != 'quit\n':
        if query == 'help\n':
            menu()
        else:
            engine.query_engine(query)
        query = str(input("Enter your query: ") + "\n")
    print("Goodbye!")
    quit
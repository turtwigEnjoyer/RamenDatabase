from antlr4 import *
from QueryParser import QueryParser
from QueryLexer import QueryLexer
from QueryVisitor import QueryVisitor
from QueryListener import QueryListener
from Firebase.QueryFilter import QueryFilter
from query import MyVisitor

def query_engine(query):
    try:
        stream = InputStream(query)
        lexer = QueryLexer(stream)
        stream = CommonTokenStream(lexer)
        parser = QueryParser(stream)
        tree = parser.prog()
        visitor = MyVisitor()
        output = visitor.visit(tree)
        for x in output:
            print(x)
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
    menu()
    query = str(input("Enter your query: ") + "\n")
    while query != 'quit':
        if query == 'help':
            menu()
        else:
            query_engine(query)
        query = str(input("Enter your query: ") + "\n")
    print("Goodbye!")
    quit
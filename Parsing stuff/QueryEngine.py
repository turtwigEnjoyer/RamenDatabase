from antlr4 import *
from QueryParser import QueryParser
from QueryLexer import QueryLexer
from QueryVisitor import QueryVisitor
from QueryListener import QueryListener
from Firebase.QueryFilter import QueryFilter
from Firebase.DbInterface import DbInterface
from Firebase.PrettyPrinter import PrettyPrinter
from query import MyVisitor
from antlr4.error.ErrorListener import ErrorListener


#TODO: error handling
# 'and' typed wrong gives second query but not the first
# give an error message for things or avoid crashes entirely

#fixed:
# quotations work with spaced value entries
# no spaced filters so no adjustments on that one

class ErrorListener(ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Syntax error at line " + str(line) + ":" + str(column))
        print("Please enter a valid query.")

#Engine class contains the commands that need to be run to start up the parser and then connect it to the database
# This is where the two parts of the project come together and work together to query the data from the database
class Engine:
    #constructor method that creates database and pretty printer instances
    def __init__(self):
        self.database = DbInterface()
        self.prettyPrinter = PrettyPrinter()

    #Query engine function that boots up the ANTLR parser
    #The queries passed into this method are then sent to the parser to be broken down
    #This will then request that data from the database and print it nicely to be displayed to the user

    def query_engine(self, query):
        try:
            stream = InputStream(query)
            lexer = QueryLexer(stream)
            tokenStream = CommonTokenStream(lexer)
            parser = QueryParser(tokenStream)

            parser.removeErrorListeners()
            parser.addErrorListener(ErrorListener())

            tree = parser.prog()
            visitor = MyVisitor()
            output = visitor.visit(tree)

            ramenList = self.database.Query(output)
            self.prettyPrinter.print(ramenList)
            return 0

        except Exception as e:
            # print(f"Error {e}")
            return str(e)


#menu function prints out all info needed by user to operate the query system
def menu():
    print("Welcome: To get information about various types of Ramen, enter a query such as 'Filter == Value AND "
          "Filter > Value'")
    print('All queries that contain a word with spaces in it like: Country == "South Korea" must be typed with quotes'
          ' as shown.')
    print("Available filters are: Brand, Country, Style, Variety, Stars")
    print("Use 'AND' to combine up to two filters")
    print("Type 'help' for full list of available commands")
    print("Type 'quit' to quit")


#main method creates the engine and starts off the program allowing the user to query as much as they desire
if __name__ == '__main__':
    engine = Engine()
    menu()
    query = str(input("Enter your query: ") + "\n")
    while query.lower() != 'quit\n':
        if query.lower() == 'help\n':
            menu()
        else:
            engine.query_engine(query)
        query = str(input("Enter your query: ") + "\n")
    print("Goodbye!")
    quit()

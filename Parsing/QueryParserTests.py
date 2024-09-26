import sys
sys.path.append("../")
from antlr4 import *
from QueryParser import QueryParser
from QueryLexer import QueryLexer
from QueryVisitor import QueryVisitor
from QueryListener import QueryListener
from Firebase.QueryFilter import QueryFilter
import query

#Testing class for all parser
# doesnt use our errorlistener class so still reads things as errors that do not show up in the query engine
# tests still helped us figure out a lot about our code though
class QueryParserTests:
    def setUp(self):
        self.lexer = None
        self.parser = None
    def parseQuery(self, query):
        input = InputStream(query)
        self.lexer = QueryLexer(input)
        tokenStream = CommonTokenStream(self.lexer)
        self.parser = QueryParser(tokenStream)
        result = self.parser.prog()
        return result

    def testQuery1(self):
        testQuery1 = "Country == Japan AND stars > 4\n"
        print(f"Testing parser Case 1: {testQuery1}")
        tree = self.parseQuery(testQuery1)
        print(tree)
        visitor = query.MyVisitor()
        print(visitor.visit(tree))
        output = visitor.visit(tree)
        if output is None:
            print("Test Failed")
        else:
            print(output)
            for x in output:
                print(x)
        return 0

    def testQuery2(self):
        testQuery2 = "Style == pack AND Brand == Wang\n"
        print(f"Testing parser Case 2: {testQuery2}")
        tree = self.parseQuery(testQuery2)
        visitor = query.MyVisitor()
        output = visitor.visit(tree)
        if output is None:
            print("Test Failed")
        else:
            print(output)
            for x in output:
                print(x)
        return 0

    def testQuery3(self):
        testQuery3 = "Style == Pack AND Stars == 8\n"
        print(f"Testing parser Case 3: {testQuery3}")
        tree = self.parseQuery(testQuery3)
        visitor = query.MyVisitor()
        output = visitor.visit(tree)
        if output is None:
            print("Test Failed")
        else:
            print(output)
            for x in output:
                print(x)
        return 0

    def testQuery4(self):
        testQuery4 = "Brand == \"Samyang Foods\"\n"
        print(f"Testing parser Case 4: {testQuery4}")
        tree = self.parseQuery(testQuery4)
        visitor = query.MyVisitor()
        output = visitor.visit(tree)
        if output is None:
            print("Test Failed")
        else:
            print(output)
            for x in output:
                print(x)
        return 0

if __name__ == '__main__':
    test = QueryParserTests()
    test.testQuery1()
    test.testQuery2()
    test.testQuery3()
    test.testQuery4()

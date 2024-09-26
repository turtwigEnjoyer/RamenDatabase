import ast

from antlr4 import *
from QueryParser import QueryParser
from QueryLexer import QueryLexer
from QueryVisitor import QueryVisitor
from QueryListener import QueryListener
from Firebase.QueryFilter import QueryFilter


# overwrites generated visitor from the antlr grammar to do the things we actually want it to do
# still probably needs to be updated to fit our current use case
#
class MyVisitor(QueryVisitor):
    #constructor method just initializes the storage container
    def __init__(self):
        self.storage = []

    #the visitPrintJoin method is the last visited method that actually returns the command to the engine
    # this one is specifically for if the query is a compound query with an 'AND' in it
    def visitPrintJoin(self, ctx):
        container = self.visit(ctx.expr(0))
        marker = 0
        if container not in self.storage:
            marker += 1
            self.storage.append(container)
        container = self.visit(ctx.expr(1))
        if container not in self.storage:
            marker += 1
            self.storage.append(container)
        #if marker > 0:
            #print(self.storage)
        return self.storage

    #visitPrintExpr is for any other queries
    #returns these queries back to the engine to actually gather data from the database
    def visitPrintExpr(self, ctx):
        container = self.visit(ctx.expr())
        self.storage.append(container)
        #print(self.storage)
        return self.storage

    #the visitCompare method visits goes in one more layer of the ANTLR and breaks up the operation and
    # then each side of the query: filter and value
    def visitCompare(self, ctx):
        left = ctx.ID().getText().capitalize()
        right = self.visit(ctx.val())
        op = ctx.op.text
        container = QueryFilter(left, op, right)
        return container

    # the visitID method visits the value held in the ID spot so it grabs the filter string as well as the value
    # if its a string
    def visitId(self, ctx):
        identifier = ctx.ID().getText()
        identifier = identifier.strip('"')
        #breaking up multi-worded answer
        words = identifier.split(' ')
        identifier = ""
        #and putting it back together capitalized correctly
        for word in words:
            word.capitalize()
            identifier += word
            if word != words[-1]:
                identifier += " "
        return identifier

    #Finally visitInt grabs the value if it is an int and sends it up through the visitor chain
    def visitInt(self, ctx):
        return int(ctx.INT().getText())


# Test main method that shows the use of visitor this shows all the setup for utilizing an antlr visitor class
# Ideally nobody should need to download antlr or anything because all the classes required are pre-generated in the
# repo. We will have to change this file to be just a class definition file for the visitor and then implement the
# below code in the query engine. This code will then be hooked up to user input to parse each incoming query. It will
# then be sent to the interface that filters and collects the data from the database finally that filtered data will
# be printed onscreen for the user's pleasure
# def main(): #test
#     stream = InputStream('country == "New Zealand" AND Stars > 4\n')
#     lexer = QueryLexer(stream)
#     stream = CommonTokenStream(lexer)
#     parser = QueryParser(stream)
#     tree = parser.prog()
#     visitor = MyVisitor()
#     output = visitor.visit(tree)
#     print(output)
#     for x in output:
#         print(x)
#     return 0
#
#
# main()


def testParser(inputQuery):
    stream = InputStream(inputQuery)
    lexer = QueryLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = QueryParser(token_stream)
    tree = parser.prog()
    visitor = MyVisitor()
    visitor.visit(tree)
    return visitor.storage

testQuery1 = 'Country == "South Korea" AND Stars > 4\n'
testQuery2 = "Style == pack AND Brand == Wang"
testQuery3 = "Variety == soup"
testQuery4 = "Brand == 'Samyang Foods' AND Stars == 5"

print(testParser(testQuery1))
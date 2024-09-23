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
    def __init__(self):
        self.storage = []

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

    def visitPrintExpr(self, ctx):
        container = self.visit(ctx.expr())
        self.storage.append(container)
        #print(self.storage)
        return self.storage

    def visitCompare(self, ctx):
        left = ctx.ID().getText()
        right = self.visit(ctx.val())
        op = ctx.op.text
        container = QueryFilter(left, op, right)
        return container

    def visitId(self, ctx):
        identifier = ctx.ID().getText()
        identifier = identifier.strip('"')
        return identifier

    def visitInt(self, ctx):
        return int(ctx.INT().getText())


# Test main method that shows the use of visitor this shows all the setup for utilizing an antlr visitor class
# Ideally nobody should need to download antlr or anything because all the classes required are pre-generated in the
# repo. We will have to change this file to be just a class definition file for the visitor and then implement the
# below code in the query engine. This code will then be hooked up to user input to parse each incoming query. It will
# then be sent to the interface that filters and collects the data from the database finally that filtered data will
# be printed onscreen for the user's pleasure
def main(): #test
    stream = InputStream('Country == "New Zealand"\n')
    lexer = QueryLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = QueryParser(stream)
    tree = parser.prog()
    visitor = MyVisitor()
    output = visitor.visit(tree)
    for x in output:
        print(x)
    return 0


main()

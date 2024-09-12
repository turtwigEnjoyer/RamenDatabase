import ast

from antlr4 import *
from QueryParser import QueryParser
from QueryLexer import QueryLexer
from QueryVisitor import QueryVisitor
from QueryListener import QueryListener


# overwrites generated visitor from the antlr grammar to do the things we actually want it to do
# still probably needs to be updated to fit our current use case
#
class MyVisitor(QueryVisitor):
    def __init__(self):
        self.left = ""
        self.right = ""

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitVal(self, ctx):
        return ctx.VAL

    def visitCompare(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ctx.op.type

    def visitJoin(self, ctx):
        return ctx.op.type


def main():
    stream = InputStream("country != Japan AND ratings <= 4\n")
    lexer = QueryLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = QueryParser(stream)
    tree = parser.prog()
    visitor = MyVisitor()
    output = visitor.visit(tree)
    print(output)
    return 0


main()

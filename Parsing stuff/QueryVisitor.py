# Generated from C:/Users/jackk/OneDrive/College/Fall Semester 2024/CS3050/RamenDatabase/Parsing stuff/Query.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QueryParser import QueryParser
else:
    from QueryParser import QueryParser

# This class defines a complete generic visitor for a parse tree produced by QueryParser.

class QueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QueryParser#prog.
    def visitProg(self, ctx:QueryParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#printExpr.
    def visitPrintExpr(self, ctx:QueryParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#blank.
    def visitBlank(self, ctx:QueryParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#compare.
    def visitCompare(self, ctx:QueryParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#join.
    def visitJoin(self, ctx:QueryParser.JoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#id.
    def visitId(self, ctx:QueryParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#val.
    def visitVal(self, ctx:QueryParser.ValContext):
        return self.visitChildren(ctx)



del QueryParser
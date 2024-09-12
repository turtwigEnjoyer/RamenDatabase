# Generated from C:/Users/jackk/OneDrive/College/Fall Semester 2024/CS3050/RamenDatabase/Parsing stuff/Query.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QueryParser import QueryParser
else:
    from QueryParser import QueryParser

# This class defines a complete listener for a parse tree produced by QueryParser.
class QueryListener(ParseTreeListener):

    # Enter a parse tree produced by QueryParser#prog.
    def enterProg(self, ctx:QueryParser.ProgContext):
        pass

    # Exit a parse tree produced by QueryParser#prog.
    def exitProg(self, ctx:QueryParser.ProgContext):
        pass


    # Enter a parse tree produced by QueryParser#printExpr.
    def enterPrintExpr(self, ctx:QueryParser.PrintExprContext):
        pass

    # Exit a parse tree produced by QueryParser#printExpr.
    def exitPrintExpr(self, ctx:QueryParser.PrintExprContext):
        pass


    # Enter a parse tree produced by QueryParser#blank.
    def enterBlank(self, ctx:QueryParser.BlankContext):
        pass

    # Exit a parse tree produced by QueryParser#blank.
    def exitBlank(self, ctx:QueryParser.BlankContext):
        pass


    # Enter a parse tree produced by QueryParser#compare.
    def enterCompare(self, ctx:QueryParser.CompareContext):
        pass

    # Exit a parse tree produced by QueryParser#compare.
    def exitCompare(self, ctx:QueryParser.CompareContext):
        pass


    # Enter a parse tree produced by QueryParser#join.
    def enterJoin(self, ctx:QueryParser.JoinContext):
        pass

    # Exit a parse tree produced by QueryParser#join.
    def exitJoin(self, ctx:QueryParser.JoinContext):
        pass


    # Enter a parse tree produced by QueryParser#id.
    def enterId(self, ctx:QueryParser.IdContext):
        pass

    # Exit a parse tree produced by QueryParser#id.
    def exitId(self, ctx:QueryParser.IdContext):
        pass


    # Enter a parse tree produced by QueryParser#val.
    def enterVal(self, ctx:QueryParser.ValContext):
        pass

    # Exit a parse tree produced by QueryParser#val.
    def exitVal(self, ctx:QueryParser.ValContext):
        pass



del QueryParser
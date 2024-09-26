# Generated from C:/Users/jackk/OneDrive/College/Fall Semester 2024/CS3050/RamenDatabase/Parsing/Query.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by QueryParser#printJoin.
    def enterPrintJoin(self, ctx:QueryParser.PrintJoinContext):
        pass

    # Exit a parse tree produced by QueryParser#printJoin.
    def exitPrintJoin(self, ctx:QueryParser.PrintJoinContext):
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


    # Enter a parse tree produced by QueryParser#brand.
    def enterBrand(self, ctx:QueryParser.BrandContext):
        pass

    # Exit a parse tree produced by QueryParser#brand.
    def exitBrand(self, ctx:QueryParser.BrandContext):
        pass


    # Enter a parse tree produced by QueryParser#country.
    def enterCountry(self, ctx:QueryParser.CountryContext):
        pass

    # Exit a parse tree produced by QueryParser#country.
    def exitCountry(self, ctx:QueryParser.CountryContext):
        pass


    # Enter a parse tree produced by QueryParser#style.
    def enterStyle(self, ctx:QueryParser.StyleContext):
        pass

    # Exit a parse tree produced by QueryParser#style.
    def exitStyle(self, ctx:QueryParser.StyleContext):
        pass


    # Enter a parse tree produced by QueryParser#variety.
    def enterVariety(self, ctx:QueryParser.VarietyContext):
        pass

    # Exit a parse tree produced by QueryParser#variety.
    def exitVariety(self, ctx:QueryParser.VarietyContext):
        pass


    # Enter a parse tree produced by QueryParser#stars.
    def enterStars(self, ctx:QueryParser.StarsContext):
        pass

    # Exit a parse tree produced by QueryParser#stars.
    def exitStars(self, ctx:QueryParser.StarsContext):
        pass


    # Enter a parse tree produced by QueryParser#topTen.
    def enterTopTen(self, ctx:QueryParser.TopTenContext):
        pass

    # Exit a parse tree produced by QueryParser#topTen.
    def exitTopTen(self, ctx:QueryParser.TopTenContext):
        pass


    # Enter a parse tree produced by QueryParser#id.
    def enterId(self, ctx:QueryParser.IdContext):
        pass

    # Exit a parse tree produced by QueryParser#id.
    def exitId(self, ctx:QueryParser.IdContext):
        pass


    # Enter a parse tree produced by QueryParser#int.
    def enterInt(self, ctx:QueryParser.IntContext):
        pass

    # Exit a parse tree produced by QueryParser#int.
    def exitInt(self, ctx:QueryParser.IntContext):
        pass



del QueryParser
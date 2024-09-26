# Generated from C:/Users/jackk/OneDrive/College/Fall Semester 2024/CS3050/RamenDatabase/Parsing/Query.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by QueryParser#printJoin.
    def visitPrintJoin(self, ctx:QueryParser.PrintJoinContext):
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


    # Visit a parse tree produced by QueryParser#brand.
    def visitBrand(self, ctx:QueryParser.BrandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#country.
    def visitCountry(self, ctx:QueryParser.CountryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#style.
    def visitStyle(self, ctx:QueryParser.StyleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#variety.
    def visitVariety(self, ctx:QueryParser.VarietyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#stars.
    def visitStars(self, ctx:QueryParser.StarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#topTen.
    def visitTopTen(self, ctx:QueryParser.TopTenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#id.
    def visitId(self, ctx:QueryParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#int.
    def visitInt(self, ctx:QueryParser.IntContext):
        return self.visitChildren(ctx)



del QueryParser
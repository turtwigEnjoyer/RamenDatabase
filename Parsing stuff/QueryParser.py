# Generated from C:/Users/jackk/OneDrive/College/Fall Semester 2024/CS3050/RamenDatabase/Parsing stuff/Query.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,37,8,3,1,4,1,4,3,4,41,8,
        4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,1,2,1,0,9,14,46,0,11,1,0,0,0,2,24,
        1,0,0,0,4,26,1,0,0,0,6,36,1,0,0,0,8,40,1,0,0,0,10,12,3,2,1,0,11,
        10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,
        0,15,16,3,4,2,0,16,17,7,0,0,0,17,18,3,4,2,0,18,19,5,17,0,0,19,25,
        1,0,0,0,20,21,3,4,2,0,21,22,5,17,0,0,22,25,1,0,0,0,23,25,5,17,0,
        0,24,15,1,0,0,0,24,20,1,0,0,0,24,23,1,0,0,0,25,3,1,0,0,0,26,27,3,
        6,3,0,27,28,7,1,0,0,28,29,3,8,4,0,29,5,1,0,0,0,30,37,5,3,0,0,31,
        37,5,4,0,0,32,37,5,5,0,0,33,37,5,6,0,0,34,37,5,7,0,0,35,37,5,8,0,
        0,36,30,1,0,0,0,36,31,1,0,0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,
        1,0,0,0,36,35,1,0,0,0,37,7,1,0,0,0,38,41,5,15,0,0,39,41,5,16,0,0,
        40,38,1,0,0,0,40,39,1,0,0,0,41,9,1,0,0,0,4,13,24,36,40
    ]

class QueryParser ( Parser ):

    grammarFileName = "Query.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'AND'", "'OR'", "'Brand'", "'Country'", 
                     "'Style'", "'Variety'", "'Stars'", "'TopTen'", "'=='", 
                     "'<'", "'>'", "'<='", "'>='", "'!='" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "BRAND", "COUNTRY", "STYLE", 
                      "VARIETY", "STARS", "TOPTEN", "EQ", "LT", "GT", "LTEQ", 
                      "GTEQ", "NEQ", "ID", "INT", "NEWLINE", "WS", "ANY", 
                      "QUOTED_ID" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_expr = 2
    RULE_filter = 3
    RULE_val = 4

    ruleNames =  [ "prog", "command", "expr", "filter", "val" ]

    EOF = Token.EOF
    AND=1
    OR=2
    BRAND=3
    COUNTRY=4
    STYLE=5
    VARIETY=6
    STARS=7
    TOPTEN=8
    EQ=9
    LT=10
    GT=11
    LTEQ=12
    GTEQ=13
    NEQ=14
    ID=15
    INT=16
    NEWLINE=17
    WS=18
    ANY=19
    QUOTED_ID=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.CommandContext)
            else:
                return self.getTypedRuleContext(QueryParser.CommandContext,i)


        def getRuleIndex(self):
            return QueryParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = QueryParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.command()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 131576) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(QueryParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintJoinContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.CommandContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.ExprContext)
            else:
                return self.getTypedRuleContext(QueryParser.ExprContext,i)

        def NEWLINE(self):
            return self.getToken(QueryParser.NEWLINE, 0)
        def AND(self):
            return self.getToken(QueryParser.AND, 0)
        def OR(self):
            return self.getToken(QueryParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintJoin" ):
                listener.enterPrintJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintJoin" ):
                listener.exitPrintJoin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintJoin" ):
                return visitor.visitPrintJoin(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(QueryParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(QueryParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def command(self):

        localctx = QueryParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = QueryParser.PrintJoinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr()
                self.state = 16
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 17
                self.expr()
                self.state = 18
                self.match(QueryParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = QueryParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.expr()
                self.state = 21
                self.match(QueryParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = QueryParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(QueryParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def filter_(self):
            return self.getTypedRuleContext(QueryParser.FilterContext,0)

        def val(self):
            return self.getTypedRuleContext(QueryParser.ValContext,0)

        def EQ(self):
            return self.getToken(QueryParser.EQ, 0)
        def LT(self):
            return self.getToken(QueryParser.LT, 0)
        def GT(self):
            return self.getToken(QueryParser.GT, 0)
        def LTEQ(self):
            return self.getToken(QueryParser.LTEQ, 0)
        def GTEQ(self):
            return self.getToken(QueryParser.GTEQ, 0)
        def NEQ(self):
            return self.getToken(QueryParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = QueryParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            localctx = QueryParser.CompareContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.filter_()
            self.state = 27
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 28
            self.val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_filter

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CountryContext(FilterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.FilterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COUNTRY(self):
            return self.getToken(QueryParser.COUNTRY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountry" ):
                listener.enterCountry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountry" ):
                listener.exitCountry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCountry" ):
                return visitor.visitCountry(self)
            else:
                return visitor.visitChildren(self)


    class VarietyContext(FilterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.FilterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIETY(self):
            return self.getToken(QueryParser.VARIETY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariety" ):
                listener.enterVariety(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariety" ):
                listener.exitVariety(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariety" ):
                return visitor.visitVariety(self)
            else:
                return visitor.visitChildren(self)


    class StyleContext(FilterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.FilterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STYLE(self):
            return self.getToken(QueryParser.STYLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStyle" ):
                listener.enterStyle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStyle" ):
                listener.exitStyle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStyle" ):
                return visitor.visitStyle(self)
            else:
                return visitor.visitChildren(self)


    class TopTenContext(FilterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.FilterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOPTEN(self):
            return self.getToken(QueryParser.TOPTEN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopTen" ):
                listener.enterTopTen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopTen" ):
                listener.exitTopTen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopTen" ):
                return visitor.visitTopTen(self)
            else:
                return visitor.visitChildren(self)


    class StarsContext(FilterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.FilterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STARS(self):
            return self.getToken(QueryParser.STARS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStars" ):
                listener.enterStars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStars" ):
                listener.exitStars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStars" ):
                return visitor.visitStars(self)
            else:
                return visitor.visitChildren(self)


    class BrandContext(FilterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.FilterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BRAND(self):
            return self.getToken(QueryParser.BRAND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrand" ):
                listener.enterBrand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrand" ):
                listener.exitBrand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrand" ):
                return visitor.visitBrand(self)
            else:
                return visitor.visitChildren(self)



    def filter_(self):

        localctx = QueryParser.FilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filter)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = QueryParser.BrandContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(QueryParser.BRAND)
                pass
            elif token in [4]:
                localctx = QueryParser.CountryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(QueryParser.COUNTRY)
                pass
            elif token in [5]:
                localctx = QueryParser.StyleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(QueryParser.STYLE)
                pass
            elif token in [6]:
                localctx = QueryParser.VarietyContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.match(QueryParser.VARIETY)
                pass
            elif token in [7]:
                localctx = QueryParser.StarsContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.match(QueryParser.STARS)
                pass
            elif token in [8]:
                localctx = QueryParser.TopTenContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.match(QueryParser.TOPTEN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_val

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(QueryParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(QueryParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def val(self):

        localctx = QueryParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_val)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = QueryParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(QueryParser.ID)
                pass
            elif token in [16]:
                localctx = QueryParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(QueryParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






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
        4,1,13,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,3,1,3,3,3,31,8,3,1,3,0,0,4,0,2,4,6,0,2,1,0,1,2,1,0,3,8,32,
        0,9,1,0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,6,30,1,0,0,0,8,10,3,2,1,0,
        9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,
        0,13,14,3,4,2,0,14,15,7,0,0,0,15,16,3,4,2,0,16,17,5,11,0,0,17,23,
        1,0,0,0,18,19,3,4,2,0,19,20,5,11,0,0,20,23,1,0,0,0,21,23,5,11,0,
        0,22,13,1,0,0,0,22,18,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,
        9,0,0,25,26,7,1,0,0,26,27,3,6,3,0,27,5,1,0,0,0,28,31,5,9,0,0,29,
        31,5,10,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,7,1,0,0,0,3,11,22,30
    ]

class QueryParser ( Parser ):

    grammarFileName = "Query.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'AND'", "'OR'", "'=='", "'<'", "'>'", 
                     "'<='", "'>='", "'!='" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "EQ", "LT", "GT", "LTEQ", 
                      "GTEQ", "NEQ", "ID", "INT", "NEWLINE", "WS", "ANY" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_expr = 2
    RULE_val = 3

    ruleNames =  [ "prog", "command", "expr", "val" ]

    EOF = Token.EOF
    AND=1
    OR=2
    EQ=3
    LT=4
    GT=5
    LTEQ=6
    GTEQ=7
    NEQ=8
    ID=9
    INT=10
    NEWLINE=11
    WS=12
    ANY=13

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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.command()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==11):
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
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = QueryParser.PrintJoinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr()
                self.state = 14
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 15
                self.expr()
                self.state = 16
                self.match(QueryParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = QueryParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.expr()
                self.state = 19
                self.match(QueryParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = QueryParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
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

        def ID(self):
            return self.getToken(QueryParser.ID, 0)
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
            self.state = 24
            self.match(QueryParser.ID)
            self.state = 25
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 26
            self.val()
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
        self.enterRule(localctx, 6, self.RULE_val)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = QueryParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(QueryParser.ID)
                pass
            elif token in [10]:
                localctx = QueryParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
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






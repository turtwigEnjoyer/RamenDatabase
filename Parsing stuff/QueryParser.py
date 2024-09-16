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
        4,1,13,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        5,2,28,8,2,10,2,12,2,31,9,2,1,3,1,3,3,3,35,8,3,1,3,0,1,4,4,0,2,4,
        6,0,2,1,0,8,13,1,0,1,2,36,0,9,1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,0,
        6,34,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,
        11,12,1,0,0,0,12,1,1,0,0,0,13,14,3,4,2,0,14,15,5,5,0,0,15,18,1,0,
        0,0,16,18,5,5,0,0,17,13,1,0,0,0,17,16,1,0,0,0,18,3,1,0,0,0,19,20,
        6,2,-1,0,20,21,3,6,3,0,21,22,7,0,0,0,22,23,3,6,3,0,23,29,1,0,0,0,
        24,25,10,1,0,0,25,26,7,1,0,0,26,28,3,4,2,2,27,24,1,0,0,0,28,31,1,
        0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,5,1,0,0,0,31,29,1,0,0,0,32,
        35,5,3,0,0,33,35,5,4,0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,7,1,0,0,
        0,4,11,17,29,34
    ]

class QueryParser ( Parser ):

    grammarFileName = "Query.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'AND'", "'OR'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'=='", "'<'", 
                     "'>'", "'<='", "'>='", "'!='" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "ID", "INT", "NEWLINE", 
                      "WS", "ANY", "EQ", "LT", "GT", "LTEQ", "GTEQ", "NEQ" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_expr = 2
    RULE_identifier = 3

    ruleNames =  [ "prog", "command", "expr", "identifier" ]

    EOF = Token.EOF
    AND=1
    OR=2
    ID=3
    INT=4
    NEWLINE=5
    WS=6
    ANY=7
    EQ=8
    LT=9
    GT=10
    LTEQ=11
    GTEQ=12
    NEQ=13

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                localctx = QueryParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(QueryParser.NEWLINE)
                pass
            elif token in [5]:
                localctx = QueryParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(QueryParser.NEWLINE)
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(QueryParser.IdentifierContext,i)

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


    class JoinContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.ExprContext)
            else:
                return self.getTypedRuleContext(QueryParser.ExprContext,i)

        def AND(self):
            return self.getToken(QueryParser.AND, 0)
        def OR(self):
            return self.getToken(QueryParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin" ):
                listener.enterJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin" ):
                listener.exitJoin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoin" ):
                return visitor.visitJoin(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = QueryParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = QueryParser.CompareContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 20
            self.identifier()
            self.state = 21
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 22
            self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QueryParser.JoinContext(self, QueryParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 24
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 25
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 26
                    self.expr(2) 
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_identifier

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ValContext(IdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.IdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(QueryParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVal" ):
                listener.enterVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVal" ):
                listener.exitVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal" ):
                return visitor.visitVal(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(IdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QueryParser.IdentifierContext
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



    def identifier(self):

        localctx = QueryParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifier)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = QueryParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(QueryParser.ID)
                pass
            elif token in [4]:
                localctx = QueryParser.ValContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         





# Generated from C:/Users/jackk/OneDrive/College/Fall Semester 2024/CS3050/RamenDatabase/Parsing stuff/Query.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,19,131,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,
        0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,
        10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,4,13,98,8,13,11,13,12,
        13,99,1,13,3,13,103,8,13,1,14,4,14,106,8,14,11,14,12,14,107,1,15,
        3,15,111,8,15,1,15,1,15,1,16,4,16,116,8,16,11,16,12,16,117,1,16,
        1,16,1,17,1,17,1,18,1,18,4,18,126,8,18,11,18,12,18,127,1,18,1,18,
        0,0,19,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,
        25,13,27,14,29,15,31,16,33,17,35,18,37,19,1,0,4,2,0,65,90,97,122,
        1,0,48,57,2,0,9,9,32,32,3,0,32,32,65,90,97,122,136,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,
        1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,1,39,1,0,0,0,3,43,1,0,0,0,5,46,
        1,0,0,0,7,52,1,0,0,0,9,60,1,0,0,0,11,66,1,0,0,0,13,74,1,0,0,0,15,
        80,1,0,0,0,17,83,1,0,0,0,19,85,1,0,0,0,21,87,1,0,0,0,23,90,1,0,0,
        0,25,93,1,0,0,0,27,102,1,0,0,0,29,105,1,0,0,0,31,110,1,0,0,0,33,
        115,1,0,0,0,35,121,1,0,0,0,37,123,1,0,0,0,39,40,5,65,0,0,40,41,5,
        78,0,0,41,42,5,68,0,0,42,2,1,0,0,0,43,44,5,79,0,0,44,45,5,82,0,0,
        45,4,1,0,0,0,46,47,5,66,0,0,47,48,5,114,0,0,48,49,5,97,0,0,49,50,
        5,110,0,0,50,51,5,100,0,0,51,6,1,0,0,0,52,53,5,67,0,0,53,54,5,111,
        0,0,54,55,5,117,0,0,55,56,5,110,0,0,56,57,5,116,0,0,57,58,5,114,
        0,0,58,59,5,121,0,0,59,8,1,0,0,0,60,61,5,83,0,0,61,62,5,116,0,0,
        62,63,5,121,0,0,63,64,5,108,0,0,64,65,5,101,0,0,65,10,1,0,0,0,66,
        67,5,86,0,0,67,68,5,97,0,0,68,69,5,114,0,0,69,70,5,105,0,0,70,71,
        5,101,0,0,71,72,5,116,0,0,72,73,5,121,0,0,73,12,1,0,0,0,74,75,5,
        83,0,0,75,76,5,116,0,0,76,77,5,97,0,0,77,78,5,114,0,0,78,79,5,115,
        0,0,79,14,1,0,0,0,80,81,5,61,0,0,81,82,5,61,0,0,82,16,1,0,0,0,83,
        84,5,60,0,0,84,18,1,0,0,0,85,86,5,62,0,0,86,20,1,0,0,0,87,88,5,60,
        0,0,88,89,5,61,0,0,89,22,1,0,0,0,90,91,5,62,0,0,91,92,5,61,0,0,92,
        24,1,0,0,0,93,94,5,33,0,0,94,95,5,61,0,0,95,26,1,0,0,0,96,98,7,0,
        0,0,97,96,1,0,0,0,98,99,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,
        103,1,0,0,0,101,103,3,37,18,0,102,97,1,0,0,0,102,101,1,0,0,0,103,
        28,1,0,0,0,104,106,7,1,0,0,105,104,1,0,0,0,106,107,1,0,0,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,30,1,0,0,0,109,111,5,13,0,0,110,109,
        1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,5,10,0,0,113,32,
        1,0,0,0,114,116,7,2,0,0,115,114,1,0,0,0,116,117,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,6,16,0,0,120,34,
        1,0,0,0,121,122,9,0,0,0,122,36,1,0,0,0,123,125,5,34,0,0,124,126,
        7,3,0,0,125,124,1,0,0,0,126,127,1,0,0,0,127,125,1,0,0,0,127,128,
        1,0,0,0,128,129,1,0,0,0,129,130,5,34,0,0,130,38,1,0,0,0,7,0,99,102,
        107,110,117,127,1,6,0,0
    ]

class QueryLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AND = 1
    OR = 2
    BRAND = 3
    COUNTRY = 4
    STYLE = 5
    VARIETY = 6
    STARS = 7
    EQ = 8
    LT = 9
    GT = 10
    LTEQ = 11
    GTEQ = 12
    NEQ = 13
    ID = 14
    INT = 15
    NEWLINE = 16
    WS = 17
    ANY = 18
    QUOTED_ID = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'AND'", "'OR'", "'Brand'", "'Country'", "'Style'", "'Variety'", 
            "'Stars'", "'=='", "'<'", "'>'", "'<='", "'>='", "'!='" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "BRAND", "COUNTRY", "STYLE", "VARIETY", "STARS", 
            "EQ", "LT", "GT", "LTEQ", "GTEQ", "NEQ", "ID", "INT", "NEWLINE", 
            "WS", "ANY", "QUOTED_ID" ]

    ruleNames = [ "AND", "OR", "BRAND", "COUNTRY", "STYLE", "VARIETY", "STARS", 
                  "EQ", "LT", "GT", "LTEQ", "GTEQ", "NEQ", "ID", "INT", 
                  "NEWLINE", "WS", "ANY", "QUOTED_ID" ]

    grammarFileName = "Query.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



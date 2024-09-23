grammar Query;

options {
    language = Python3;
}

prog: command+ ;

command: expr op=(AND | OR) expr NEWLINE    #printJoin
       | expr NEWLINE                       #printExpr
       | NEWLINE        #blank
       ;

expr: ID op=('==' | '<' | '>' | '<=' | '>=' | '!=') val #compare
    ;

val: ID        #id
   | INT       #int
   ;

AND: 'AND';
OR: 'OR';

EQ: '==';
LT: '<';
GT: '>';
LTEQ: '<=';
GTEQ: '>=';
NEQ: '!=';

ID : [a-zA-Z]+ | QUOTED_ID ;
INT: [0-9]+ ;
NEWLINE : '\r'? '\n' ;
WS : [ \t]+ -> skip ;
ANY: . ;

QUOTED_ID : '"' [a-zA-Z ]+ '"' ;

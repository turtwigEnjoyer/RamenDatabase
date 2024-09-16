grammar Query;

options {
    language = Python3;
}

prog: command+ ;

command: expr NEWLINE   #printExpr
       | NEWLINE        #blank
       ;

expr: identifier op=('==' | '<' | '>' | '<=' | '>=' | '!=') identifier #compare
    | expr op=(AND | OR) expr                                          #join
    ;

identifier:  ID          #id
          | INT          #val
          ;

AND: 'AND';
OR: 'OR';

EQ: '==';
LT: '<';
GT: '>';
LTEQ: '<=';
GTEQ: '>=';
NEQ: '!=';

ID : [a-zA-Z]+ ;
INT: [0-9]+ ;
NEWLINE : '\r'? '\n' ;
WS : [ \t]+ -> skip ;
ANY: . ;


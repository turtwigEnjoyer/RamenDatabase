grammar Query;

options {
    language = Python3;
}

prog: command+ ;

command: expr op=(AND | OR) expr NEWLINE    #printJoin
       | expr NEWLINE                       #printExpr
       | NEWLINE        #blank
       ;

expr: filter op=('==' | '<' | '>' | '<=' | '>=' | '!=') val #compare
    ;

filter: BRAND          #brand
      | COUNTRY        #country
      | STYLE          #style
      | VARIETY         #variety
      | STARS           #stars
      ;

val: ID        #id
   | INT       #int
   ;

AND: 'AND';
OR: 'OR';

BRAND: 'Brand';
COUNTRY: 'Country';
STYLE: 'Style';
VARIETY: 'Variety';
STARS: 'Stars';

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

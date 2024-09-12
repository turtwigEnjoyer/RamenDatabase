Parser team

* Can be tokenized (take string separate by whitespace) (“cost” then we know we are looking at the cost) (calories, style, type)
* Parsing the user input 
* Can use py parse 

Query language:

Brand + Country + Style + Variety + Stars

Country + Style 
> Japan + Pack

> Samyang Foods + South Korea + Pack + Kimchi + > 4.0

> KOKA + Bowl + > 4.0

Stars + Variety
> 5.0 + Spicy Ramen

parse the string for 'Variety' by whitespace, then match with strings in database

help:

Choose how you would like to filter the reviews. 

You can select one or more of these filters:
Brand + Country + Style + Variety + Stars 

ANTLR How to:
- install plugin to pycharm
- make sure to install the antlr-python3-runtime file which I can add to repo
- add it to the interpreter section of the project
- should be setup from there on

steps
- build grammar (grammar is used to define the query language we are making -> it is generated into a lexer, parser, and visitor template)
- build visitor ( visitor is what communicates with the parser) - we will be building over the template to make use of the data the way we want to
- build interface that user will interact with that will send commands to parser
- then work on communication between the database and command collection interface

adding useful antlr and python links:
- https://github.com/RutledgePaulV/rsql-parser-python/blob/master/rsql_python/query.py
- https://medium.com/@ab.rhmn97/build-an-api-query-language-with-antlr-in-python-7313dba222e7



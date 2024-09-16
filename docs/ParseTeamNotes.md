> Query language:

The user can specify how they want to filter/search through the ramen reviews by using the '+' symbol to combine filters (only up to two filters allowed at a time). 
Available filters/keywords that the user can use are: 'Brand', 'Country', 'Style', 'Variety', and 'Stars'


* Country + Style 
* Japan + Pack


* Brand + Variety
* Samyang Foods + Kimchi

* Stars + Variety
* = 5.0 + Spicy Ramen
  
* Country + Stars
* Japan + > 4.0


We will parse the string for 'Variety' by whitespace, then match with strings in database

> help:

Choose how you would like to filter the reviews. You can select one or more of these filters:
Brand + Country + Style + Variety + Stars 

(column, operation, value)



> Query engine:

this function is defined in the QueryEngine and called within the Parser
function will be able to handle compound queries as well


processQuery(filterType, comparisonType, queryInput) {
	return list of DB values that fit the query
}

* filterType: 'Brand' or 'Country' or 'Style' etc. 
* comparisonType: ==, >, <, !=
* queryInput: the actual typed stuff

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

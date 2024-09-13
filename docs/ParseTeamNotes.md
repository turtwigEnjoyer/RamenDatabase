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

# The Ramen Database Project
Warm up project for CS3050 Software Engineering.

Created by: Zoe Bell, Bradon Soucy, Jack Klug, and Nora Garcia

## Necessary packages

``` pip install antlr4-python3-runtime ```

``` pip install google-cloud-firestore ```

``` pip install firebase-admin ```

## How to Run

This program has two executables:

[QueryEngine](./Parsing/QueryEngine.py) is the main executable for our program. It should be executed from the root directory.
This program takes in queries with a language such as:

``` Field == Value ```

``` E.g. Country == Japan```

We can run queries compounded on two fields such as:

``` Field1 == Value1 AND Field2 >= Value2 ```

``` E.g. Country == Japan AND Stars >= 3.5```

Please note that string fields will only produce queries on equality

[Admin Insertion Program](./Main/DbInsertionEngine.py) is the admin insertion program.
It will delete all data from the database and reinsert the data from the given JSON file.

Our current JSON file is located in [here](./files/ramen_ratings_short.json)

## Description of Data
* Source: https://www.kaggle.com/datasets/residentmario/ramen-ratings
* Id: unique identifier for the review
* Brand: brand name of the ramen
* Variety: name of the product
* Style: how the ramen is sold(cup, bowl, tray, etc)
* Country: where the ramen is from
* Stars: indication of the ramen quality on a 5-point scale
* TopTen: Boolean to indicate whether it is classified as top ten
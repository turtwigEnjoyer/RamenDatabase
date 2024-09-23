# The Ramen Database Project
Warm up project for CS3050 Software Engineering.

Created by: Zoe Bell, Bradon Soucy, Jack Klug, and Nora Garcia

Here we should write about our development plan, instructions and documentation to keep track of what others are doing.
- Firebase documentation and notes will be [here](docs/Firebase.md)

## Necessary packages

``` pip install antlr4-python3-runtime ```

``` pip install google-cloud-firestore ```

``` pip install firebase-admin ```

    

## Description of Data
* Source: https://www.kaggle.com/datasets/residentmario/ramen-ratings
* Review number: unique identifier for the review
* Brand: brand name of the ramen
* Variety: name of the product
* Style: how the ramen is sold(cup, bowl, tray, etc)
* Country: where the ramen is from
* Stars: indication of the ramen quality on a 5-point scale

## Formatting
For code formatting I (Nora) propose pep8 formatting. I think Pycharm defaults to this formatting so it might be most useful. 

I'm using [the autopep8 extension](https://marketplace-visualstudio-com.translate.goog/items?itemName=ms-python.autopep8&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sc) on VS code 
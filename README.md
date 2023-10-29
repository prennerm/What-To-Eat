# What To Eat
#### Video Demo: https://youtu.be/hupp69ShO4Y
#### Description
What To Eat is Marwin Prenner's Final Project for the Harvard course CS50x 2023. This project is a flask application, combined with a SQL script that is supposed to return an assortment of different food options based on the amount of time the user has at their disposal as well as vegetarian, vegan and kosher preferences and wether or not the user is looking for hot or cold food.
Once the user has decided what option they will be going for, they can use the provided link to find out detailed instructions on the dish from an external website.
Furthermore the user is enabled to add new recipes by putting in the name of the dish, the amount of time the preparation takes, wether or not the dish is vegetarian, vegan, kosher and to be served hot or cold. As well as take a look at all the available recipes on external homepages.

Benefits of the different files:

app.py: Contains the Python code that creates the webpage and stores and operates the different functions that are necessary for the use case of this project to run (searching or adding recipes). This file contains the following functions: all_recipes(), search(), search_results(), show_recipe(), add(), index(), get_db().

The most important functions will be described in more detail:

all_recipes(): will be called as soon as the user chooses the option "all_recipes". Then a SQL statement is called, that returns all information stored in both tables, except for the id (which is only there for joining the two tables and would not provide any benefit to the user, if shown)

search_results(): When the user opens "search" on the website, they will be prompted to put in the different parameters. The SQL query is built in such a way that it will always work no matter how little input the user provides, meaning that if they left all input fields blank, the query would just return all recipes.

add(): Perhaps the most intriguing function. It allows the user to expand upon the 20 dishes that are originally part of this project by however many dishes they want. Built similarly to the query that is used as part of the search_results() function, the user is prompted to provide the name, the different characteristics and a URL.

recipes.sqlite: Creates the two tables recipe_names and characteristics. Stores 20 different dish descriptions within these two tables in the following way: recipe_names contains the id that the two tables will be joined on when the user searches for recipes that fulfill certain criteria, the name of the dish and the url of the detailed recipe. The second table characteristics contains the same id, the time that is stored for a certain recipe and in the form of BIT, the boolean value for vegetarian, vegan, kosher and hot.

add.html, all_recipes.html, index.html, layout.html, search_results.html, search.html, styles.css: necessary for all the different pages of the web application to run.
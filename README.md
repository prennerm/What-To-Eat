# What To Eat
#### Video Demo: https://youtu.be/hupp69ShO4Y
#### Description
What To Eat is Marwin Prenner's Final Project for the Harvard course CS50x 2023. This project is a flask application, combined with a SQL script that is supposed to return an assortment of different food options based on the amount of time the user has at their disposal as well as vegetarian, vegan and kosher preferences and wether or not the user is looking for hot or cold food.
Once the user has decided what option they will be going for, they can use the provided link to find out detailed instructions on the dish from an external website.
Furthermore the user is enabled to add new recipes by putting in the name of the dish, the amount of time the preparation takes, wether or not the dish is vegetarian, vegan, kosher and to be served hot or cold. Also well as take a look at all the available recipes.

Benefits of the different files:

app.py: Contains the Python code that creates the webpage and stores and operates the different functions that are necessary for the use case of this project to run (searching or adding recipes).
recipes.sqlite: Creates the two tables recipe_names and characteristics. Stores 20 different dish descriptions.
add.html, all_recipes.html, index.html, layout.html, search_results.html, search.html, styles.css: necessary for all the different pages of the web application to run.
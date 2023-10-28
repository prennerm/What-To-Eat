from flask import Flask, render_template, g, request

import sqlite3

DATABASE = "recipes"

app = Flask(__name__)


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route("/")
def index():
    return render_template("index.html")


# method to show all recipes
@app.route("/all_recipes")
def all_recipes():
    connection = get_db().cursor()
    recipes = connection.execute(
        "SELECT r.name, c.time, c.vegetarian, c.vegan, c.kosher, c.hot, r.url FROM recipe_names r JOIN characteristics c ON r.id = c.recipe_id;"
    ).fetchall()
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html")


# method to show the search results
@app.route("/search_results", methods=["POST"])
def search_results():
    time = request.form.get("time")
    vegetarian = request.form.get("vegetarian")
    vegan = request.form.get("vegan")
    kosher = request.form.get("kosher")
    hot = request.form.get("hot")

    query = "SELECT r.name, c.time, c.vegetarian, c.vegan, c.kosher, c.hot, r.url FROM recipe_names r JOIN characteristics c ON r.id = c.recipe_id WHERE c.time <= ?"
    params = [time]

    if vegetarian:
        query += " AND c.vegetarian = ?"
        params.append(1)
    if vegan:
        query += " AND c.vegan = ?"
        params.append(1)
    if kosher:
        query += " AND c.kosher = ?"
        params.append(1)
    if hot:
        query += " AND c.hot = ?"
        params.append(1)

    connection = get_db().cursor()
    matching_recipes = connection.execute(query, params).fetchall()
    print(matching_recipes)
    return render_template("search_results.html", recipes=matching_recipes)


# method to show a recipe
@app.route("/show_recipe/<id>")
def show_recipe(id):
    return render_template("all_recipes.html")


# method to add a recipe to the database
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        url = request.form.get("url")
        time = request.form.get("time")
        vegetarian = request.form.get("vegetarian")
        vegan = request.form.get("vegan")
        kosher = request.form.get("kosher")
        hot = request.form.get("hot")
        connection = get_db()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "insert into recipe_names(name, url) values (?, ?)",
                (name, url),
            )
            last_id = cursor.lastrowid
            cursor.execute(
                "insert into characteristics(recipe_id, time, vegetarian, vegan, kosher, hot) VALUES(?, ?, ?, ?, ?, ?)",
                (last_id, time, vegetarian, vegan, kosher, hot),
            )
            connection.commit()
        except Exception as ex:
            return render_template(
                "add.html",
                message=f"Are you sure, that you put in all the necessary information about your favourite recipe?<br />{ex}",
            )
        return render_template("add.html", message=f"Recipe {name} added!")
    else:
        return render_template("add.html", message=None)

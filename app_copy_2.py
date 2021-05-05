import os
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/")
@app.route("/get_stories")
def get_stories():
    stories = list(mongo.db.stories.find())
    return render_template("blockbusters.html", stories=stories)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    stories = list(mongo.db.stories.find({"$text": {"$search": query}}))
    return render_template("blockbusters.html", stories=stories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check whether username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, that Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("add_story", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check for existing username in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure the hashed password matches the user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "add_story", username=session["user"]))
            else:
                # invalid password match
                flash("Sorry - incorrect Password and/or Username")
                return redirect(url_for("login"))

        else:
            # username not valid
            flash("Sorry - incorrect Password and/or Username")
            return redirect(url_for("login"))
    
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    # remove user session from cookies
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_story", methods=["GET", "POST"])
def add_story():
    if request.method == "POST":
        story = {
            "title_name": request.form.get("title_name"),
            "genre_name": request.form.get("genre_name"),
            "character_name": request.form.get("character_name"),
            "plot_name": request.form.get("plot_name"),
            "resolution_name": request.form.get("resolution_name"),
            "setting_name": request.form.get("setting_name"),
            "cast_name": request.form.getlist("cast_name"),
            "cast_url": request.form.getlist("cast_url"),
            "created_by":  session["user"]
        }
        mongo.db.stories.insert_one(story)
        flash("Block+Buster Built!")
        return redirect(url_for("get_stories"))

    characters = mongo.db.character.find().sort("character_name", 1)
    plots = mongo.db.plot.find().sort("plot_name", 1)
    resolutions = mongo.db.resolution.find().sort("resolution_name", 1)
    settings = mongo.db.setting.find().sort("setting_name", 1)
    genres = mongo.db.genres.find().sort("genre_name", 1)
    casts = mongo.db.cast.find().sort("cast_name", 1)
    casturls = mongo.db.cast.find().sort("cast_url", 1)
    return render_template("add_story.html", genres=genres, characters=characters, plots=plots, resolutions=resolutions, settings=settings, casts=casts, casturls=casturls)


@app.route("/edit_story/<story_id>/", methods=["GET", "POST"])
def edit_story(story_id):
    if request.method == "POST":
        submit = {
            "title_name": request.form.get("title_name"),
            "genre_name": request.form.get("genre_name"),
            "character_name": request.form.get("character_name"),
            "plot_name": request.form.get("plot_name"),
            "resolution_name": request.form.get("resolution_name"),
            "setting_name": request.form.get("setting_name"),
            "cast_name": request.form.get("cast_name"),
            "cast_url": request.form.get("cast_url"),
            "created_by":  session["user"]
        }
        mongo.db.stories.update({"_id": ObjectId(story_id)}, submit)
        flash("Block+Buster Updated!")
    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})

    characters = mongo.db.character.find().sort("character_name", 1)
    plots = mongo.db.plot.find().sort("plot_name", 1)
    resolutions = mongo.db.resolution.find().sort("resolution_name", 1)
    settings = mongo.db.setting.find().sort("setting_name", 1)
    genres = mongo.db.genres.find().sort("genre_name", 1)
    casts = mongo.db.cast.find().sort("cast_name", 1)
    casturls = mongo.db.cast.find().sort("cast_url", 1)
    return render_template("edit_story.html", story=story, genres=genres, characters=characters, plots=plots, resolutions=resolutions, settings=settings, casts=casts, casturls=casturls)


@app.route("/delete_story/<story_id>")
def delete_story(story_id):
    mongo.db.stories.remove({"_id": ObjectId(story_id)})
    flash("Block+Buster Deleted")
    return redirect(url_for("get_stories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
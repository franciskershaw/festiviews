import os
from flask import (
    Flask, render_template, request,
    flash, redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        # check if username has already been taken by another user
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password_1"))
        }
        mongo.db.users.insert_one(sign_up)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("favourites", username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Signed in as {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "favourites", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/favourites/<username>", methods=["GET", "POST"])
def favourites(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session['user']:
        return render_template("favourites.html", username=username)

    return redirect(url_for('login'))


@app.route('/browse')
def browse():
    festivals = list(mongo.db.festivals.find().sort('name', 1))
    return render_template('browse.html', festivals=festivals)


@app.route("/view_festival/<festival_id>")
def view_festival(festival_id):
    festival = mongo.db.festivals.find_one({"_id": ObjectId(festival_id)})

    return render_template("view_festival.html",
                           festival=festival)


@app.route('/add_festival', methods=['GET', 'POST'])
def add_festival():
    if request.method == 'POST':
        add_festival = {
            "name": request.form.get("festival_name"),
            "location": request.form.get("festival_location"),
            "start_date": request.form.get('festival_start_date'),
            "end_date": request.form.get('festival_end_date')
        }
        mongo.db.festivals.insert_one(add_festival)

        return redirect(url_for("browse"))

    return render_template("add_festival.html")


@app.route('/logout')
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        # DON'T FORGET TO CHANGE THIS TO FALSE BEFORE SUBMISSION
        debug=True
    )

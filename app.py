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


@app.route("/view_festival/<url>")
def view_festival(url):
    festival = mongo.db.festivals.find_one({"url": url})
    festival_id = festival['_id']
    reviews = mongo.db.reviews.find({"festival_id": ObjectId(festival_id)})

    reviews_arr = []

    for review in reviews:
        reviews_arr.append(review)

    return render_template("view_festival.html",
                           festival=festival,
                           reviews_arr=reviews_arr)


@app.route('/add_festival', methods=['GET', 'POST'])
def add_festival():
    if request.method == 'POST':
        add_festival = {
            "name": request.form.get("festival_name"),
            "url": request.form.get("festival_name").lower().replace(' ', '_'),
            "location": request.form.get("festival_location"),
            "start_date": request.form.get('festival_start_date'),
            "end_date": request.form.get('festival_end_date'),
            "genre": request.form.get('festival_genre'),
            "capacity": request.form.get('festival_capacity'),
            "notable_act_one": request.form.get('festival_headliner_1'),
            "notable_act_two": request.form.get('festival_headliner_2'),
            "notable_act_three": request.form.get('festival_headliner_3'),
            "website": request.form.get('festival_website'),
            "ticket_price": request.form.get('festival_price'),
            "ticket_link": request.form.get('festival_ticket_link'),
            "image_link": request.form.get('festival_image'),
            "description": request.form.get('festival_description'),
            "reviews": []
        }
        mongo.db.festivals.insert_one(add_festival)

        return redirect(url_for("browse"))

    return render_template("add_festival.html")


@app.route('/edit_festival/<url>', methods=["GET", "POST"])
def edit_festival(url):
    if request.method == 'POST':
        mongo.db.festivals.update_one(
            {"url": url},
            {"$set": {"name": request.form.get("festival_name"),
                      "url": request.form.get(
                          "festival_name").lower().replace(' ', '_'),
                      "location": request.form.get("festival_location"),
                      "start_date": request.form.get('festival_start_date'),
                      "end_date": request.form.get('festival_end_date'),
                      "genre": request.form.get('festival_genre'),
                      "capacity": request.form.get('festival_capacity'),
                      "notable_act_one": request.form.get(
                          'festival_headliner_1'),
                      "notable_act_two": request.form.get(
                          'festival_headliner_2'),
                      "notable_act_three": request.form.get(
                          'festival_headliner_3'),
                      "website": request.form.get('festival_website'),
                      "ticket_price": request.form.get('festival_price'),
                      "ticket_link": request.form.get('festival_ticket_link'),
                      "image_link": request.form.get('festival_image'),
                      "description": request.form.get(
                          'festival_description')}})

        flash('Festival updated')
        return redirect(url_for('view_festival', url=url))

    festival = mongo.db.festivals.find_one({'url': url})
    return render_template("edit_festival.html", festival=festival)


@app.route('/delete_festival/<url>')
def delete_festival(url):
    festival = mongo.db.find_one({'url': url})
    festival_id = festival['_id']
    # delete festival from database
    mongo.db.festivals.delete_one({"url": url})
    # delete corresponding reviews from reviews database
    mongo.db.reviews.delete_many({'festival_id': ObjectId(festival_id)})
    flash("Festival and corresponding reviews deleted")
    return redirect(url_for('browse'))


@app.route('/add_review/<url>', methods=['GET', 'POST'])
def add_review(url):
    festival = mongo.db.festivals.find_one({'url': url})
    festival_id = festival['_id']
    if request.method == 'POST':
        # Grab form data from form
        review = {
            "created_by": session['user'],
            "festival_id": festival_id,
            "year": request.form.get('year'),
            "rating": request.form.get('rating'),
            "location": request.form.get('location'),
            "nightlife": request.form.get('nightlife'),
            "lineup": request.form.get('lineup'),
            "campsites": request.form.get('campsites'),
            "value": request.form.get('value'),
            "food": request.form.get('food'),
            "toilets": request.form.get('toilets'),
            "kid_friendly": request.form.get('kid_friendly'),
            "text": request.form.get('review')
        }

        review_id = mongo.db.reviews.insert_one(review)
        mongo.db.festivals.update_one(
            {"url": url},
            {'$push': {'reviews': review_id.inserted_id}})

        flash('Review added!')
        return redirect(url_for('view_festival', url=url))

    return render_template('add_review.html', festival=festival)


@app.route('/edit_review/<review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    festival_id = review['festival_id']
    if request.method == 'POST':
        mongo.db.reviews.update_one(
            {"_id": ObjectId(review_id)},
            {"$set": {"year": request.form.get('year'),
                      "rating": request.form.get('rating'),
                      "location": request.form.get('location'),
                      "nightlife": request.form.get('nightlife'),
                      "lineup": request.form.get('lineup'),
                      "campsites": request.form.get('campsites'),
                      "value": request.form.get('value'),
                      "food": request.form.get('food'),
                      "toilets": request.form.get('toilets'),
                      "kid_friendly": request.form.get('kid_friendly'),
                      "text": request.form.get('review')}})

        flash('Review has been updated')
        return redirect(url_for('view_festival', festival_id=festival_id))

    return render_template('edit_review.html',
                           review=review)


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    festival_id = review['festival_id']
    print(review)
    # delete review from database
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    # delete review id from festivals database
    mongo.db.festivals.update_one({"_id": ObjectId(festival_id)},
                                  {'$pull': {'reviews': ObjectId(review_id)}})
    flash("Review deleted")
    return redirect(url_for('browse'))


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

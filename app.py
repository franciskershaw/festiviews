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
    """
    This function is for the creation of an account, it checks
    if the username has been taken, checks that the password and
    confirmation passwords match, and either flashes error
    messages or adds a new user to the database, redirecting to
    the user's new 'favourites' page.
    """
    if request.method == "POST":
        # check if username has already been taken by another user
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        password_1 = request.form.get("password_1")
        password_2 = request.form.get("password_2")

        if existing_user:
            flash("Username already exists, please a different one")
            return redirect(url_for("sign_up"))

        # check if password_1 and password_2 match
        if password_1 != password_2:
            flash("Passwords do not match")
            return redirect(url_for("sign_up"))

        # add user to datatbase
        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(password_1),
            "favourites": []
        }
        mongo.db.users.insert_one(sign_up)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("favourites", username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This function is for users logging in, it checks that the
    submited username exists, then checks that the password
    matches what's on the database, and either logs in successfuly
    by redirecting to the user's 'favourites' page, or flashes an
    error.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check that the password is correct
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
    """
    This function finds the user's favourited festivals (if
    there are any), sorts them alphabetically, appends them
    into an array that can be accessed on the front end, and
    renders the template for the favourites page.

    GET = render template for login.html
    POST = render template for favourites.html
    """
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    username = user['username']
    # sort favourites alphabetically
    favourites = mongo.db.festivals.find(
        {"favourited_by": username}).sort([('name', 1)])

    favourites_arr = []

    # loop over favourites and append them to array
    for favourite in favourites:
        favourites_arr.append(favourite)

    # check user is logged in
    if session['user']:
        return render_template("favourites.html",
                               username=username,
                               favourites=favourites,
                               favourites_arr=favourites_arr)

    # if not logged in, redirect to login page
    return redirect(url_for('login'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    This function allows users to use the search bar from anywhere
    on the site, and sorts results alphabetically on the browse
    page.
    """
    query = request.form.get('search_bar')
    festivals = list(mongo.db.festivals.find(
        {"$text": {"$search": query}}).sort('name', 1))

    return render_template('browse.html', festivals=festivals)


@app.route('/browse')
def browse():
    """
    This function finds all available festivals from the db and
    renders them alphabetically on the browse all page.
    """
    festivals = list(mongo.db.festivals.find().sort('name', 1))
    return render_template('browse.html', festivals=festivals)


@app.route("/view_festival/<url>")
def view_festival(url):
    """
    This function relates to the rendering of the indivdiual
    festival 'hubs'. It also finds and sorts any reviews present by
    order for most recently uploaded, appends them to an array that
    can be accessed on the front end, and renders the view_festival
    template.
    """
    festival = mongo.db.festivals.find_one({"url": url})
    festival_id = festival['_id']
    # sort reviews by _id (most recent first)
    reviews = mongo.db.reviews.find(
        {"festival_id": ObjectId(festival_id)}).sort([('_id', 1), ('_id', -1)])

    reviews_arr = []

    # loop over the reviews and append them to reviews_arr
    for review in reviews:
        reviews_arr.append(review)

    return render_template("view_festival.html",
                           festival=festival,
                           reviews_arr=reviews_arr)


@app.route('/add_festival', methods=['GET', 'POST'])
def add_festival():
    """
    This function allows administrators only to create a new festival
    'hub' that users can add reviews for. It pulls all the information
    from the form on add_festival.html.
    """
    user = session['user']
    if request.method == 'POST':
        # create a valid url from based off of the festival name
        url = request.form.get("festival_name").lower().replace(' ', '_')
        # grab data from form
        add_festival = {
            "name": request.form.get("festival_name"),
            "url": url,
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
            "covid_status": request.form.get('covid_status'),
            "reviews": [],
            "favourited_by": []
        }
        # add all the details above to the database
        mongo.db.festivals.insert_one(add_festival)

        flash('New festival added')
        return redirect(url_for("view_festival", url=url))

    if user == 'administrator':
        return render_template("add_festival.html")
    else:
        flash("Sorry, you can't access this area")
        return redirect(url_for('browse'))


@app.route('/edit_festival/<url>', methods=["GET", "POST"])
def edit_festival(url):
    """
    This function allows administrators only to edit a previously
    created festival, ensuring that if name of the festival is
    changed then the url is updated accordingly.
    """
    if request.method == 'POST':
        new_url = request.form.get(
                          "festival_name").lower().replace(' ', '_')
        # grab data and update the festival on the db
        mongo.db.festivals.update_one(
            {"url": url},
            {"$set": {"name": request.form.get("festival_name"),
                      "url": new_url,
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
                          'festival_description'),
                      "covid_status": request.form.get('covid_status')}})
        flash('Festival updated')
        return redirect(url_for('view_festival', url=new_url))

    festival = mongo.db.festivals.find_one({'url': url})
    return render_template("edit_festival.html", festival=festival)


@app.route('/delete_festival/<url>')
def delete_festival(url):
    """
    This function allows administrators only to delete previously
    created festivals from the site and database. It also deletes
    any associated reviews from the reviews collection.
    """
    # find festival
    festival = mongo.db.festivals.find_one({'url': url})
    festival_id = festival['_id']
    # delete festival from database
    mongo.db.festivals.delete_one({"url": url})
    # delete corresponding reviews from reviews database
    mongo.db.reviews.delete_many({'festival_id': ObjectId(festival_id)})

    flash("Festival and corresponding reviews deleted")
    return redirect(url_for('browse'))


@app.route('/add_review/<url>', methods=['GET', 'POST'])
def add_review(url):
    """
    This function allows any logged in user to post reviews to the
    festival 'hub' that they are currently browsing. It creates the
    review, but also updates the relevant festival record to include
    the new review's id, before then redirecting back to the previous
    festival page.
    """
    festival = mongo.db.festivals.find_one({'url': url})
    festival_id = festival['_id']
    if request.method == 'POST':
        # grab data from form
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

        # add review to the reviews collection on the db
        review_id = mongo.db.reviews.insert_one(review)
        review_new = mongo.db.reviews.find_one({'_id': review_id.inserted_id})
        review_new_rating = review_new['rating']
        # update the corresponding festival document by adding review id
        mongo.db.festivals.update_one(
            {"url": url},
            {'$push': {'reviews': {'review_id': review_id.inserted_id,
                                   'review_rating': review_new_rating}}})

        festival_reviews = festival['reviews']
        rating_arr = []

        for review in festival_reviews:
            rating_arr += review['review_rating']

        rating_arr_convert = map(int, rating_arr)
        rating_arr_int = list(rating_arr_convert)
        rating_arr_sum = sum(rating_arr_int)
        rating_arr_num = len(rating_arr_int)
        rating_arr_av = rating_arr_sum/rating_arr_num

        mongo.db.festivals.update_one(
            {"url": url},
            {'$push': {'reviews_av': rating_arr_av}})

        flash('Thanks for your review!')
        return redirect(url_for('view_festival', url=url))

    return render_template('add_review.html', festival=festival)


@app.route('/edit_review/<review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    """
    This allows logged in users to update their own reviews, before
    then being redirected back to the festival page they were reviewing.
    """
    review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    festival = mongo.db.festivals.find_one(
        {'_id': ObjectId(review['festival_id'])})
    url = festival['url']

    if request.method == 'POST':
        # grab data from form
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

        flash('Review has updated successfuly')
        return redirect(url_for('view_festival', url=url))

    return render_template('edit_review.html',
                           review=review,
                           festival=festival)


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    """
    This function allows logged in users to delete their own reviews
    from the festival page and from the database before redirecting
    back to the festival 'hub' the review was being deleted from.
    """
    review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    festival_id = review['festival_id']
    festival = mongo.db.festivals.find_one({'_id': ObjectId(festival_id)})
    url = festival['url']

    # delete review from database
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    # delete review id from festivals database
    mongo.db.festivals.update_one({"_id": ObjectId(festival_id)},
                                  {'$pull': {'reviews': ObjectId(review_id)}})
    flash("Review deleted")
    return redirect(url_for('view_festival', url=url))


@app.route('/add_favourites/<festival_id>', methods=['GET', 'POST'])
def add_favourites(festival_id):
    """
    This function allows logged in users to add or remove festivals
    form their 'favourites' page on various locations on the site.
    It checks if the user has favourited the festival already or not,
    and either removes or adds the festival to their profile depending
    on which is true.
    """
    username = session['user']
    festival = mongo.db.festivals.find_one({'_id': ObjectId(festival_id)})
    festival_users = festival['favourited_by']

    if request.method == 'POST':
        # check if the user appears on the festival's 'favourited_by' DB array
        if username in festival_users:
            # update the festival on DB to remove the username
            mongo.db.festivals.update_one(
                {'_id': festival['_id']},
                {'$pull': {'favourited_by': username}})
            # update the user on DB to remove festival from their favourites
            mongo.db.users.update_one(
                {'username': username},
                {'$pull': {'favourites': festival['_id']}})
            flash(festival.get('name') + ' removed from favourites')
        else:
            # add festival to the user's 'favourites' array on DB
            mongo.db.users.update_one(
                {"username": username},
                {'$push': {'favourites': festival['_id']}})
            # Add user to the festivals 'favourited_by' array on DB
            mongo.db.festivals.update_one(
                {"_id": festival['_id']},
                {'$push': {'favourited_by': username}})
            flash(festival.get('name') + ' added to favourites')
    return redirect(url_for('browse'))


@app.route('/faq')
def faq():
    """
    This function renders the static FAQ page.
    """
    return render_template('faq.html')


@app.route('/logout')
def logout():
    """
    This function removes the user from session
    cookies and redirects back to the login
    page.
    """
    flash("Goodbye!")
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        # DON'T FORGET TO CHANGE THIS TO FALSE BEFORE SUBMISSION
        debug=True
    )

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
    festivals = mongo.db.festivals.find()
    return render_template('index.html', festivals=festivals)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        # DON'T FORGET TO CHANGE THIS TO FALSE BEFORE SUBMISSION
        debug=True
    )

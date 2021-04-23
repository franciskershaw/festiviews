import os
from flask import Flask, render_template, request, flash
if os.path.exists('env.py'):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', '5000')),
        # DON'T FORGET TO CHANGE THIS TO FALSE BEFORE SUBMISSION
        debug=True
    )

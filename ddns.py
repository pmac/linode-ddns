import os
from flask import Flask, abort, request
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
API_KEY = os.environ['API_KEY']


@app.route('/', methods=['POST'])
def home():
    if request.form['api_key'] == API_KEY:
        return request.environ['REMOTE_ADDR']

    abort(400)

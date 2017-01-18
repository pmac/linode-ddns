from flask import Flask, request
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/')
def home():
    return request.environ['REMOTE_ADDR']

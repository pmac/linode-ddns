import os

from flask import Flask, abort, request, render_template
from werkzeug.contrib.fixers import ProxyFix

import requests
from decouple import config


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

API_KEY = config('API_KEY')
LINODE_API_KEY = config('LINODE_API_KEY')
LINODE_DOMAIN_ID = config('LINODE_DOMAIN_ID')
LINODE_RESOURCE_ID = config('LINODE_RESOURCE_ID')
API_URL = 'https://api.linode.com/'


def linode_api(action, params):
    req_params = {
        'api_key': LINODE_API_KEY,
        'api_action': action,
    }
    req_params.update(params)
    return requests.get(API_URL, params=req_params).json()


def get_current_ip():
    data = linode_api('domain.resource.list', {
        'DomainID': LINODE_DOMAIN_ID,
        'ResourceID': LINODE_RESOURCE_ID,
    })
    return data['DATA'][0]['TARGET']


def set_new_ip(new_ip):
    linode_api('domain.resource.update', {
        'DomainID': LINODE_DOMAIN_ID,
        'ResourceID': LINODE_RESOURCE_ID,
        'Target': new_ip,
    })


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method != 'POST':
        return render_template('index.html')

    if request.form.get('api_key', '') != API_KEY:
        abort(401)

    home_ip = request.environ['REMOTE_ADDR']
    dns_ip = get_current_ip()
    if dns_ip != home_ip:
        set_new_ip(home_ip)
        return 'Updated: %s' % home_ip
    else:
        return 'No Change', 304

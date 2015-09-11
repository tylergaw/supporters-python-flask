import os
import requests

from requests.auth import HTTPBasicAuth
from supporter_signup.config import config_app
from flask import Flask, redirect, request, url_for, render_template

# Initialize the app
app = Flask('supporter_signup')

# Set up the environment and logging
env = os.environ['ENV']
config_app(app, env)

try:
    API_URL = os.environ['GW_API_URL']
    API_CLIENT_ID = os.environ['GW_CLIENT_ID']
except KeyError:
    raise KeyError('You must set GW_API_URL and GW_CLIENT_ID environment variables.')

class Supporter:
    bucket_url = API_URL + 'bucket'
    auth = HTTPBasicAuth(API_CLIENT_ID, '')

    def create(self, payload):
        req = requests.post(self.bucket_url, json=payload, auth=self.auth)
        print req.headers
        print req.status_code
        print req.text
        return req


@app.route('/success/')
def success():
    return render_template(
        'success.html',
        email=request.args.get('email')
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    error = False
    supporter = Supporter()

    if request.method == 'POST':
        payload = {
            'email': request.form['email'],
            'source': request.form['source']
        }
        req = supporter.create(payload)

        if req.status_code == 201:
            return redirect(url_for('success', email=payload['email']))
        else:
            error = True

    return render_template('sign_up.html', error=error)

if __name__ == '__main__':
    app.run()

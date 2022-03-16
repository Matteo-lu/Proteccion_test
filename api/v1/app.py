#!/usr/bin/python3

from flask import Flask
from flask import make_response
from flask import jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import json

from api.v1.views import app_views

with open('secrets.json') as f:
    SECRETS = json.load(f)

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
   
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mateolondono.u@gmail.com'
app.config['MAIL_PASSWORD'] = SECRETS['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.errorhandler(404)
def not_found(error):
    """handler for 404 errors that returns a JSON-formatted 404 response"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

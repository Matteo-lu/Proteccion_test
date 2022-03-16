#!/usr/bin/python3

"""
    Module containing the mail view from the API
"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from flask import make_response
from flask_mail import Message
from api.v1.app import mail

from api.v1.views import app_views, fibo_function

@app_views.route('/message', strict_slashes=False)
def message():
    """view to send email with fibonacci result"""

    result = fibo_function.fibonacci()
    current = result["current time"]
    msg = Message('Mateo Londoño' + current,
                sender="mateolondono.u@example.com",
                recipients=["chamogomez@gmail.com", "correalondon@gmail.com"])
    msg.body = str(result["Fibonacci series"])
    mail.send(msg)
    return ('enviado')

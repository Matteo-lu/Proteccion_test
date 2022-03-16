#!/usr/bin/python3

"""
    Module containing the fibonacci view from the API
"""

from api.v1.views import app_views, fibo_function
from flask import Flask
from flask import jsonify


@app_views.route('/fibonacci', strict_slashes=False)
def fibonacci_view():
    """method to return the Fibonacci series
    according to the current time as test for Proteccion"""
    return (jsonify(fibo_function.fibonacci())), 200


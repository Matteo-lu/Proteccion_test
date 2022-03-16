#!/usr/bin/python3

"""
    Module containing the status view from the API
"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def index():
    """method to return status ok"""
    return (jsonify(status="OK")), 200

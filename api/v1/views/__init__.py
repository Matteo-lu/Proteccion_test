#!/usr/bin/python3

"""
initialize the views packages
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.status import *
from api.v1.views.fibonacci import *
from api.v1.views.fibo_function import *
from api.v1.views.mail import *

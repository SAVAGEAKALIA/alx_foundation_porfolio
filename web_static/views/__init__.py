#!/usr/bin/python3
""" Blueprint for Portfolio project """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from . import route_1

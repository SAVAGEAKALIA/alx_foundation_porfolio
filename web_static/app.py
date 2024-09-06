#!/usr/bin/env python
""" Flask application setup script """
from os import environ
from flask import Flask, render_template
from .views import app_views
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)
app.register_blueprint(app_views)


# @app.route('/', defaults={'path': ''}, strict_slashes=False)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(TemplateNotFound)
def template_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)

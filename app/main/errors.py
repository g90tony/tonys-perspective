from flask import render_template

from . import main

@main.errorhandler(404)
def resource_not_found(error):
    return render_template('404.html'),404
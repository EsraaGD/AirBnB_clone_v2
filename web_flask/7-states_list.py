#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Display html page with states list from A-Z"""
    s = sorted(list(storage.all("State").values()
    return render_template('7-state_list.html', states=s)

@app.teardown_appcontext
def teardown(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

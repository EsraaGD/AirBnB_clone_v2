#!/usr/bin/python3
"""Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Display an HTML page with a list of states sorted from A-Z.
    The states are retrieved from the storage,
    sorted, and then passed to the template.
    """
    s = sorted(list(storage.all("State").values()))
    return render_template('7-state_list.html', states=s)


@app.teardown_appcontext
def teardown(error):
    """Remove the current SQLAlchemy Session
    This function is called after each request,
    ensuring that database resources are properly released.
    """
    storage.close()


if __name__ == "__main__":
    """This is the entry point of the program that starts the Flask web server.
    """
    app.run(host='0.0.0.0', port=5000)

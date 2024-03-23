#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display ""Hello HBNB!"" message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display "HBNB" message"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Display "C" message"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_py(text):
    """Display "Python" message"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

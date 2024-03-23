#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template


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
def display_py(text='is cool'):
    """Display "Python" message"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Display "n is a number" message"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_num_template(n):
    """Display "n is a number" message"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_num_odd_even(n):
    """Display "n is a number" message"""
    if n % 2 == 0:
        number = "even"
    else:
        number = "odd"
    return render_template('6-number_odd_or_even.html', n=n, number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

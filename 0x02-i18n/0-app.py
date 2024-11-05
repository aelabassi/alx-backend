#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 1-index.html
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='', port=5000)

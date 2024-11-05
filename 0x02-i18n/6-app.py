#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


app = Flask(__name__)


class Config:
    """ Babel configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """ Get locale from request
    """
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES'])
    ]
    for local in options:
        if local and local in app.config['LANGUAGES']:
            return local


def get_user(login_as: int) -> Union[Dict[str, Union[str, None]], None]:
    """ Validate login_as
    Args:
        login_as: int
    Returns:
        Dict[str, Union[str, None]] or None
    """
    return users.get(login_as)


@app.before_request
def before_request():
    """ Before request
    """
    user = get_user(1)
    g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 1-index.html
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()

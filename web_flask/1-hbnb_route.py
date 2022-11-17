#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
        Routes: /
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_start():
    """
        Routes: /hbnb
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
        Routes: /
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
        Routes: /hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
        Routes: /c/<text>
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """
        Routes: /python/(<text>)
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def n_route(n):
    """
        Routes: /number/<n>
    """
    return "{}  is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_route(n):
    """
        Routes: /number_template/<n>
    """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

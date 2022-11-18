#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def city():
    """ Route: /cities_by_states
    """
    data = storage.all("State")
    return render_template("8-cities_by_states.html", states=data)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

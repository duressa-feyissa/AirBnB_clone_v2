#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)



@app.route("/hbnb_filters", strict_slashes=False)
def hbhnb_filters():
    """ Route: /hbnb_filters
    """
    data = storage.all("State")
    data2 = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=data, amenities=data2)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")

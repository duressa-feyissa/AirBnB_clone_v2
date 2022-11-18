#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def state(id=None):
    """ Route: /states or /states/<id>
    """
    data = storage.all("State")
    if id is None:
        return render_template("7-states_list.html", states=data)
    else:
        ID = "{}.{}".format("State", id)
        return render_template("9-states.html", state=data, id=ID)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")

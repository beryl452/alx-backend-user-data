#!/usr/bin/env python3
"""A simple Flask app with user authentication features.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    return jsonify({"message": "Bienvenue"})

# Copyright (c) Daniella Norman-Walker. All rights reserved.

from flask import Flask, send_from_directory

app = Flask(__name__)

"""
Main routes path.
All routing is client side, and so we just serve up the app.
"""
@app.route("/")
@app.route("/<path:path>")
def home(path = None):
    return send_from_directory('client/public', 'index.html')

"""
Path for all the static files (compiled JS/CSS, etc.)
"""
@app.route("/resource/<path:path>")
def content(path):
    return send_from_directory('client/public', path)

if __name__ == "__main__":
    app.run(debug=True, port=61975)

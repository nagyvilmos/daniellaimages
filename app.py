# Copyright (c) Daniella Norman-Walker. All rights reserved.
import os
from flask import Flask, send_from_directory, json

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
Query which images are available
"""
@app.route("/api/images")
def api_images():
    #os.listdir('resource/client/public')
    return json.jsonify(os.listdir('client/public/images'))

"""
Path for all the static files (compiled JS/CSS, etc.)
"""
@app.route("/resource/<path:path>")
def content(path):
    return send_from_directory('client/public', path)

if __name__ == "__main__":
    app.run(debug=True, port=61975)

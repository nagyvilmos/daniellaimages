# Copyright (c) Daniella Norman-Walker. All rights reserved.

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def root():
    return send_from_directory('client/public', 'index.html')

if __name__ == "__main__":
    app.run(debug=True, port=61975)

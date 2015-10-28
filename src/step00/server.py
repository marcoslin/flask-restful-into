#!/usr/bin/env python

from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def root():
    msg = {"message": "Hello World"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(debug=True)

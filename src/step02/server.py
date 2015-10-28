#!/usr/bin/env python

from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound
app = Flask(__name__)


@app.route("/")
def root():
    msg = {"message": "This is Root"}
    return jsonify(msg)


@app.route("/car1/<make>/<model>")
def car1(make, model):
    car = {
        "make": make,
        "model": model
    }
    return jsonify(car)


@app.route("/car2/<string:make>/<int:model>")
def car2(make, model):
    car = {
        "make": make,
        "model": model
    }
    return jsonify(car)


@app.route("/car/<string:make>/<int:model>")
@app.route("/car/<string:make>/", defaults={"model": 500})
@app.route("/car/", defaults={"make": "Fiat", "model": 500})
def car(make, model):
    car = {
        "make": make,
        "model": model
    }
    return jsonify(car)


@app.route("/inventory/", methods=['POST'])
def inventory_post():
    data = request.json
    resp = jsonify({"idinput": data.get("id")})
    resp.status_code = 201
    return resp


if __name__ == "__main__":
    app.run(debug=True)

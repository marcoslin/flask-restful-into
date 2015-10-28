#!/usr/bin/env python

import time
from flask import Flask, jsonify, Response, json, send_file

app = Flask(__name__)


@app.route("/")
def root():
    msg = {"message": "This is Root"}
    return jsonify(msg)


@app.route("/simple/")
def return_simple():
    return "I lost it", 404


@app.route("/generator/")
def return_generator():

    def loads_of_data():
        yield "["
        for i in xrange(5):
            if i:
                yield ","
            yield '{ "key%d": "Entry Number %d"}' % (i, i)
            time.sleep(1)
        yield "]"

    return Response(loads_of_data(), content_type="application/json")


@app.route("/response/")
def return_response():
    msg = {"message": "I am working on that..."}
    msg_json = json.dumps(msg)
    return Response(msg_json, content_type="application/json", status=202)


@app.route("/file/")
def return_file():
    return send_file('flask_logo.png')


if __name__ == "__main__":
    app.run(debug=True)

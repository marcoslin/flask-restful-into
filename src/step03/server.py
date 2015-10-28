#!/usr/bin/env python

from flask import Flask, redirect

from lib import set_restful_error_handler
from routes import static, sample, camera

app = Flask(__name__)

set_restful_error_handler(app)

app.register_blueprint(static.blueprint(), url_prefix='/app')
app.register_blueprint(sample.blueprint(), url_prefix='/sample')
app.register_blueprint(camera.blueprint(), url_prefix='/d')


@app.route("/")
def root():
    return redirect('/app')


if __name__ == "__main__":
    app.run()

from flask import Blueprint, send_from_directory


def blueprint():
    bp = Blueprint('static', __name__)

    @bp.route('/<path:path>')
    def send_app(path):
        return send_from_directory('www/', path)

    @bp.route('/')
    def send_app_index():
        return send_from_directory('www/', 'index.html')

    return bp

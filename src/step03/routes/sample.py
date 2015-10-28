from flask import Blueprint, jsonify, request
from werkzeug.exceptions import NotFound


def blueprint():
    bp = Blueprint('sample', __name__)

    @bp.route("/inventory/", methods=['POST'])
    def inventory_post():
        data = request.json
        resp = jsonify({"idinput": data.get("id")})
        resp.status_code = 201
        return resp

    @bp.route("/inventory/<int:id>", methods=['GET', 'PUT', 'DELETE'])
    def inventory_getput(id):
        if request.method == "GET":
            if id < 10:
                return jsonify({"idinput": id})
            else:
                raise NotFound("%d does not exists in the system" % id)
        elif request.method == "DELETE":
            return "Deleted", 204
        else:
            data = request.json
            data["id"] = id
            return jsonify(data)

    @bp.route("/error/", methods=['GET', 'PUT', 'DELETE'])
    def return_error():
        result = 10/0
        return result

    return bp

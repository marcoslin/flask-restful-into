import requests
from flask import Blueprint, jsonify, Response, json
from werkzeug.exceptions import NotFound

from lib import CameraData


def blueprint():
    bp = Blueprint('camera', __name__)

    @bp.route('/collegio/')
    def collegio_list():
        # jsonify doesn't support list
        return Response(json.dumps(CameraData.COLLEGIO), content_type="application/json")

    @bp.route('/collegio/<string:id>')
    def collegio_get(id):
        res = None
        for entry in CameraData.COLLEGIO:
            if entry.get("id") == id:
                res = entry
                break

        if res:
            return jsonify(res)
        else:
            raise NotFound("Collegio not found for id %s" % id)

    @bp.route('/deputato/<string:collegio>/')
    def deputato_list(collegio):
        sql = CameraData.SPARQL % collegio
        url = CameraData.SPARQL_URL_PRE + sql + CameraData.SPARQL_URL_POS

        resp = requests.get(url, stream=True)
        return Response(resp.iter_lines(), content_type="application/json")

    return bp

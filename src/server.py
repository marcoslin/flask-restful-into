#!/usr/bin/env python

from flask import Flask, jsonify, Response
import requests
app = Flask(__name__)

SPARQL = '''
SELECT
    distinct ?deputato ?nome ?cognome ?img ?categoryY ?categoryX
WHERE {
    ?deputato a ocd:deputato;
        ocd:rif_leg <http://dati.camera.it/ocd/legislatura.rdf/repubblica_17>;
        foaf:firstName ?nome; foaf:surname ?cognome;
        foaf:gender ?categoryY; foaf:depiction ?img;
        ocd:rif_mandatoCamera ?mandato;
        ocd:aderisce ?aderisce .

    ?aderisce ocd:rif_gruppoParlamentare ?gruppo .
    ?gruppo <http://purl.org/dc/terms/alternative> ?categoryX .

    ?mandato ocd:rif_elezione ?elezione . ?elezione dc:coverage "TOSCANA" .

    FILTER NOT EXISTS{
        ?mandato ocd:endDate ?date
    }
    MINUS{
        ?aderisce ocd:endDate ?fineAdesione
    }
}
'''


@app.route("/")
def root():
    msg = {"message": "This is Root"}
    return jsonify(msg)


@app.route("/query/")
def query():
    url = "http://dati.camera.it/sparql?default-graph-uri=&query=" + SPARQL + "&format=application%2Fjson&timeout=0&debug=on"
    resp = requests.get(url, stream=True)
    return Response(resp.iter_lines(), content_type="application/json")


if __name__ == "__main__":
    app.run(debug=True)

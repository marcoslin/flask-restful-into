from flask import jsonify
from werkzeug.exceptions import default_exceptions, HTTPException
from werkzeug.exceptions import InternalServerError


def set_restful_error_handler(app):
    def restful_error_handler(ex):
        resp = jsonify(error_message=str(ex))
        if isinstance(ex, HTTPException):
            resp.status_code = ex.code
        else:
            resp.status_code = InternalServerError.code
        return resp

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = restful_error_handler


class CameraData(object):
    COLLEGIO = [
        {"id": "ABRUZZO", "desc": "Abruzzo"},
        {"id": "BASILICATA", "desc": "Basilicata"},
        {"id": "CALABRIA", "desc": "Calabria"},
        {"id": "CAMPANIA 1", "desc": "Campania 1"},
        {"id": "CAMPANIA 2", "desc": "Campania 2"},
        {"id": "EMILIA-ROMAGNA", "desc": "Emilia-Romagna"},
        {"id": "FRIULI-VENEZIA GIULIA", "desc": "Friuli-Venezia Giulia"},
        {"id": "LAZIO 1", "desc": "Lazio 1"},
        {"id": "LAZIO 2", "desc": "Lazio 2"},
        {"id": "LIGURIA", "desc": "Liguria"},
        {"id": "LOMBARDIA 1", "desc": "Lombardia 1"},
        {"id": "LOMBARDIA 2", "desc": "Lombardia 2"},
        {"id": "LOMBARDIA 3", "desc": "Lombardia 3"},
        {"id": "MARCHE", "desc": "Marche"},
        {"id": "MOLISE", "desc": "Molise"},
        {"id": "PIEMONTE 1", "desc": "Piemonte 1"},
        {"id": "PIEMONTE 2", "desc": "Piemonte 2"},
        {"id": "PUGLIA", "desc": "Puglia"},
        {"id": "SARDEGNA", "desc": "Sardegna"},
        {"id": "SICILIA 1", "desc": "Sicilia 1"},
        {"id": "SICILIA 2", "desc": "Sicilia 2"},
        {"id": "TOSCANA", "desc": "Toscana"},
        {"id": "TRENTINO-ALTO ADIGE", "desc": "Trentino-Alto Adige"},
        {"id": "UMBRIA", "desc": "Umbria"},
        {"id": "VALLE D'AOSTA", "desc": "Valle d'Aosta"},
        {"id": "VENETO 1", "desc": "Veneto 1"},
        {"id": "VENETO 2", "desc": "Veneto 2"}
    ]

    SPARQL_URL_PRE = "http://dati.camera.it/sparql?default-graph-uri=&query="

    SPARQL_URL_POS = "&format=application%2Fjson&timeout=0&debug=on"

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

        ?mandato ocd:rif_elezione ?elezione . ?elezione dc:coverage "%s" .

        FILTER NOT EXISTS{
            ?mandato ocd:endDate ?date
        }
        MINUS{
            ?aderisce ocd:endDate ?fineAdesione
        }
    }
    '''

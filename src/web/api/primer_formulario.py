from flask import Blueprint, jsonify, request
#from src.web.controllers.api import base
#import requests
#from src.web.forms.postulacion_form import PostulacionForm, PostulacionFormValues
#from src.web.schemas.postulacion_schema import postulacion_schema

bp = Blueprint("postulacion", __name__, url_prefix="/api/postulacion")


#@base.validation(schema=PostulacionForm, method="POST")
@bp.post("/primer-formulario")
def primer_formulario():
    """
    Primer formulario de postulación.
    """
    data = request.get_json()
    print(data)
    return jsonify(data), 201
    """
    postulacion_data = postulacion_schema.load(body["postulacion"])



    return jsonify(body), 201
    """

@bp.get("/segundo-formulario")
def segundo_formulario():
    """
    Segundo formulario de postulación.
    """
    return jsonify({"message": "Segundo formulario de postulación"}), 200
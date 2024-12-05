from flask import Blueprint, jsonify, request


from src.core.services import paises_service, genero_service, estado_civil_service
from src.web.schemas import estado_civil_schema, genero_schema, pais_schema, postulacion_schema



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

@bp.get("/primer-formulario-data")
def primer_formulario_get():
    """
    
    """
    paises = paises_service.listar_paises()
    generos = genero_service.listar_generos()
    estados_civiles = estado_civil_service.listar_estados_civiles()
    #programa = get_programa()
    data_paises = pais_schema.paises_schema.dump(paises)
    data_generos = genero_schema.generos_schema.dump(generos)
    data_estados_civiles = estado_civil_schema.estados_civiles_schema.dump(estados_civiles)


    data_response = {
        "paises": data_paises,
        "generos": data_generos,
        "estados_civiles": data_estados_civiles,
        #"programa": programa
    }

    return jsonify(data_response), 200
from flask import Blueprint, jsonify, request, make_response
from flask_wtf.csrf import generate_csrf


from src.core.services import paises_service, genero_service, estado_civil_service
from src.web.schemas import (
    estado_civil_schema, genero_schema, pais_schema, postulacion_schema, informacion_alumno_entrante_schema,
    tutor_schema, archivo_schema
)



bp = Blueprint("solicitud_postulacion", __name__, url_prefix="/api/postulacion")


#@base.validation(schema=PostulacionForm, method="POST")

@bp.post("/primer-formulario")
def primer_formulario():
    """
    Primer formulario de postulación.
    """
    data = request.get_json()
    return jsonify(data), 201
    token = request.headers.get("X-CSRF-Token")

    print(data)
    data_postulacion = data["postulacion"]
    data_alumno = data["alumno"]
    id_programa = data["id_programa"]
    data_tutor_institucional = data["tutorInstitucional"]
    data_tutor_academico = data["tutorAcademico"]
    data_cedula = data["cedula_de_identidad"]
    data_pasaporte = data["pasaporte"]
    data_archivos = data["archivo"]
    
    archivo_pasaporte = data_archivos["pasaporte"]
    archivo_cedula = data_archivos["cedula_de_identidad"]
    certificado_b1 = data_archivos["certificado_b1"]
    plan_trabajo = data_archivos["plan_trabajo"]
    carta_recomendacion = data_archivos["carta_recomendacion"]



    alumno = informacion_alumno_entrante_schema.load(data_alumno)
    data_postulacion["id_estado"] = 1
    data_postulacion["id_informacion_alumno_entrante"] = alumno.id
    data_postulacion["id_programa"] = id_programa
    postulacion = postulacion_schema.load(data_postulacion)
   
    tutor_institucional = tutor_schema.load(data_tutor_institucional)
    tutor_academico = tutor_schema.load(data_tutor_academico)


    return jsonify(data), 201
    

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

    token = generate_csrf()
    data_response = {
        "paises": data_paises,
        "generos": data_generos,
        "estados_civiles": data_estados_civiles,
        "csrf_token": token
        #"programa": programa
    }

    #response = make_response(jsonify(data_response), 200)
    #.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173/primer-formulario'
    return jsonify(data_response), 200

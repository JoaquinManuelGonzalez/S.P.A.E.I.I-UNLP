from flask import Blueprint, jsonify, request, make_response
from flask_wtf.csrf import generate_csrf
import base64
import os

from src.core.services import (paises_service, genero_service, 
estado_civil_service, archivo_service, alumno_service, pasaporte_service, 
cedula_de_identidad_service, postulacion_service, tutor_service)
from src.web.schemas.archivo_schema import archivo_schema
from src.web.schemas.cedula_de_identidad_schema import cedula_de_identidad_schema
from src.web.schemas.postulacion_schema import postulacion_schema
from src.web.schemas.pasaporte_schema import pasaporte_schema
from src.web.schemas.estado_civil_schema import estados_civiles_schema
from src.web.schemas.tutor_schema import tutor_schema
from src.web.schemas.genero_schema import generos_schema
from src.web.schemas.pais_schema import paises_schema
from src.web.schemas.informacion_alumno_entrante_schema import informacion_alumno_entrante_schema




bp = Blueprint("solicitud_postulacion", __name__, url_prefix="/api/postulacion")


#@base.validation(schema=PostulacionForm, method="POST")

@bp.post("/primer-formulario")
def primer_formulario():
    """
    Primer formulario de postulación.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se encontraron datos en el request"}), 400
    data_postulacion = data["postulacion"]
    data_alumno = data["alumno"]
    id_programa = data["id_programa"]
    data_tutor_institucional = data["tutorInstitucional"]
    data_tutor_academico = data["tutorAcademico"]
    data_cedula = data["cedula_de_identidad"]
    data_pasaporte = data["pasaporte"]
    data_archivos = data["archivo"]
    mercosur = data["mercosur"]
    convenio_programa = data["convenioPrograma"]
    data_titulos = data["titulos"]
    

    if not data_postulacion:
        return jsonify({"error": "No se encontraron datos de la postulación"}), 400
    if not data_alumno:
        return jsonify({"error": "No se encontraron datos del alumno"}), 400
    if not data_tutor_institucional:
        return jsonify({"error": "No se encontraron datos del tutor institucional"}), 400
    if not data_tutor_academico:
        return jsonify({"error": "No se encontraron datos del tutor académico"}), 400
    if not data_archivos:
        return jsonify({"error": "No se encontraron datos de los archivos"}), 400
    if not convenio_programa:
        return jsonify({"error": "No se encontraron datos sobre si es por convenio o programa"}), 400
    if not data_titulos:
        return jsonify({"error": "No se encontraron datos de los títulos"}), 400

    if not mercosur:
        if not data_pasaporte:
            return jsonify({"error": "No se encontraron datos del pasaporte"}), 400
        else:
            archivo_pasaporte = base64.b64decode(data_archivos["pasaporte"])
            if not data_titulos["titulo_pasaporte"]:
                return jsonify({"error": "No se encontraron datos del título del pasaporte"}), 400
            titulo_pasaporte = {
                "titulo": data_titulos["titulo_pasaporte"]
            }
            try:
                pasaporte = archivo_schema.load(titulo_pasaporte)
            except Exception as err:
                return jsonify({"error": f"Error al cargar los datos del pasaporte: {err}"}), 400
            pasaporte_archivo = archivo_service.crear_archivo(**pasaporte)
            data_pasaporte["id_archivo"] = pasaporte_archivo.id
            pasaporte = pasaporte_schema.load(data_pasaporte)
            pasaporte = pasaporte_service.crear_pasaporte(**pasaporte)
            pasaporte_archivo.pasaporte = pasaporte
    else:
        if not data_pasaporte and not data_cedula:
            return jsonify({"error": "No se encontraron datos de la cédula de identidad ni del pasaporte"}), 400
        if data_pasaporte:
            archivo_pasaporte = base64.b64decode(data_archivos["pasaporte"])
            if not data_titulos["titulo_pasaporte"]:
                return jsonify({"error": "No se encontraron datos del título del pasaporte"}), 400
            titulo_pasaporte = {
                "titulo": data_titulos["titulo_pasaporte"]
            }
            try:
                pasaporte = archivo_schema.load(titulo_pasaporte)
            except Exception as err:
                return jsonify({"error": f"Error al cargar los datos del pasaporte: {err}"}), 400
            pasaporte_archivo = archivo_service.crear_archivo(**pasaporte)
            data_pasaporte["id_archivo"] = pasaporte_archivo.id
            pasaporte = pasaporte_schema.load(data_pasaporte)
            pasaporte = pasaporte_service.crear_pasaporte(**pasaporte)
            pasaporte_archivo.pasaporte = pasaporte
        if data_cedula:
            archivo_cedula = base64.b64decode(data_archivos["cedula_de_identidad"])
            if not data_titulos["titulo_cedula_de_identidad"]:
                return jsonify({"error": "No se encontraron datos del título del pasaporte"}), 400
            titulo_cedula = {
                "titulo": data_titulos["titulo_cedula_de_identidad"]
            }
            try:
                cedula_de_identidad = archivo_schema.load(titulo_cedula)
            except Exception as err:
                return jsonify({"error": f"Error al cargar los datos de la cedula de identidad: {err}"}), 400
            cedula_de_identidad_archivo = archivo_service.crear_archivo(**cedula_de_identidad)
            data_cedula["id_archivo"] = cedula_de_identidad_archivo.id
            cedula_de_identidad = cedula_de_identidad_schema.load(data_cedula)
            cedula_de_identidad = cedula_de_identidad_service.crear_cedula_de_identidad(**cedula_de_identidad)
            cedula_de_identidad_archivo.cedula_identidad = cedula_de_identidad

   
    carta_recomendacion = data_archivos["carta_recomendacion"]
    if not carta_recomendacion:
        return jsonify({"error": "No se encontraron datos de la carta de recomendación"}), 400
    else:
        archivo_carta_recomendacion = base64.b64decode(data_archivos["carta_recomendacion"])
        if not data_titulos["titulo_carta_recomendacion"]:
            return jsonify({"error": "No se encontraron datos del título de la carta de recomendación"}), 400
        titulo_carta_recomendacion = {
            "titulo": data_titulos["titulo_carta_recomendacion"]
        }
        try:
            carta_recomendacion = archivo_schema.load(titulo_carta_recomendacion)
        except Exception as err:
            return jsonify({"error": f"Error al cargar los datos de la carta de recomendación: {err}"}), 400
        carta_recomendacion = archivo_service.crear_archivo(**carta_recomendacion)
        
    
    data_alumno["discapacitado"] = False
    if data_pasaporte["numero"] != "":
        data_alumno["id_pasaporte"] = pasaporte.id
    if data_cedula["numero"] != "":
        data_alumno["id_cedula_de_identidad"] = cedula_de_identidad.id
    try:
        print(data_alumno)
        alumno = informacion_alumno_entrante_schema.load(data_alumno)
    except Exception as err:
        return jsonify({"error": f"Error al cargar los datos del alumno: {err}"}), 400
    alumno = alumno_service.crear_informacion_alumno_entrante(**alumno)

    data_postulacion["id_estado"] = 1
    data_postulacion["id_informacion_alumno_entrante"] = alumno.id
    if convenio_programa == "programa":
        data_postulacion["id_programa"] = id_programa
    try:
        postulacion = postulacion_schema.load(data_postulacion)
    except Exception as err:
        return jsonify({"error": f"Error al cargar los datos de la postulación: {err}"}), 400
    postulacion = postulacion_service.crear_postulacion(**postulacion)
    postulacion.informacion_alumno_entrante = alumno
    
    if postulacion.de_posgrado:
        if not data_archivos["plan_trabajo"]:
            return jsonify({"error": "No se encontraron datos del plan de trabajo"}), 400
        else:
            plan_trabajo = base64.b64decode(data_archivos["plan_trabajo"])
            if not data_titulos["titulo_plan_trabajo"]:
                return jsonify({"error": "No se encontraron datos del título del plan de trabajo"}), 400
            titulo_plan_trabajo = {
                "titulo": data_titulos["titulo_plan_trabajo"]
            }
            try:
                plan_trabajo = archivo_schema.load(titulo_plan_trabajo)
            except Exception as err:
                return jsonify({"error": f"Error al cargar los datos del plan de trabajo: {err}"}), 400
            plan_trabajo = archivo_service.crear_archivo(**plan_trabajo)

    
    pais_nacionalidad = paises_service.get_pais_by_id(alumno.id_pais_nacionalidad)
    if pais_nacionalidad.hispanohablante:
        if data_archivos["certificado_b1"]:
            archivo_certificado_b1 = base64.b64decode(data_archivos["certificado_b1"])
            if not data_titulos["titulo_certificado_b1"]:
                return jsonify({"error": "No se encontraron datos del título del certificado B1"}), 400
            titulo_certificado_b1 = {
                "titulo": data_titulos["titulo_certificado_b1"]
            }
            try:
                certificado_b1 = archivo_schema.load(titulo_certificado_b1)
            except Exception as err:
                return jsonify({"error": f"Error al cargar los datos del certificado B1: {err}"}), 400
            certificado_b1 = archivo_service.crear_archivo(**certificado_b1)
    else:
        if not data_archivos["certificado_b1"]:
            return jsonify({"error": "No se encontraron datos del certificado B1"}), 400
        else:
            archivo_certificado_b1 = base64.b64decode(data_archivos["certificado_b1"])
            if not data_titulos["titulo_certificado_b1"]:
                return jsonify({"error": "No se encontraron datos del título del certificado B1"}), 400
            titulo_certificado_b1 = {
                "titulo": data_titulos["titulo_certificado_b1"]
            }
            try:
                certificado_b1 = archivo_schema.load(titulo_certificado_b1)
            except Exception as err:
                return jsonify({"error": f"Error al cargar los datos del certificado B1: {err}"}), 400
            certificado_b1 = archivo_service.crear_archivo(**certificado_b1)
    
    try:
        tutor_institucional = tutor_schema.load(data_tutor_institucional)
    except:
        return jsonify({"error": "Error al cargar los datos del tutor institucional"}), 400
    tutor_institucional = tutor_service.crear_tutor(**tutor_institucional)
    try:
        tutor_academico = tutor_schema.load(data_tutor_academico)
    except:
        return jsonify({"error": "Error al cargar los datos del tutor académico"}), 400
    tutor_academico = tutor_service.crear_tutor(**tutor_academico)

    carta_recomendacion.informacion_alumno_entrante = alumno
    carta_recomendacion.postulacion = postulacion

    if data_pasaporte["numero"] != "":
        pasaporte_archivo.informacion_alumno_entrante = alumno
        pasaporte_archivo.postulacion = postulacion
        
    if data_cedula["numero"] != "":
        cedula_de_identidad_archivo.informacion_alumno_entrante = alumno
        cedula_de_identidad_archivo.postulacion = postulacion
    
    if data_archivos["certificado_b1"] != "":
        certificado_b1.informacion_alumno_entrante = alumno
        certificado_b1.postulacion = postulacion

    if data_archivos["plan_trabajo"] != None:
        plan_trabajo.informacion_alumno_entrante = alumno
        plan_trabajo.postulacion = postulacion

    tutor_institucional.postulaciones.append = postulacion
    tutor_academico.postulaciones.append = postulacion



    return jsonify(data), 201
    
    
    

@bp.get("/primer-formulario-data")
def primer_formulario_get():
    """
    
    """
    paises = paises_service.listar_paises()
    generos = genero_service.listar_generos()
    estados_civiles = estado_civil_service.listar_estados_civiles()
    #programa = get_programa()
    data_paises = paises_schema.dump(paises)
    data_generos = generos_schema.dump(generos)
    data_estados_civiles = estados_civiles_schema.dump(estados_civiles)

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

from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from src.core.models.postulacion import Postulacion
from src.core.services import (postulacion_service, alumno_service, estado_postulacion_service,
paises_service, genero_service, estado_civil_service, pasaporte_service, cedula_de_identidad_service,
programa_service)


postulacion_bp = Blueprint('postulacion', __name__, url_prefix='/postulaciones')

@postulacion_bp.get('/')
def listar_postulaciones():

    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")
    email = request.args.get("email")
    estado = request.args.get("estado")
    pagina = request.args.get("pagina", 1, type=int)
    ordenado_por = request.args.get("ordenado_por", "nombre")
    orden = request.args.get("orden", "asc")
    por_pagina = 10

    postulaciones = postulacion_service.filtrar_postulaciones(
        nombre,
        apellido,
        email,
        estado,
        pagina,
        ordenado_por,
        orden,
        por_pagina
    )

    estados = estado_postulacion_service.listar_estados()

    #postulaciones = postulacion_service.listar_postulaciones()
    return render_template('postulaciones/listar_postulaciones.html', postulaciones=postulaciones, estados=estados)

@postulacion_bp.get('/ver_postulacion/<int:id_postulacion>')
def ver_postulacion(id_postulacion):
    postulacion = postulacion_service.get_postulacion_by_id(id_postulacion)
    alumno = alumno_service.get_alumno_by_id(postulacion.id_informacion_alumno_entrante)
    pais_residencia = paises_service.get_pais_by_id(alumno.id_pais_de_residencia)
    nacionalidad = paises_service.get_pais_by_id(alumno.id_pais_nacionalidad)
    pais_nacimiento = paises_service.get_pais_by_id(alumno.id_pais_de_nacimiento)
    genero = genero_service.get_genero_by_id(alumno.id_genero)
    estado_civil = estado_civil_service.get_estado_civil_by_id(alumno.id_estado_civil)
    if alumno.id_pasaporte is not None:
        pasaporte = pasaporte_service.get_pasaporte_by_id(alumno.id_pasaporte)
        pais_pasaporte = paises_service.get_pais_by_id(pasaporte.id_pais)
    else:
        pasaporte = None
        pais_pasaporte = None
    if alumno.id_cedula_de_identidad is not None:
        cedula_de_identidad = cedula_de_identidad_service.get_cedula_de_identidad_by_id(alumno.id_cedula_de_identidad)
        pais_cedula_de_identidad = paises_service.get_pais_by_id(cedula_de_identidad.id_pais)
    else:
        cedula_de_identidad = None
        pais_cedula_de_identidad = None
    if postulacion.id_programa is not None:
        programa = programa_service.get_programa_by_id(postulacion.id_programa)
    else:
        programa = None

    tutores = postulacion.tutores
    tutor_institucional = None
    tutor_academico = None
    for tutor in tutores:
        if tutor.es_institucional:
            tutor_institucional = tutor
        else:
            tutor_academico = tutor
    
    data = {
        "postulacion": postulacion,
        "alumno": alumno,
        "pais_residencia": pais_residencia,
        "nacionalidad": nacionalidad,
        "pais_nacimiento": pais_nacimiento,
        "genero": genero,
        "estado_civil": estado_civil,
        "pasaporte": pasaporte,
        "cedula_de_identidad": cedula_de_identidad,
        "programa": programa,
        "pais_pasaporte": pais_pasaporte,
        "pais_cedula_de_identidad": pais_cedula_de_identidad,
        "tutor_institucional": tutor_institucional,
        "tutor_academico": tutor_academico
    }
    return render_template('postulaciones/ver_postulacion.html', **data)


@postulacion_bp.post('aprobar_solicitud_de_postulacion/<int:id_postulacion>')
def aceptar_solicitud(id_postulacion):
    pass

@postulacion_bp.post('rechazar_solicitud_de_postulacion/<int:id_postulacion>')
def rechazar_solicitud(id_postulacion):
    pass  

@postulacion_bp.get('/listar_solicitudes_de_postulacion')
def listar_solicitudes_de_postulacion():
    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")
    email = request.args.get("email")
    estado = "Solicitud de Postulacion"
    pagina = request.args.get("pagina", 1, type=int)
    ordenado_por = request.args.get("ordenado_por", "nombre")
    orden = request.args.get("orden", "asc")
    por_pagina = 10

    postulaciones = postulacion_service.filtrar_postulaciones(
        nombre,
        apellido,
        email,
        estado,
        pagina,
        ordenado_por,
        orden,
        por_pagina
    )

    estados = estado_postulacion_service.listar_estados()

    #postulaciones = postulacion_service.listar_postulaciones()
    return render_template('postulaciones/listar_solicitudes_de_postulacion.html', postulaciones=postulaciones, estados=estados)
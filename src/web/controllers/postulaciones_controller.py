import csv
from flask import Blueprint, Response, request, render_template, redirect, url_for, flash, session
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
        pasaporte = ""
        pais_pasaporte = ""
    if alumno.id_cedula_de_identidad is not None:
        cedula_de_identidad = cedula_de_identidad_service.get_cedula_de_identidad_by_id(alumno.id_cedula_de_identidad)
        pais_cedula_de_identidad = paises_service.get_pais_by_id(cedula_de_identidad.id_pais)
    else:
        cedula_de_identidad = ""
        pais_cedula_de_identidad = ""
    if postulacion.id_programa is not None:
        programa = programa_service.get_programa_by_id(postulacion.id_programa)
    else:
        programa = ""

    tutores = postulacion.tutores
    tutor_institucional = ""
    tutor_academico = ""
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


@postulacion_bp.post('aprobar_rechazar_postulacion/<int:id_postulacion>')
def aceptar_rechazar_1(id_postulacion):
    if request.method == 'POST':
        decision = request.form['decision']

        if decision == 'aceptar':
            postulacion_service.aprobar_postulacion_etapa_1(id_postulacion)
            flash('Postulación aprobada', 'success')
            return redirect(url_for('postulacion.ver_postulacion', id_postulacion=id_postulacion))
    else:
        flash('Debe seleccionar una opción', 'danger')
        return redirect(url_for('postulacion.ver_postulacion', id_postulacion=id_postulacion))
    

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

@postulacion_bp.get('/exportar_csv')
def exportar_csv():
    # Obtener los parámetros de filtrado
    nombre = request.args.get("nombre", None)
    apellido = request.args.get("apellido", None)
    email = request.args.get("email", None)
    estado = request.args.get("estado", None)
    ordenado_por = request.args.get("ordenado_por", None)
    orden = request.args.get("orden", None)

    # Filtrar las postulaciones según los parámetros
    postulaciones = postulacion_service.get_postulaciones(
        nombre,
        apellido,
        email,
        estado,
        ordenado_por,
        orden
    )

    # Crear los datos para el CSV
    datos_csv = [["Nombre", "Apellido", "Email", "Fecha de Postulación", "Estado"]]
    for postulacion in postulaciones:
        datos_csv.append([
            postulacion.informacion_alumno_entrante.nombre,
            postulacion.informacion_alumno_entrante.apellido,
            postulacion.informacion_alumno_entrante.email,
            postulacion.creacion.strftime("%d-%m-%Y"),
            postulacion.estado.nombre,
        ])

    # Generar la respuesta CSV
    response = Response(
        "\n".join([",".join(map(str, fila)) for fila in datos_csv]),
        mimetype="text/csv",
    )
    response.headers["Content-Disposition"] = "attachment; filename=postulaciones.csv"
    return response
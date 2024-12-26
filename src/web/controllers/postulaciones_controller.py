from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from src.core.models.postulacion import Postulacion
from src.core.services import (postulacion_service, alumno_service, estado_postulacion_service,
paises_service, genero_service, estado_civil_service, pasaporte_service, cedula_de_identidad_service,
programa_service, archivo_service, usuario_service, email_service, periodo_postulacion_service)
from src.core.database import db
from flask import current_app as app
from src.web.handlers.permisos import check
import os
import io
from src.web.handlers.auth import get_rol_sesion, get_id_sesion
from src.web.handlers.permisos import check
import time
from src.web.forms.postulacion_form import PostulacionForm
from src.web.forms.postulacion_estadia_form import PostulacionEstadiaForm
from src.web.schemas.archivo_schema import archivo_schema

postulacion_bp = Blueprint('postulacion', __name__, url_prefix='/postulaciones')


@postulacion_bp.get('/')
@check("postulaciones_listar")
@check("gestor")
@check("admin")
def listar_postulaciones():

    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")
    email = request.args.get("email")
    fecha_desde = request.args.get("fecha_desde")
    fecha_hasta = request.args.get("fecha_hasta")
    estado = request.args.get("estado")
    pagina = request.args.get("pagina", 1, type=int)
    ordenado_por = request.args.get("ordenado_por", "nombre")
    orden = request.args.get("orden", "asc")
    id_periodo = request.args.get("id_periodo")
    por_pagina = 10

    postulaciones = postulacion_service.filtrar_postulaciones(
        nombre,
        apellido,
        email,
        estado,
        pagina,
        ordenado_por,
        orden,
        por_pagina,
        fecha_desde,
        fecha_hasta,
        id_periodo
    )

    periodos_postulacion = periodo_postulacion_service.listar_periodos_postulacion()

    estados = estado_postulacion_service.listar_estados()

    #postulaciones = postulacion_service.listar_postulaciones()
    return render_template('postulaciones/listar_postulaciones.html', postulaciones=postulaciones, estados=estados, periodos=periodos_postulacion)


@postulacion_bp.get('/ver_postulacion/<int:id_postulacion>')
#@check("postulaciones_detalle")
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

    archivos = archivo_service.get_archivos_by_postulacion(postulacion.id)
    presidencia = False
    if get_rol_sesion(session) == "jefe" or "admin":
        presidencia = True
        
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
        "tutor_academico": tutor_academico,
        "archivos": archivos,
        "presidencia": presidencia
    }
    return render_template('postulaciones/ver_postulacion.html', **data)


@postulacion_bp.post('aprobar_solicitud_de_postulacion/<int:id_postulacion>')
@check("solicitud_postulacion_aceptar")
def aceptar_solicitud(id_postulacion):
    postulacion = postulacion_service.get_postulacion_by_id(id_postulacion)
    postulacion_service.actualizar_estado_postulacion(postulacion, "Postulacion Iniciada")
    alumno = alumno_service.get_alumno_by_id(postulacion.id_informacion_alumno_entrante)
    usuario_service.crear_usuario_solicitud_aprobada(alumno.nombre, alumno.apellido, alumno.email, alumno.id)
    flash('Solicitud de postulacion aprobada', 'success')
    return redirect(url_for('postulacion.listar_solicitudes_de_postulacion'))
    

@postulacion_bp.post('rechazar_solicitud_de_postulacion/<int:id_postulacion>')
@check("solicitud_postulacion_rechazar")
def rechazar_solicitud(id_postulacion):
    postulacion = postulacion_service.get_postulacion_by_id(id_postulacion)
    alumno = alumno_service.get_alumno_by_id(postulacion.id_informacion_alumno_entrante)
    motivo = request.form.get('reject_reason')
    if not motivo:
        flash('El motivo de rechazo es obligatorio.', 'danger')
        return redirect(url_for('postulacion.ver_postulacion', id_postulacion=postulacion.id))
    else:
        postulacion_service.actualizar_estado_postulacion(postulacion, "Solicitud Rechazada")
        titulo = "Solicitud de Postulacion Rechazada"
        cuerpo = f"Su solicitud de postulacion ha sido rechazada. El motivo de rechazo es: {motivo}"
        destino = alumno.email
        email_service.send_email(titulo, cuerpo, [destino])
        flash('Solicitud de postulacion rechazada', 'danger')
        return redirect(url_for('postulacion.listar_solicitudes_de_postulacion'))


@postulacion_bp.get('/listar_solicitudes_de_postulacion')
@check("solicitud_postulacion_listar")
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

@postulacion_bp.get('/descargar_archivo/<filename>')
@check("archivo_descargar")
def descargar_archivo(filename):
    return archivo_service.descargar_archivo(filename)
    

@postulacion_bp.get('/mis_postulaciones')
@check("alumno")
def mis_postulaciones():
    id_alumno = None
    if get_rol_sesion(session) == "alumno":
        usuario = usuario_service.buscar_usuario(get_id_sesion(session))
        id_alumno = usuario.id_alumno   

    fecha_desde = request.args.get("fecha_desde")
    fecha_hasta = request.args.get("fecha_hasta")
    estado = request.args.get("estado")
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = 10

    
    postulaciones = postulacion_service.filtrar_postulaciones_por_alumno(
        estado,
        pagina,
        por_pagina,
        fecha_desde,
        fecha_hasta,
        id_alumno
    )

    estados = estado_postulacion_service.listar_estados()

    return render_template("postulaciones/mis_postulaciones.html", postulaciones=postulaciones, estados=estados)

@postulacion_bp.route('/toggle_inscripciones', methods=['GET', 'POST'])
@check("habilitar_periodo_postulacion")
def periodo_postulacion_toggle():

    periodos = None
    print(request.method)
    if request.method == 'POST':
        periodo_actual = periodo_postulacion_service.periodo_actual()
        if periodo_actual:
            periodo_postulacion_service.deshabilitar_periodo_postulacion()
        else:
            #fecha_desde = request.form.get("fecha_desde")
            #periodo_postulacion_service.habilitar_periodo_postulacion(fecha_desde)
            periodo_postulacion_service.habilitar_periodo_postulacion()
        time.sleep(0.2)  # TODO. Forma berreta de asegurarme que la lista se actualiza para cuando haga el redirect
        return redirect(url_for('postulacion.periodo_postulacion_toggle'))
    else:
        fecha_desde = request.args.get("fecha_desde")
        fecha_hasta = request.args.get("fecha_hasta")
        orden = request.args.get("orden", "desc")
        pagina = request.args.get("pagina", 1, type=int)
        por_pagina = 10

        periodos = periodo_postulacion_service.listar_periodos_postulacion(fecha_desde, fecha_hasta, pagina, por_pagina, orden)
    return render_template('postulaciones/toggle_inscripciones.html', periodos=periodos)

@postulacion_bp.get('/repostulacion')
#@check("alumno")
def repostulacion():
    form = PostulacionForm()
    return render_template('postulaciones/repostulacion.html', form=form)

@postulacion_bp.get('/ingresar_datos_estadia/<int:id_postulacion>')
#@check("alumno")
def ingresar_datos_estadia(id_postulacion):
    form = PostulacionEstadiaForm()
    return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)

@postulacion_bp.post('/guardar_datos_estadia/<int:id_postulacion>')
#@check("alumno")
def guardar_datos_estadia(id_postulacion):
    form = PostulacionEstadiaForm()
    if not form.validate_on_submit():
        flash('Error al cargar los datos', 'danger')
        return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)
    
    if not form.psicofisico.data:
        flash('El archivo psicofisico es obligatorio', 'danger')
        return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)
    
    if not form.politicas_institucionales.data:
        flash('El archivo de politicas institucionales es obligatorio', 'danger')
        return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)
    
    if not form.fecha_ingreso.data:
        flash('La fecha de ingreso es obligatoria', 'danger')
        return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)
    
    if not form.duracion_estadia.data:
        flash('La duracion de la estadia es obligatoria', 'danger')
        return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)
    
    postulacion = postulacion_service.get_postulacion_by_id(id_postulacion)
    alumno = postulacion.informacion_alumno_entrante
    psicofisico = form.psicofisico.data
    print(f"El archivo psicofisico se sube así: {psicofisico.filename}")
    path_psicofisico = f"{id_postulacion}_{alumno.id}_psicofisico_{psicofisico.filename}"
    archivo_psicofisico = {
        "titulo": psicofisico.filename,
        "path": path_psicofisico,
        "id_postulacion": id_postulacion,
        "id_informacion_alumno_entrante": alumno.id
    }

    try:
        archivo_psicofisico = archivo_schema.load(archivo_psicofisico)
    except Exception as err:
        print(err)
        flash('Error al cargar el archivo psicofisico', 'danger')
        return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)
    
    politicas_institucionales = form.politicas_institucionales.data
    print(f"El archivo politicas institucionales se sube así: {politicas_institucionales}")
    path_politicas_institucionales = f"{id_postulacion}_{alumno.id}_politicasI_{politicas_institucionales.filename}"
    archivo_politicas = {
        "titulo": politicas_institucionales.filename,
        "path": path_politicas_institucionales,
        "id_postulacion": id_postulacion,
        "id_informacion_alumno_entrante": alumno.id
    }

    try:
        archivo_politicas = archivo_schema.load(archivo_politicas)
    except Exception as err:
        print(err)
        flash('Error al cargar el archivo de politicas institucionales', 'danger')
        return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)
    
    alumno.discapacidad = form.discapacidad.data
    if form.discapacidad.data == True and form.certificado_discapacidad.data:
        certificado_discapacidad = form.certificado_discapacidad.data
        print(f"El archivo certificado de discapacidad se sube así: {certificado_discapacidad.filename}")
        path_certificado_discapacidad = f"{id_postulacion}_{alumno.id}_certificadoDiscapacidad_{certificado_discapacidad.filename}"
        archivo_certificado_discapacidad = {
            "titulo": certificado_discapacidad.filename,
            "path": path_certificado_discapacidad,
            "id_postulacion": id_postulacion,
            "id_informacion_alumno_entrante": alumno.id
        }
        try:
            archivo_certificado_discapacidad = archivo_schema.load(archivo_certificado_discapacidad)
        except Exception as err:
            print(err)
            flash('Error al cargar el archivo de certificado de discapacidad', 'danger')
            return render_template('postulaciones/postulacion_estadia.html', form=form, id_postulacion=id_postulacion)

    postulacion.fecha_ingreso = form.fecha_ingreso.data
    postulacion.duracion_estadia = form.duracion_estadia.data

    if form.consulado_visacion.data != "":
        postulacion.consulado_visacion = form.consulado_visacion.data
   
    db.session.commit()
    archivo_service.crear_archivo(**archivo_psicofisico)
    archivo_service.crear_archivo(**archivo_politicas)

    if form.discapacidad.data == True and form.certificado_discapacidad.data:
        archivo_service.crear_archivo(**archivo_certificado_discapacidad)
        archivo_service.save_file_minio(request.files['certificado_discapacidad'].read(), archivo_certificado_discapacidad['path'])
    
    archivo_service.save_file_minio(request.files['psicofisico'].read(), archivo_psicofisico['path'])
    archivo_service.save_file_minio(request.files['politicas_institucionales'].read(), archivo_politicas['path'])
    print(f"El archivo se sube así: {psicofisico}")
    flash('Datos guardados exitosamente', 'success')
    return redirect(url_for('postulacion.mis_postulaciones'))
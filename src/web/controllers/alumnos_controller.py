from flask import Blueprint, request, render_template, session, flash, redirect, url_for
from src.core.services import alumno_service, archivo_service, usuario_service, email_service, paises_service, pasaporte_service, cedula_de_identidad_service
from src.web.handlers.auth import get_rol_sesion, get_id_sesion
from src.web.handlers.permisos import check
from src.web.forms import AlumnoForm
from src.core.database import db


alumnos_bp = Blueprint("alumnos_bp", __name__, url_prefix="/alumnos")


@alumnos_bp.get("/")
@check("alumnos_listar")
def listar_alumnos():

    """
    faltudad = None
    if get_rol_sesion(session) == "punto_focal":
        id_punto_focal = get_id_sesion(session)
        facultad = usuario_service.buscar_usuario(id_punto_focal)
        # NECESITO SABER LA FACULTAD DEL PUNTO FOCAL 
    """
    
    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")
    email = request.args.get("email")
    pagina = request.args.get("pagina", 1, type=int)
    ordenado_por = request.args.get("ordenado_por", "nombre")
    orden = request.args.get("orden", "asc")
    por_pagina = 5

    alumnos = alumno_service.filtrar_alumnos(
        nombre,
        apellido,
        email,
        pagina,
        ordenado_por,
        orden,
        por_pagina
    )

    return render_template("alumnos/listar-alumnos.html", alumnos=alumnos)


@alumnos_bp.get("ver-detalle-alumno/<int:id_alumno>")
@check("alumnos_detalle")
def ver_detalle_alumno(id_alumno):
    
    alumno = alumno_service.get_alumno_by_id(id_alumno)
    return render_template("alumnos/ver-detalle-alumno.html", alumno=alumno)


@alumnos_bp.get("solicitar-edicion/<int:id_alumno>")
@check("alumno")
@check("alumnos_editar")
def solicitar_edicion(id_alumno):

    alumno = alumno_service.get_alumno_by_id(id_alumno)
    return render_template("alumnos/solicitar-edicion.html", alumno=alumno)


@alumnos_bp.post("solicitar-edicion/<int:id_alumno>/")
@check("alumno")
@check("alumnos_editar")
def enviar_solicitud_edicion(id_alumno):

    alumno = alumno_service.get_alumno_by_id(id_alumno)

    # Capturar los datos del formulario
    info_personal = request.form.get('informacion_personal', '').strip()
    info_ubicacion = request.form.get('informacion_ubicacion', '').strip()
    documentos = request.form.get('documentos', '').strip()


    # Verificar si al menos una sección tiene datos para modificar
    if not info_personal and not info_ubicacion and not documentos:
        flash('Debe especificar al menos una sección para modificar.', 'danger')
        return render_template("alumnos/solicitar-edicion.html", alumno=alumno)
    
    titulo = f"Solicitud de edición de datos para el alumno {alumno.nombre} {alumno.apellido}"

    # Formatear el mensaje
    mensaje = f"{alumno.nombre} {alumno.apellido} ha solicitado la edición de los siguientes datos:\n\n"

    mensaje += "Información Personal:\n"
    mensaje += info_personal if info_personal else "No se han especificado modificaciones."
    mensaje += "\n\n"

    mensaje += "Información de Ubicación:\n"
    mensaje += info_ubicacion if info_ubicacion else "No se han especificado modificaciones."
    mensaje += "\n\n"

    mensaje += "Documentos Asociados:\n"
    mensaje += documentos if documentos else "No se han especificado modificaciones."
    mensaje += "\n\n"

    mensaje += f"Para revisar la solicitud, en primer lugar inicie sesión en el sistema como Usuario Presidencia Jefe y luego haga clic en el siguiente enlace: {url_for('alumnos_bp.editar_alumno', id_alumno=id_alumno, _external=True)}"

    destinatario = ["joaquinmgonzalez16@outlook.com"]

    email_service.send_email(titulo, mensaje, destinatario)

    flash('La solicitud de edición ha sido enviada con éxito.', 'success')
    return redirect(url_for('alumnos_bp.ver_detalle_alumno', id_alumno=id_alumno))


@alumnos_bp.get("editar-alumno/<int:id_alumno>")
@check("admin")
@check("alumnos_editar")
def editar_alumno(id_alumno):

    alumno = alumno_service.get_alumno_by_id(id_alumno)
    form = AlumnoForm(alumno=alumno)  # Pasando el objeto alumno al formulario

    form.pais_de_nacimiento.data = alumno.pais_de_nacimiento.id

    return render_template('alumnos/editar_alumno.html', form=form, alumno=alumno)


@alumnos_bp.post("editar-alumno/<int:id_alumno>")
@check("admin")
@check("alumnos_editar")
def actualizar_alumno(id_alumno):
    #hago post y actualizo la info
    pass


@alumnos_bp.post("alumnos/eliminar-alumno/<int:id_alumno>")
def eliminar_alumno(id_alumno):
    pass
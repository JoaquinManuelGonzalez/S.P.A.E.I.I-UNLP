from flask import Blueprint, request, render_template, session, flash, redirect, url_for
from src.core.services import alumno_service, archivo_service, usuario_service, email_service, paises_service, pasaporte_service, cedula_de_identidad_service
from src.web.handlers.auth import get_rol_sesion, get_id_sesion
from src.web.handlers.permisos import check
from src.web.forms import AlumnoForm
from src.core.database import db


alumnos_bp = Blueprint("alumnos_bp", __name__, url_prefix="/alumnos")


@alumnos_bp.get("/")
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
    form = AlumnoForm(obj=alumno)

    form.numero_pasaporte.data = alumno.pasaporte.numero if alumno.pasaporte else 123
    form.pais_emision_pasaporte.data = alumno.pasaporte.pais if alumno.pasaporte else 123
    form.numero_cedula.data = alumno.cedula_de_identidad.numero if alumno.cedula_de_identidad else paises_service.get_pais_by_id(1)
    form.pais_emision_cedula.data = alumno.cedula_de_identidad.pais if alumno.cedula_de_identidad else paises_service.get_pais_by_id(1)

    """
    # Pre-cargar datos de pasaporte y cédula si existen
    if alumno.pasaporte:
        form.numero_pasaporte.data = alumno.pasaporte.numero
        form.pais_emision_pasaporte.data = alumno.pasaporte.pais
    if alumno.cedula_de_identidad:
        form.numero_cedula.data = alumno.cedula_de_identidad.numero
        form.pais_emision_cedula.data = alumno.cedula_de_identidad.pais
    

    if form.validate_on_submit():
        # Actualizar información del alumno
        form.populate_obj(alumno)

        # Actualizar pasaporte si cambia el número o el país
        if form.numero_pasaporte.data and form.pais_emision_pasaporte.data:
            if (alumno.pasaporte is None or 
                alumno.pasaporte.numero != form.numero_pasaporte.data or 
                alumno.pasaporte.pais != form.pais_emision_pasaporte.data):
                if alumno.pasaporte is None:
                    alumno.pasaporte = pasaporte_service.crear_pasaporte(
                        numero=form.numero_pasaporte.data,
                        pais=form.pais_emision_pasaporte.data
                    )
                alumno.pasaporte.numero = form.numero_pasaporte.data
                alumno.pasaporte.pais = form.pais_emision_pasaporte.data

        # Actualizar cédula de identidad si cambia el número o el país
        if form.numero_cedula.data and form.pais_emision_cedula.data:
            if (alumno.cedula_de_identidad is None or 
                alumno.cedula_de_identidad.numero != form.numero_cedula.data or 
                alumno.cedula_de_identidad.pais != form.pais_emision_cedula.data):
                if alumno.cedula_de_identidad is None:
                    alumno.cedula_de_identidad = CedulaDeIdentidad()
                alumno.cedula_de_identidad.numero = form.numero_cedula.data
                alumno.cedula_de_identidad.pais = form.pais_emision_cedula.data
                
        db.session.commit()
        flash('Información del alumno actualizada correctamente.', 'success')
        return redirect(url_for('listar_alumnos'))
        """


    return render_template('editar_alumno.html', form=form)


@alumnos_bp.post("editar-alumno/<int:id_alumno>")
@check("admin")
@check("alumnos_editar")
def actualizar_alumno(id_alumno):
    #hago post y actualizo la info
    pass


@alumnos_bp.post("eliminar-alumno/<int:id_alumno>")
def eliminar_alumno(id_alumno):
    pass
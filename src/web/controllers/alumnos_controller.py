from flask import Blueprint, request, render_template, session, flash, redirect, url_for
from src.core.services import (
    alumno_service,
    archivo_service,
    usuario_service,
    email_service,
    paises_service,
    pasaporte_service,
    cedula_de_identidad_service,
    genero_service,
    estado_civil_service,
)
from src.web.handlers.auth import get_rol_sesion, get_id_sesion
from src.web.handlers.permisos import check
from src.web.forms import AlumnoForm, PasaporteForm, CedulaForm

from src.core.database import db


alumnos_bp = Blueprint("alumnos_bp", __name__, url_prefix="/alumnos")


@alumnos_bp.get("/")
@check("alumnos_listar")
def listar_alumnos():

    facultad = None
    if get_rol_sesion(session) == "punto_focal":
        usuario = usuario_service.buscar_usuario(get_id_sesion(session))
        facultad = usuario.facultad_id

    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")
    email = request.args.get("email")
    pagina = request.args.get("pagina", 1, type=int)
    ordenado_por = request.args.get("ordenado_por", "nombre")
    orden = request.args.get("orden", "asc")
    por_pagina = 5

    alumnos = alumno_service.filtrar_alumnos(
        nombre, apellido, email, pagina, ordenado_por, orden, por_pagina, facultad
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


@alumnos_bp.post("solicitar-edicion/<int:id_alumno>")
@check("alumno")
@check("alumnos_editar")
def enviar_solicitud_edicion(id_alumno):
    alumno = alumno_service.get_alumno_by_id(id_alumno)

    # Capturar los datos del formulario
    info_personal = request.form.get("informacion_personal", "").strip()
    info_ubicacion = request.form.get("informacion_ubicacion", "").strip()
    documentos = request.form.get("documentos", "").strip()
    archivos = {
        "foto_pasaporte": request.files.get("foto_pasaporte"),
        "cedula_identidad": request.files.get("cedula_identidad"),
        "certificado_espanol": request.files.get("certificado_espanol"),
        "certificado_discapacidad": request.files.get("certificado_discapacidad"),
    }

    # Si no se selecciona ningún archivo, asignarles None
    for nombre_archivo, archivo in archivos.items():
        if archivo.filename == "":
            archivos[nombre_archivo] = None

    # Verificar si al menos una sección tiene datos para modificar
    if not info_personal and not info_ubicacion and not any(archivos.values()):
        flash("Debe especificar al menos una sección para modificar.", "danger")
        return render_template("alumnos/solicitar-edicion.html", alumno=alumno)

    titulo = f"Solicitud de edición de datos para el alumno {alumno.nombre} {alumno.apellido}"

    # Formatear el mensaje
    mensaje = f"{alumno.nombre} {alumno.apellido} ha solicitado la edición de los siguientes datos:\n\n"

    mensaje += "Información Personal:\n"
    mensaje += (
        info_personal if info_personal else "No se han especificado modificaciones."
    )
    mensaje += "\n\n"

    mensaje += "Información de Ubicación:\n"
    mensaje += (
        info_ubicacion if info_ubicacion else "No se han especificado modificaciones."
    )
    mensaje += "\n\n"

    mensaje += "Documentos Asociados:\n"
    mensaje += documentos if documentos else "No se han especificado modificaciones."
    mensaje += "\n\n"

    # Variables para los archivos
    foto_pasaporte = None
    foto_cedula = None
    certificado_b1 = None
    certificado_discapacidad = None

    # Procesar los archivos adjuntos
    if request.files["foto_pasaporte"].filename != "":
        foto_pasaporte = request.files["foto_pasaporte"]
        foto_pasaporte_filename = foto_pasaporte.filename
    else:
        foto_pasaporte_filename = "No se han especificado modificaciones."

    if request.files["cedula_identidad"].filename != "":
        foto_cedula = request.files["cedula_identidad"]
        foto_cedula_filename = foto_cedula.filename
    else:
        foto_cedula_filename = "No se han especificado modificaciones."

    if request.files["certificado_espanol"].filename != "":
        certificado_b1 = request.files["certificado_espanol"]
        certificado_b1_filename = certificado_b1.filename
    else:
        certificado_b1_filename = "No se han especificado modificaciones."

    if request.files["certificado_discapacidad"].filename != "":
        certificado_discapacidad = request.files["certificado_discapacidad"]
        certificado_discapacidad_filename = certificado_discapacidad.filename
    else:
        certificado_discapacidad_filename = "No se han especificado modificaciones."

    # Agregar los archivos al mensaje
    mensaje += "Archivos Asociados a la Información Personal:\n"
    mensaje += f"Foto o Archivo de Pasaporte: {foto_pasaporte_filename}\n"
    mensaje += f"Foto o Archivo de Cédula de Identidad: {foto_cedula_filename}\n"
    mensaje += f"Foto o Archivo de Certificado B1 o superior de Español: {certificado_b1_filename}\n"
    mensaje += f"Foto o Archivo de Certificado de Discapacidad: {certificado_discapacidad_filename}\n\n"

    mensaje += f"Para revisar la solicitud, en primer lugar inicie sesión en el sistema como Usuario Presidencia Jefe y luego haga clic en el siguiente enlace: {url_for('alumnos_bp.editar_alumno', id_alumno=id_alumno, _external=True)}"

    # Crear lista de archivos a adjuntar
    archivos = []

    # Comprobar si hay archivos y agregar a la lista
    if foto_pasaporte_filename != "No se han especificado modificaciones.":
        archivos.append(foto_pasaporte)
    if foto_cedula_filename != "No se han especificado modificaciones.":
        archivos.append(foto_cedula)
    if certificado_b1_filename != "No se han especificado modificaciones.":
        archivos.append(certificado_b1)
    if certificado_discapacidad_filename != "No se han especificado modificaciones.":
        archivos.append(certificado_discapacidad)

    destinatario = ["joaquinmgonzalez16@outlook.com"]

    email_service.send_email(titulo, mensaje, destinatario, archivos)

    flash("La solicitud de edición ha sido enviada con éxito.", "success")
    return redirect(url_for("alumnos_bp.ver_detalle_alumno", id_alumno=id_alumno))


@alumnos_bp.get("editar-alumno/<int:id_alumno>")
@check("admin")
@check("alumnos_editar")
def editar_alumno(id_alumno):

    alumno = alumno_service.get_alumno_by_id(id_alumno)

    archivos = {
        "Pasaporte": (
            archivo_service.obtener_archivo_por_id(alumno.pasaporte.id_archivo)
            if alumno.pasaporte
            else "No posee información asociada."
        ),
        "Cédula de Identidad": (
            archivo_service.obtener_archivo_por_id(
                alumno.cedula_de_identidad.id_archivo
            )
            if alumno.cedula_de_identidad
            else "No posee información asociada."
        ),
        "Certificado B1": archivo_service.obtener_archivo_por_palabra_clave(
            (alumno.archivos), "certificadoB1"
        ),
        "Certificado de Discapacidad": archivo_service.obtener_archivo_por_palabra_clave(
            (alumno.archivos), "certificadoDiscapacidad"
        ),
    }

    form = AlumnoForm(obj=alumno)
    form_pasaporte = PasaporteForm(obj=alumno.pasaporte)
    form_cedula = CedulaForm(obj=alumno.cedula_de_identidad)

    return render_template(
        "alumnos/editar_alumno.html",
        form=form,
        alumno=alumno,
        form_pasaporte=form_pasaporte,
        form_cedula=form_cedula,
        archivos=archivos,
    )


@alumnos_bp.get("editar-alumno/ver-archivo/<int:id_archivo>")
def ver_archivo(id_archivo):
    archivo = archivo_service.obtener_archivo_por_id(id_archivo)
    url = archivo_service.generar_url_firmada(archivo)
    return redirect(url)


@alumnos_bp.post("editar-alumno/<int:id_alumno>")
@check("admin")
@check("alumnos_editar")
def actualizar_alumno(id_alumno):

    alumno = alumno_service.get_alumno_by_id(id_alumno)
    form = AlumnoForm(obj=alumno)
    form_pasaporte = PasaporteForm(obj=alumno.pasaporte)
    form_cedula = CedulaForm(obj=alumno.cedula_de_identidad)
    usuario = usuario_service.buscar_usuario_email(alumno.email)

    if form_pasaporte.validate_on_submit():
        numero_pasaporte = form_pasaporte.numero.data
        pais_emision_pasaporte = paises_service.get_pais_by_id(
            form_pasaporte.id_pais_emision.data
        )
        if (alumno.pasaporte.numero != numero_pasaporte) or (not alumno.pasaporte):
            if pasaporte_service.check_numero(numero_pasaporte):
                flash(
                    "El número de pasaporte ingresado ya está registrado para otro Alumno Entrante.",
                    "danger",
                )
                return render_template(
                    "alumnos/editar_alumno.html",
                    form=form,
                    alumno=alumno,
                    form_pasaporte=form_pasaporte,
                    form_cedula=form_cedula,
                )
        if alumno.pasaporte:
            pasaporte_service.actualizar_pasaporte(
                alumno.pasaporte, numero_pasaporte, pais_emision_pasaporte
            )
        else:
            pasaporte_service.crear_pasaporte(
                alumno, numero_pasaporte, pais_emision_pasaporte
            )

    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        fecha_de_nacimiento = form.fecha_de_nacimiento.data
        genero = genero_service.get_genero_by_id(form.id_genero.data)
        estado_civil = estado_civil_service.get_estado_civil_by_id(
            form.id_estado_civil.data
        )
        discapacitado = form.discapacitado.data
        pais_de_nacimiento = paises_service.get_pais_by_id(
            form.id_pais_de_nacimiento.data
        )
        pais_de_residencia = paises_service.get_pais_by_id(
            form.id_pais_de_residencia.data
        )
        pais_de_nacionalidad = paises_service.get_pais_by_id(
            form.id_pais_nacionalidad.data
        )
        domicilio_pais_de_residencia = form.domicilio_pais_de_residencia.data
        numero_pasaporte = (
            form.numero_pasaporte.data if form.numero_pasaporte.data else None
        )
        numero_cedula = form.numero_cedula.data if form.numero_cedula.data else None
        pais_emision_pasaporte = (
            paises_service.get_pais_by_id(form.id_pais_emision_pasaporte.data)
            if form.id_pais_emision_pasaporte.data
            else None
        )
        pais_emision_cedula = (
            paises_service.get_pais_by_id(form.id_pais_emision_cedula.data)
            if form.id_pais_emision_cedula.data
            else None
        )

        if alumno.email != email:
            if alumno_service.check_email(email):
                flash(
                    "El email ingresado ya está registrado para otro Alumno Entrante.",
                    "danger",
                )
                return render_template(
                    "alumnos/editar_alumno.html", form=form, alumno=alumno
                )
        if alumno.pasaporte:
            if alumno.pasaporte.numero != numero_pasaporte:
                if pasaporte_service.check_numero(numero_pasaporte):
                    flash(
                        "El número de pasaporte ingresado ya está registrado para otro Alumno Entrante.",
                        "danger",
                    )
                    return render_template(
                        "alumnos/editar_alumno.html", form=form, alumno=alumno
                    )
        if alumno.cedula_de_identidad:
            if alumno.cedula_de_identidad.numero != numero_cedula:
                if cedula_de_identidad_service.check_numero(numero_cedula):
                    flash(
                        "El número de cédula de identidad ingresado ya está registrado para otro Alumno Entrante.",
                        "danger",
                    )
                    return render_template(
                        "alumnos/editar_alumno.html", form=form, alumno=alumno
                    )

        alumno = alumno_service.actualizar_informacion_alumno(
            alumno,
            nombre,
            apellido,
            email,
            fecha_de_nacimiento,
            genero,
            estado_civil,
            discapacitado,
            pais_de_nacimiento,
            pais_de_residencia,
            pais_de_nacionalidad,
            domicilio_pais_de_residencia,
        )

        usuario_service.actualizar_informacion_usuario_alumno(
            usuario, alumno.nombre, alumno.apellido, alumno.email
        )
        titulo = (
            f"Actualización de datos para el alumno {alumno.nombre} {alumno.apellido}"
        )
        mensaje = f"Se han actualizado sus datos personales en el sistema de acuerdo a las modificaciones solicitadas. Si desea realizar más cambios, por favor, realice una nueva Solicitud de Edición de Datos Personales."
        destinatario = [alumno.email]
        email_service.send_email(titulo, mensaje, destinatario)
    else:
        # Obtener el primer campo con error
        first_error_field = next(iter(form.errors))
        # Primer error del campo
        first_error_message = form.errors[first_error_field][0]
        # Mostrar el error
        flash(
            f"Error en el campo {getattr(form, first_error_field).label.text}: {
              first_error_message}",
            "danger",
        )
        return render_template("alumnos/editar_alumno.html", form=form, alumno=alumno)

    flash(
        "Los datos del Alumno Entrante han sido actualizados con éxito.",
        "success",
    )
    return render_template("alumnos/ver-detalle-alumno.html", alumno=alumno)


@alumnos_bp.post("alumnos/eliminar-alumno/<int:id_alumno>")
def eliminar_alumno(id_alumno):
    pass


@alumnos_bp.get("alumnos/ver-documentacion/<int:id_alumno>")
def ver_documentacion(id_alumno):
    pass

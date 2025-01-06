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


alumnos_bp = Blueprint("alumnos_bp", __name__, url_prefix="/alumnos")


@alumnos_bp.get("/")
@check("alumnos_listar")
def listar_alumnos():
    """
    Listar alumnos con filtros y paginación.
    Esta función obtiene los parámetros de filtro y paginación de la solicitud HTTP,
    filtra los alumnos según los parámetros proporcionados y devuelve una plantilla HTML
    con la lista de alumnos.
    Parámetros de solicitud:
        - nombre (str): Nombre del alumno a filtrar (opcional).
        - apellido (str): Apellido del alumno a filtrar (opcional).
        - email (str): Email del alumno a filtrar (opcional).
        - pagina (int): Número de página para la paginación (opcional, por defecto 1).
        - ordenado_por (str): Campo por el cual ordenar los resultados (opcional, por defecto "nombre").
        - orden (str): Orden de los resultados, ascendente ("asc") o descendente ("desc") (opcional, por defecto "asc").
    Retorna:
        str: Renderiza la plantilla HTML 'alumnos/listar-alumnos.html' con la lista de alumnos filtrados.
    """

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
    """
    Muestra el detalle de un alumno específico.
    Args:
        id_alumno (int): El ID del alumno cuyo detalle se desea ver.
    Returns:
        str: Renderiza la plantilla HTML con los detalles del alumno y sus archivos asociados.
    La función obtiene la información del alumno a través de su ID y luego recupera los archivos asociados
    al alumno, como el pasaporte, cédula de identidad, certificado B1 y certificado de discapacidad. Si el 
    alumno no tiene información asociada a alguno de estos documentos, se indica que no posee información 
    asociada. Finalmente, se renderiza una plantilla HTML con los detalles del alumno y sus archivos.
    """

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

    return render_template(
        "alumnos/ver-detalle-alumno.html", alumno=alumno, archivos=archivos
    )


@alumnos_bp.get("solicitar-edicion/<int:id_alumno>")
@check("alumno")
@check("alumnos_editar")
def solicitar_edicion(id_alumno):
    """
    Solicita la edición de los datos de un alumno.
    Args:
        id_alumno (int): El ID del alumno cuyos datos se desean editar.
    Returns:
        Response: Una respuesta de renderización de la plantilla "solicitar-edicion.html" con los datos del alumno.
    """

    alumno = alumno_service.get_alumno_by_id(id_alumno)
    return render_template("alumnos/solicitar-edicion.html", alumno=alumno)


@alumnos_bp.post("solicitar-edicion/<int:id_alumno>")
@check("alumno")
@check("alumnos_editar")
def enviar_solicitud_edicion(id_alumno):
    """
    Envía una solicitud de edición de datos para un alumno específico.
    Args:
        id_alumno (int): El ID del alumno para el cual se solicita la edición de datos.
    Returns:
        Response: Redirige a la página de detalles del alumno o renderiza la página de solicitud de edición con un mensaje de error.
    Captura los datos del formulario y los archivos adjuntos, verifica que al menos una sección tenga datos para modificar,
    formatea un mensaje con la información proporcionada y envía un correo electrónico con la solicitud de edición.
    """

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

    destinatario = usuario_service.buscar_usuario(1).email

    email_service.send_email(titulo, mensaje, [destinatario], archivos)

    flash("La solicitud de edición ha sido enviada con éxito.", "success")
    return redirect(url_for("alumnos_bp.ver_detalle_alumno", id_alumno=id_alumno))


@alumnos_bp.get("editar-alumno/<int:id_alumno>")
@check("admin")
@check("alumnos_editar")
def editar_alumno(id_alumno):
    """
    Edita la información de un alumno específico.
    Args:
        id_alumno (int): El ID del alumno a editar.
    Returns:
        Response: Redirige a la página de edición del alumno con los formularios y archivos correspondientes,
                  o redirige a la lista de alumnos si el alumno no existe.
    Funcionalidad:
        - Obtiene el alumno por su ID.
        - Si el alumno no existe, muestra un mensaje de error y redirige a la lista de alumnos.
        - Obtiene los archivos asociados al alumno, incluyendo pasaporte, cédula de identidad,
          certificado B1 y certificado de discapacidad.
        - Crea formularios para editar la información del alumno, pasaporte y cédula de identidad.
        - Renderiza la plantilla de edición del alumno con los formularios y archivos obtenidos.
    """

    alumno = alumno_service.get_alumno_by_id(id_alumno)

    if not alumno:
        flash("El Alumno Entrante no existe.", "danger")
        return redirect(url_for("alumnos_bp.listar_alumnos"))

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
    form_pasaporte = PasaporteForm(prefix="pasaporte", obj=alumno.pasaporte)
    form_cedula = CedulaForm(prefix="cedula", obj=alumno.cedula_de_identidad)

    return render_template(
        "alumnos/editar_alumno.html",
        form=form,
        alumno=alumno,
        form_pasaporte=form_pasaporte,
        form_cedula=form_cedula,
        archivos=archivos,
    )


@alumnos_bp.get("editar-alumno/ver-archivo/<int:id_archivo>")
@check("archivo_descargar")
def ver_archivo(id_archivo):
    """
    Obtiene y descarga un archivo basado en su ID.

    Args:
        id_archivo (int): El ID del archivo a obtener y descargar.

    Returns:
        Response: La respuesta que contiene el archivo descargado.
    """

    archivo = archivo_service.obtener_archivo_por_id(id_archivo)
    return archivo_service.descargar_archivo(archivo.path)


@alumnos_bp.post("editar-alumno/<int:id_alumno>")
@check("admin")
@check("alumnos_editar")
def actualizar_alumno(id_alumno):
    """
    Actualiza la información de un alumno existente en el sistema.
    Parámetros:
    id_alumno (int): El ID del alumno a actualizar.
    Funcionalidad:
    - Obtiene la información del alumno por su ID.
    - Carga los formularios de edición de alumno, pasaporte y cédula de identidad.
    - Verifica y actualiza la información del pasaporte si se ha proporcionado.
    - Verifica y actualiza la información de la cédula de identidad si se ha proporcionado.
    - Verifica y actualiza la información personal del alumno si se ha proporcionado.
    - Envía un correo electrónico al alumno notificando la actualización de sus datos.
    - Muestra mensajes de error si hay campos faltantes o datos duplicados.
    Retorna:
    - Renderiza la plantilla de edición del alumno con los formularios y mensajes de error si hay problemas.
    - Redirige a la página de detalles del alumno si la actualización es exitosa.
    """

    alumno = alumno_service.get_alumno_by_id(id_alumno)
    form = AlumnoForm(obj=alumno)
    form_pasaporte = PasaporteForm(prefix="pasaporte", obj=alumno.pasaporte)
    form_cedula = CedulaForm(prefix="cedula", obj=alumno.cedula_de_identidad)
    usuario = usuario_service.buscar_usuario_email(alumno.email)
    archivos_originales = {
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
    archivos_nuevos = {
        "foto_pasaporte": request.files.get("filePasaporte"),
        "cedula_identidad": request.files.get("fileCedula"),
        "certificado_espanol": request.files.get("fileCertificadoB1"),
        "certificado_discapacidad": request.files.get("fileCertificadoDiscapacidad"),
    }

    # Si no se selecciona ningún archivo, asignarles None
    for nombre_archivo, archivo in archivos_nuevos.items():
        if archivo.filename == "":
            archivos_nuevos[nombre_archivo] = None

    if form_pasaporte.validate_on_submit():
        numero_pasaporte = form_pasaporte.numero.data
        pais_emision_pasaporte = paises_service.get_pais_by_id(
            form_pasaporte.id_pais.data
        )

        tiene_datos_pasaporte = (
            numero_pasaporte
            or pais_emision_pasaporte
            or archivos_nuevos["foto_pasaporte"]
            or (archivos_originales["Pasaporte"] != "No posee información asociada.")
        )
        datos_pasaporte_completos = (
            numero_pasaporte
            and pais_emision_pasaporte
            and (
                archivos_nuevos["foto_pasaporte"]
                or archivos_originales["Pasaporte"] != "No posee información asociada."
            )
        )

        if tiene_datos_pasaporte:
            if not datos_pasaporte_completos:
                flash(
                    "Un Pasaporte requiere de número, país de emisión y archivo asociado.",
                    "danger",
                )
                return render_template(
                    "alumnos/editar_alumno.html",
                    form=form,
                    alumno=alumno,
                    form_pasaporte=form_pasaporte,
                    form_cedula=form_cedula,
                    archivos=archivos_originales,
                )
            else:
                if (not alumno.pasaporte) or (
                    alumno.pasaporte.numero != numero_pasaporte
                ):
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
                            archivos=archivos_originales,
                        )
                if alumno.pasaporte:
                    if archivos_nuevos["foto_pasaporte"]:
                        filename = f"{alumno.id}_pasaporte_{archivos_nuevos['foto_pasaporte'].filename}"
                        pasaporte_service.actualizar_pasaporte_con_archivo(
                            alumno.pasaporte,
                            numero_pasaporte,
                            pais_emision_pasaporte,
                            archivos_nuevos["foto_pasaporte"],
                            filename,
                        )
                    else:
                        pasaporte_service.actualizar_informacion_pasaporte(
                            alumno.pasaporte, numero_pasaporte, pais_emision_pasaporte
                        )
                else:
                    filename = f"{alumno.id}_pasaporte_{archivos_nuevos['foto_pasaporte'].filename}"
                    nuevo_pasaporte = pasaporte_service.crear_pasaporte_desde_edicion(
                        numero_pasaporte,
                        pais_emision_pasaporte,
                        archivos_nuevos["foto_pasaporte"],
                        filename,
                    )
                    alumno_service.asignar_pasaporte_alumno(alumno, nuevo_pasaporte.id)

    if form_cedula.validate_on_submit():
        numero_cedula = form_cedula.numero.data
        pais_emision_cedula = paises_service.get_pais_by_id(form_cedula.id_pais.data)

        tiene_datos_cedula = (
            numero_cedula
            or pais_emision_cedula
            or archivos_nuevos["cedula_identidad"]
            or (
                archivos_originales["Cédula de Identidad"]
                != "No posee información asociada."
            )
        )
        datos_cedula_completos = (
            numero_cedula
            and pais_emision_cedula
            and (
                archivos_nuevos["cedula_identidad"]
                or archivos_originales["Cédula de Identidad"]
                != "No posee información asociada."
            )
        )

        if tiene_datos_cedula:
            if not datos_cedula_completos:
                flash(
                    "Una Cédula de Identidad requiere de número, país de emisión y archivo asociado.",
                    "danger",
                )
                return render_template(
                    "alumnos/editar_alumno.html",
                    form=form,
                    alumno=alumno,
                    form_pasaporte=form_pasaporte,
                    form_cedula=form_cedula,
                    archivos=archivos_originales,
                )
            else:
                if (not alumno.cedula_de_identidad) or (
                    alumno.cedula_de_identidad.numero != numero_cedula
                ):
                    if cedula_de_identidad_service.check_numero(numero_cedula):
                        flash(
                            "El número de cédula de identidad ingresado ya está registrado para otro Alumno Entrante.",
                            "danger",
                        )
                        return render_template(
                            "alumnos/editar_alumno.html",
                            form=form,
                            alumno=alumno,
                            form_pasaporte=form_pasaporte,
                            form_cedula=form_cedula,
                            archivos=archivos_originales,
                        )
                if alumno.cedula_de_identidad:
                    if archivos_nuevos["cedula_identidad"]:
                        filename = f"{alumno.id}_cedula_{archivos_nuevos['cedula_identidad'].filename}"
                        cedula_de_identidad_service.actualizar_cedula_con_archivo(
                            alumno.cedula_de_identidad,
                            numero_cedula,
                            pais_emision_cedula,
                            archivos_nuevos["cedula_identidad"],
                            filename,
                        )
                    else:
                        cedula_de_identidad_service.actualizar_informacion_cedula_de_identidad(
                            alumno.cedula_de_identidad,
                            numero_cedula,
                            pais_emision_cedula,
                        )
                else:
                    filename = f"{alumno.id}_cedula_{archivos_nuevos['cedula_identidad'].filename}"
                    nueva_cedula = (
                        cedula_de_identidad_service.crear_cedula_desde_edicion(
                            numero_cedula,
                            pais_emision_cedula,
                            archivos_nuevos["cedula_identidad"],
                            filename,
                        )
                    )
                    alumno_service.asignar_cedula_alumno(alumno, nueva_cedula.id)

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

        if alumno.email != email:
            if alumno_service.check_email(email):
                flash(
                    "El email ingresado ya está registrado para otro Alumno Entrante.",
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
    return redirect(url_for("alumnos_bp.ver_detalle_alumno", id_alumno=alumno.id))

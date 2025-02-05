from datetime import datetime
from flask import Blueprint, flash, redirect, request, render_template, url_for, send_file
from src.core.services import asignaturas as asignaturas_service
from src.core.services import postulacion_service
from src.core.services import archivo_service
from src.web.handlers.permisos import check
from weasyprint import HTML
import io


documentos_bp = Blueprint("documentos", __name__, url_prefix="/documentos")

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def hoy():
    t = datetime.now()
    return str(t.day) + " de " + str(MESES[t.month]) + " de " + str(t.year)

#-----Descargar certificad calificaciones-----
@documentos_bp.get('/certificado_calificaciones/<int:postulacion_id>')

def certificado_calificaciones(postulacion_id):

    previous_url = request.referrer

    postulacion = postulacion_service.get_postulacion_by_id(postulacion_id)

    if postulacion is None:
        flash("No existe la postulación.", "error")
        return redirect(previous_url)
    
    asignaturas = postulacion.asignaturas

    if asignaturas is None or len(asignaturas) == 0:
        flash("No se han elegido materias para esta postulación.", "error")
        return redirect(previous_url)
    
    notas_cerradas = True
    for a in asignaturas:
        if a.aprobado < 0:
            notas_cerradas = False
    
    if not notas_cerradas:
        flash("No se han cerrado las notas de todas las materias.", "error")
        return redirect(previous_url)

    periodo = ""
    if postulacion.periodo_postulacion.inicio.month < 7 and postulacion.periodo_postulacion.inicio.month > 1:
        periodo = "Agosto - Diciembre " + str(postulacion.periodo_postulacion.inicio.year)
    else:
        periodo = "Febrero - Julio " + str(postulacion.periodo_postulacion.inicio.year + 1)

    html_string = render_template("documentos/certificado_calificaciones.html", postulacion=postulacion, fecha_firma=hoy(), periodo=periodo)
    pdf_bytes = HTML(string=html_string).write_pdf()

    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype="application/pdf",
        as_attachment=True,
        download_name="certificado_calificaciones_" + postulacion.informacion_alumno_entrante.apellido + ".pdf"
    )

#-----Descargar carta de aceptacion-----
@documentos_bp.get('/carta_aceptacion/<int:postulacion_id>')

def carta_aceptacion(postulacion_id):

    previous_url = request.referrer

    postulacion = postulacion_service.get_postulacion_by_id(postulacion_id)

    if postulacion is None:
        flash("No existe la postulación.", "error")
        return redirect(previous_url)
    
    asignaturas = postulacion.asignaturas

    if asignaturas is None or len(asignaturas) == 0:
        flash("No se han elegido materias para esta postulación.", "error")
        return redirect(previous_url)
    
    materias_validadas = True
    for a in asignaturas:
        if not a.validado:
            materias_validadas = False
    
    if not materias_validadas:
        flash("No se han validado todas las materias seleccionadas.", "error")
        return redirect(previous_url)
    
    periodo = ""
    if postulacion.periodo_postulacion.inicio.month < 7 and postulacion.periodo_postulacion.inicio.month > 1:
        periodo = "Agosto - Diciembre " + str(postulacion.periodo_postulacion.inicio.year)
    else:
        periodo = "Febrero - Julio " + str(postulacion.periodo_postulacion.inicio.year + 1)

    html_string = render_template("documentos/carta_aceptacion.html", postulacion=postulacion, fecha_firma=hoy(), periodo=periodo)
    pdf_bytes = HTML(string=html_string).write_pdf()

    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype="application/pdf",
        as_attachment=True,
        download_name="carta_aceptacion_" + postulacion.informacion_alumno_entrante.apellido + ".pdf"
    )

@documentos_bp.get('/archivo_base/<path>')
def descargar_archivo_base(path):
    return archivo_service.descargar_archivo(path)
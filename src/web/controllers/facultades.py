from flask import Blueprint, flash, redirect, request, render_template, url_for
from src.core.services import facultades as facultades_service
from src.core.services import carreras as carreras_service
from src.core.services import asignaturas as asignaturas_service
from src.core.services import usuario_service as usuarios_service
from src.web.handlers.permisos import check


facultades_bp = Blueprint("facultades", __name__, url_prefix="/facultades")

#-----Listar-----
@facultades_bp.get('/')
@check("facultades_listar")
def listar():
    """Lista todas las facultades.

    Returns:
        flask.templating.render_template: Plantilla HTML con la lista de facultades.
    """

    query = request.args

    nombre = query.get('nombre', None)
    
    facultades = facultades_service.listar_facultades(nombre=nombre)
    return render_template("facultades/listar.html", facultades=facultades, nombre=nombre)

#-----Visualizar-----
@facultades_bp.get('/<int:facultad_id>')
@check("facultades_listar")
def visualizar(facultad_id):
    """Detalle de la facultad con id facultad_id.

    Returns:
        flask.templating.render_template: Plantilla HTML con el detalle de la facultad con id facultad_id.
    """
    
    query = request.args

    nombre_carrera = query.get('nombre_carrera', None)
    tipo_carrera_id = query.get('tipo_carrera_id', None)
    try:
        tipo_carrera_id = int(tipo_carrera_id)
    except (TypeError, ValueError):
        tipo_carrera_id = None

    carreras = carreras_service.get_carreras_filtradas(facultad_id=facultad_id, nombre=nombre_carrera, tipo_carrera_id=tipo_carrera_id)

    tipos_carrera = carreras_service.get_tipos_carrera()
    
    facultad = facultades_service.get_facultad_by_id(facultad_id=facultad_id)
    if facultad is None:
        flash("La facultad solicitada no existe o ha sido eliminada.", "error")
        return redirect(url_for("facultades.listar"))

    nombre_asignatura = query.get('nombre_asignatura', None)
    pagina_asignatura = request.args.get('pagina_asignatura', 1, type=int)

    asignaturas = asignaturas_service.get_asignaturas_cursadas_por_carreras(carreras_service.get_carreras_by_facultad(facultad_id), nombre=nombre_asignatura, pagina=pagina_asignatura)

    puntos_focales = usuarios_service.get_puntos_focales_by_facultad(facultad_id)

    return render_template("facultades/visualizar.html", facultad=facultad, 
                           carreras=carreras, nombre_carrera=nombre_carrera, tipo_carrera_id=tipo_carrera_id, tipos_carrera=tipos_carrera,
                           asignaturas=asignaturas, nombre_asignatura=nombre_asignatura, pagina_asignatura=pagina_asignatura,
                           puntos_focales=puntos_focales)
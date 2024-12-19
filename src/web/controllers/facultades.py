from flask import Blueprint, flash, redirect, request, render_template, url_for
from src.core.services import facultades as facultades_service
from src.core.services import carreras as carreras_service
from src.core.services import asignaturas as asignaturas_service
from src.core.services import usuario_service as usuarios_service


facultades_bp = Blueprint("facultades", __name__, url_prefix="/facultades")

#-----Listar-----
@facultades_bp.get('/')
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
def visualizar(facultad_id):
    """Detalle de la facultad con id facultad_id.

    Returns:
        flask.templating.render_template: Plantilla HTML con el detalle de la facultad con id facultad_id.
    """
    
    query = request.args

    nombre_asignatura = query.get('nombre_search_asignatura', None)
    
    facultad = facultades_service.get_facultad_by_id(facultad_id=facultad_id)
    if facultad is None:
        flash("La facultad solicitada no existe o ha sido eliminada.", "error")
        return redirect(url_for("facultades.listar"))
    
    carreras = carreras_service.get_carreras_by_facultad(facultad_id)

    pagina = request.args.get('pagina', 1, type=int)
    asignaturas = asignaturas_service.get_asignaturas_cursadas_por_carreras(carreras, nombre=nombre_asignatura, pagina=pagina)
    puntos_focales = usuarios_service.get_puntos_focales_by_facultad(facultad_id)

    return render_template("facultades/visualizar.html", facultad=facultad, carreras=carreras, 
                           asignaturas=asignaturas, nombre_asignatura=nombre_asignatura, 
                           puntos_focales=puntos_focales, pagina=pagina)
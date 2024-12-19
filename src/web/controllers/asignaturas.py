from flask import Blueprint, flash, redirect, request, render_template, url_for
from src.core.services import facultades as facultades_service
from src.core.services import carreras as carreras_service
from src.core.services import asignaturas as asignaturas_service
from src.core.services import usuario_service as usuarios_service
from src.web.forms import AsignaturaForm


asignaturas_bp = Blueprint("asignaturas", __name__, url_prefix="/asignaturas")

#-----Visualizar-----
@asignaturas_bp.get('/<int:asignatura_id>')
def visualizar(asignatura_id):
    """Detalle de la asignatura con id asignatura_id.

    Returns:
        flask.templating.render_template: Plantilla HTML con el detalle de la asignatura con id asignatura_id.
    """
    
    asignatura = asignaturas_service.get_asignatura_by_id(asignatura_id)
    if asignatura is None:
        flash("La asignatura no existe o ha sido eliminada.", "error")
        return redirect(url_for("facultades.listar"))
    return render_template("asignaturas/visualizar.html", asignatura=asignatura, carreras=asignatura.carreras)

#-----Crear-----
@asignaturas_bp.route("/crear", methods=['GET', 'POST'])
def crear():
    """Crea una Asignatura.

    Returns:
        flask.templating.render_template: Plantilla para crear una Asignatura.
    """

    formulario = AsignaturaForm()

    facultades = facultades_service.get_all_facultades()
    formulario.facultad_id.choices =  [("", "Seleccione una facultad")] + [(facultad.id, facultad.nombre) for facultad in facultades]
    
    if formulario.validate_on_submit():
        asignatura = asignaturas_service.crear_asignatura_web(formulario)
        return redirect(url_for("asignaturas.listado_asignar_carreras", asignatura_id = asignatura.id))
    return render_template("asignaturas/crear.html", formulario=formulario)

#-----Editar-----
@asignaturas_bp.route("/<int:asignatura_id>/editar", methods=['GET', 'POST'])
def editar(asignatura_id):
    """Edita una Asignatura.

    Returns:
        flask.templating.render_template: Plantilla para editar una Asignatura.
    """
    asignatura = asignaturas_service.get_asignatura_by_id(asignatura_id)
    formulario = AsignaturaForm(obj=asignatura)

    facultades = facultades_service.get_all_facultades()
    formulario.facultad_id.choices =  [("", "Seleccione una facultad")] + [(facultad.id, facultad.nombre) for facultad in facultades]
    if formulario.validate_on_submit():
        asignatura = asignaturas_service.editar_asignatura_web(asignatura_id,formulario)
        return redirect(url_for("asignaturas.visualizar", asignatura_id = asignatura.id))
    return render_template("asignaturas/editar.html", formulario=formulario, asignatura_id=asignatura_id)

#-----Eliminar-----
@asignaturas_bp.post("/<int:asignatura_id>/eliminar")
def eliminar(asignatura_id):
    """Elimina una Asignatura.

    Returns:
        flask.templating.render_template: Visualizacion de facultad de origen.
    """
    asignatura = asignaturas_service.get_asignatura_by_id(asignatura_id)
    pudo = asignaturas_service.delete_asignatura(asignatura_id)
    if pudo:
        flash('La asignatura se ha eliminado correctamente', 'success')
    else:
        flash('No se pudo eliminar la asignatura', 'error')

    return redirect(url_for("facultades.visualizar", facultad_id = asignatura.facultad_id))

#-----Asignar asignatura a carreras-----
@asignaturas_bp.get("/<int:asignatura_id>/asignar_carreras")
def listado_asignar_carreras(asignatura_id):
    """Renderiza el listado de carreras para asignar.

    Returns:
        flask.templating.render_template: Plantilla asignar la asignatura a carreras.
    """
    asignatura = asignaturas_service.get_asignatura_by_id(asignatura_id)
    search = request.args.get("search", None)
    search = search.strip().lower() if search else None
    facultad_id = request.args.get("facultad", None)
    try:
        facultad_id = int(facultad_id)
    except (TypeError, ValueError):
        facultad_id = None

    pagina = request.args.get('pagina', 1, type=int)
    carreras = carreras_service.get_carreras(nombre=search, facultad_id=facultad_id, asignatura_id=asignatura.id)

    facultades = facultades_service.get_all_facultades()
    return render_template("asignaturas/asignatura_carrera.html", facultades=facultades, carreras=carreras, search=search, facultad_id=facultad_id, pagina=pagina, asignatura=asignatura)

@asignaturas_bp.get("/<int:asignatura_id>/asignar_carreras/<int:carrera_id>")
def asignar_carrera(asignatura_id, carrera_id):
    """Relaciona una carrera con una materia.

    Returns:
        flask.templating.render_template: Plantilla asignar la asignatura a carreras.
    """

    pudo = asignaturas_service.relacionar_asignatura_carrera(asignatura_id, carrera_id)
    if pudo:
        flash('La asignatura se ha asignado a la carrera correctamente', 'success')
    else:
        flash('No se pudo asignar la asignatura', 'error')

    return redirect(url_for("asignaturas.listado_asignar_carreras", asignatura_id = asignatura_id))

@asignaturas_bp.post("/<int:asignatura_id>/desasignar_carreras/<int:carrera_id>")
def desasignar_carrera(asignatura_id, carrera_id):
    """Relaciona una carrera con una materia.

    Returns:
        flask.templating.render_template: Plantilla asignar la asignatura a carreras.
    """

    pudo = asignaturas_service.desrelacionar_asignatura_carrera(asignatura_id, carrera_id)
    if pudo:
        flash('La asignatura se ha desasignado a la carrera correctamente', 'success')
    else:
        flash('No se pudo desasignar la asignatura', 'error')

    return redirect(url_for("asignaturas.visualizar", asignatura_id = asignatura_id))
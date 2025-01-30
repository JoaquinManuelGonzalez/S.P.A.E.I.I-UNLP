from flask import Blueprint, flash, redirect, request, render_template, url_for
from src.core.services import facultades as facultades_service
from src.core.services import carreras as carreras_service
from src.core.services import asignaturas as asignaturas_service
from src.web.forms import CarreraForm
from src.web.handlers.permisos import check


carreras_bp = Blueprint("carreras", __name__, url_prefix="/carreras")

#-----Visualizar-----
@carreras_bp.get('/<int:carrera_id>')
@check("carreras_detalle")
def visualizar(carrera_id):
    """Detalle de la carrera con id carrera_id.

    Returns:
        flask.templating.render_template: Plantilla HTML con el detalle de la carrera con id carrera_id.
    """
    
    carrera = carreras_service.get_carrera_by_id(carrera_id)
    if carrera is None:
        flash("La carrera no existe o ha sido eliminada.", "error")
        return redirect(url_for("facultades.listar"))
    return render_template("carreras/visualizar.html", carrera=carrera, asignaturas=carrera.asignaturas)

#-----Crear-----
@carreras_bp.route("/crear", methods=['GET', 'POST'])
@check("carreras_crear")
def crear():
    """Crea una Carrera.

    Returns:
        flask.templating.render_template: Plantilla para crear una Carrera.
    """

    formulario = CarreraForm()

    facultades = facultades_service.get_all_facultades()
    formulario.facultad_id.choices =  [("", "Seleccione una facultad")] + [(facultad.id, facultad.nombre) for facultad in facultades]

    tipos_carrera = carreras_service.get_tipos_carrera()
    formulario.tipo_carrera_id.choices = [("", "Seleccione un tipo de carrera")] + [(tipo_carrera.id, tipo_carrera.nombre) for tipo_carrera in tipos_carrera]
    
    if formulario.validate_on_submit():
        carrera = carreras_service.crear_carrera_web(formulario)
        return redirect(url_for("carreras.listado_asignar_asignaturas", carrera_id = carrera.id))
    return render_template("carreras/crear.html", formulario=formulario)

#-----Editar-----
@carreras_bp.route("/editar/<int:carrera_id>", methods=['GET', 'POST'])
@check("carreras_editar")
def editar(carrera_id):
    """Edita una Asignatura.

    Returns:
        flask.templating.render_template: Plantilla para editar una Asignatura.
    """
    carrera = carreras_service.get_carrera_by_id(carrera_id)
    formulario = CarreraForm(obj=carrera)

    facultades = facultades_service.get_all_facultades()
    formulario.facultad_id.choices =  [("", "Seleccione una facultad")] + [(facultad.id, facultad.nombre) for facultad in facultades]

    tipos_carrera = carreras_service.get_tipos_carrera()
    formulario.tipo_carrera_id.choices = [("", "Seleccione un tipo de carrera")] + [(tipo_carrera.id, tipo_carrera.nombre) for tipo_carrera in tipos_carrera]
    
    if formulario.validate_on_submit():
        carrera = carreras_service.editar_carrera_web(carrera_id,formulario)
        return redirect(url_for("carreras.visualizar", carrera_id = carrera.id))
    return render_template("carreras/editar.html", formulario=formulario, carrera=carrera)

#-----Eliminar-----
@carreras_bp.post("/<int:carrera_id>/eliminar")
@check("carreras_eliminar")
def eliminar(carrera_id):
    """Elimina una Carrera.

    Returns:
        flask.templating.render_template: Visualizacion de facultad de origen.
    """

    previous_url = request.referrer

    carrera = carreras_service.get_carrera_by_id(carrera_id)
    pudo = carreras_service.delete_carrera(carrera_id)
    if pudo:
        flash('La carrera se ha eliminado correctamente', 'success')
    else:
        flash('No se pudo eliminar la carrera', 'error')

    return redirect(previous_url or url_for("facultades.visualizar", facultad_id = carrera.facultad_id))

#-----Asignar asignatura a carreras-----
@carreras_bp.get("/<int:carrera_id>/asignar_asignaturas")
@check("carreras_editar")
def listado_asignar_asignaturas(carrera_id):
    """Renderiza el listado de asignaturas para asignar.

    Returns:
        flask.templating.render_template: Plantilla asignar la carrera a asignaturas.
    """
    carrera = carreras_service.get_carrera_by_id(carrera_id)
    search = request.args.get("search", None)
    search = search.strip().lower() if search else None
    facultad_id = request.args.get("facultad", None)
    try:
        facultad_id = int(facultad_id)
    except (TypeError, ValueError):
        facultad_id = None

    if not (search or facultad_id):
        asignaturas = []
    else:
        asignaturas = asignaturas_service.get_asignaturas(nombre=search, facultad_id=facultad_id, carrera_id=carrera_id)

    facultades = facultades_service.get_all_facultades()
    return render_template("carreras/asignatura_carrera.html", facultades=facultades, asignaturas=asignaturas, search=search, facultad_id=facultad_id, carrera=carrera)

@carreras_bp.get("/<int:carrera_id>/asignar_carreras/<int:asignatura_id>")
@check("carreras_editar")
def asignar_asignatura(carrera_id, asignatura_id):
    """Relaciona una carrera con una materia.

    Returns:
        flask.templating.render_template: Plantilla asignar la carrera a asignaturas.
    """

    previous_url = request.referrer

    pudo = asignaturas_service.relacionar_asignatura_carrera(asignatura_id, carrera_id)
    if pudo:
        flash('La asignatura se ha asignado a la carrera correctamente', 'success')
    else:
        flash('No se pudo asignar la asignatura', 'error')

    return redirect(previous_url or url_for("carreras.listado_asignar_asignaturas", carrera_id=carrera_id))

@carreras_bp.post("/<int:carrera_id>/desasignar_carreras/<int:asignatura_id>")
@check("carreras_editar")
def desasignar_asignatura(carrera_id, asignatura_id):
    """Desrelaciona una carrera con una materia.

    Returns:
        flask.templating.render_template: Plantilla HTML con el detalle de la carrera con id carrera_id.
    """

    previous_url = request.referrer

    pudo = asignaturas_service.desrelacionar_asignatura_carrera(asignatura_id, carrera_id)
    if pudo:
        flash('La asignatura se ha desasignado a la carrera correctamente', 'success')
    else:
        flash('No se pudo desasignar la asignatura', 'error')

    return redirect(previous_url or url_for("carreras.visualizar", carrera_id = carrera_id))
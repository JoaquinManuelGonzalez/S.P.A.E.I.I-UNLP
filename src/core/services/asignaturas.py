from src.core.database import db
from datetime import datetime
from src.core.models.asignatura import Asignatura, asignaturas_carreras
from src.core.models.carrera import Carrera
from src.core.services import carreras as carreras_service
from src.web.forms import AsignaturaForm

def crear_asignatura_web(formulario: AsignaturaForm):
    return create_asignatura(nombre=formulario.nombre.data, facultad_id=formulario.facultad_id.data)

def create_asignatura(nombre: str, facultad_id: int, id_carreras = []) -> Asignatura:
    """Crea una nueva asignatura en la base de datos.

    Args:
        nombre (str): El nombre de la asignatura.
        facultad_id (int): El id de la facultad en la que se dicta la asignatura.
        id_carreras (list): Una lista de IDs de carreras a asociar.

    Returns:
        Asignatura: El objeto Asignatura recién creado.

    Raises:
        Exception: Si ocurre un error al crear la asignatura.
    """

    new_asignatura = Asignatura(nombre=nombre, facultad_id=facultad_id)
    new_asignatura.carreras = carreras_service.list_carreras(id_carreras)

    try:
        db.session.add(new_asignatura)
        db.session.commit()
        return new_asignatura
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating Asignatura: {e}")
    
def editar_asignatura_web(asignatura_id: int, formulario: AsignaturaForm):
    return edit_asignatura(asignatura_id=asignatura_id, nombre=formulario.nombre.data, facultad_id=formulario.facultad_id.data)

def edit_asignatura(asignatura_id: int, nombre: str, facultad_id: int) -> Asignatura:

    asignatura = get_asignatura_by_id(asignatura_id)
    asignatura.nombre = nombre
    asignatura.facultad_id = facultad_id

    try:
        db.session.add(asignatura)
        db.session.commit()
        return asignatura
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating Asignatura: {e}")

def get_asignatura_by_id(asignatura_id):
    """Obtiene una asignatura por su ID.

    Args:
        asignatura_id (int): El ID de la asignatura.

    Returns:
        Asignatura: El objeto Asignatura con el ID especificado, o None si no se encuentra.
    """

    return Asignatura.query.get(asignatura_id)

def get_asignatura_by_nombre_facultad(nombre, facultad_id):
    """Obtiene una asignatura por su nombre y su facultad.

    Args:
        nombre (str): El nombre de la asignatura.
        facultad_id (int): El id de la facultad en la que se cursa.

    Returns:
        Asignatura: El objeto Asignatura o None si no se encuentra.
    """

    return Asignatura.query.filter(Asignatura.nombre == nombre and Asignatura.facultad_id == facultad_id).first()

def get_asignaturas_by_carrera(carrera_id: int):
    """Obtiene todas las asignaturas cursadas por un estudiante de la carrera pasada por parámetro.

    Args:
        id_carrera (int): El ID de la carrera de la cual quiero las asignaturas.

    Returns:
        list: Una lista de objetos Asignatura.
    """

    return Asignatura.query.filter(Asignatura.carreras.any(id=carrera_id)).all()

def get_asignaturas_cursadas_en(facultad_id: int):
    """Obtiene todas las asignaturas que se cursan en la facultad pasada por parametro.

    Args:
        id_carrera (int): El ID de la carrera de la cual quiero las asignaturas.

    Returns:
        list: Una lista de objetos Asignatura.
    """

    return Asignatura.query.filter(Asignatura.facultad_id == facultad_id).all()

def get_asignaturas_cursadas_por_carreras(carreras, nombre, pagina):
    """Obtiene todas las asignaturas que se cursan en las carreras pasadas por parámetro.

    Args:
        carreras (list): Una lista de objetos Carrera.

    Returns:
        list: Una lista de objetos Asignatura únicos.
    """

    # Convertimos los objetos Carrera a IDs
    carrera_ids = [carrera.id for carrera in carreras]

    # Consulta para obtener todas las asignaturas asociadas a las carreras especificadas
    asignaturas = Asignatura.query.join(asignaturas_carreras) \
                               .filter(asignaturas_carreras.columns.carrera_id.in_(carrera_ids)) \
                               .distinct()
    
    if nombre and nombre != "":
        asignaturas = asignaturas.filter(Asignatura.nombre.ilike(f"%{nombre}%"))

    return asignaturas.paginate(page=pagina, per_page=5, error_out=False)

def delete_asignatura(asignatura_id):
    """Elimina una asignatura (soft delete).

    Args:
        asignatura_id (int): El ID de la asignatura a eliminar.

    Returns:
        bool: True si la asignatura se eliminó correctamente, False si no se encontró.
    """

    asignatura = Asignatura.query.get(asignatura_id)
    if asignatura:
        asignatura.deleted_at = datetime.now()
        db.session.commit()
        return True
    else:
        return False
    
def relacionar_asignatura_carrera(asignatura_id, carrera_id):

    asignatura = get_asignatura_by_id(asignatura_id)
    carrera = carreras_service.get_carrera_by_id(carrera_id)

    if carrera and asignatura:
        asignatura.carreras.append(carrera)
        db.session.add(asignatura)
        db.session.commit()
        return True
    else:
        return False
    
def desrelacionar_asignatura_carrera(asignatura_id, carrera_id):

    asignatura = get_asignatura_by_id(asignatura_id)
    carrera = carreras_service.get_carrera_by_id(carrera_id)

    if carrera and asignatura:
        asignatura.carreras.remove(carrera)
        db.session.add(asignatura)
        db.session.commit()
        return True
    else:
        return False
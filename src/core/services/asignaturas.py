from src.core.database import db
from datetime import datetime
from src.core.models.asignatura import Asignatura, asignaturas_carreras
from src.core.models.carrera import Carrera
from src.core.services import carreras as carreras_service


def create_asignatura(nombre, id_carreras):
    """Crea una nueva asignatura en la base de datos.

    Args:
        nombre (str): El nombre de la asignatura.
        id_carreras (list): Una lista de IDs de carreras a asociar.

    Returns:
        Asignatura: El objeto Asignatura recién creado.

    Raises:
        Exception: Si ocurre un error al crear la asignatura.
    """

    new_asignatura = Asignatura(nombre=nombre)
    new_asignatura.carreras = carreras_service.list_carreras(id_carreras)

    db.session.add(new_asignatura)
    db.session.commit()
    return new_asignatura

def get_asignatura_by_id(asignatura_id):
    """Obtiene una asignatura por su ID.

    Args:
        asignatura_id (int): El ID de la asignatura.

    Returns:
        Asignatura: El objeto Asignatura con el ID especificado, o None si no se encuentra.
    """

    return Asignatura.query.get(asignatura_id)

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

def get_asignaturas_cursadas_por_carreras(carreras):
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
                               .distinct() \
                               .all()

    return asignaturas

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
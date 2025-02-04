from sqlalchemy import and_, func, text
from src.core.database import db
from datetime import datetime
from src.core.models.carrera import Carrera, TipoCarrera
from src.core.models.asignatura import asignaturas_carreras
from src.web.forms import CarreraForm

def crear_carrera_web(formulario: CarreraForm):
    return create_carrera(nombre=formulario.nombre.data, facultad_id=formulario.facultad_id.data, tipo_carrera_id=formulario.tipo_carrera_id.data)

def create_carrera(nombre, facultad_id, tipo_carrera_id):
    """
    Creates a new Carrera record in the database.

    Args:
        nombre (str): The name of the carrera.
        id_facultad (int): The ID of the facultad to which this carrera belongs.
        tipo_carrera_id (int): The ID of the tipo carrera

    Returns:
        Carrera: The newly created Carrera object.

    Raises:
        Exception: If an error occurs while creating the Carrera record.
    """

    try:
        new_carrera = Carrera(nombre=nombre, facultad_id=facultad_id, tipo_carrera_id=tipo_carrera_id)
        db.session.add(new_carrera)
        db.session.commit()
        return new_carrera
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating Carrera: {e}")

def editar_carrera_web(carrera_id: int, formulario: CarreraForm):
    return edit_carrera(carrera_id=carrera_id, nombre=formulario.nombre.data, facultad_id=formulario.facultad_id.data, tipo_carrera_id=formulario.tipo_carrera_id.data)

def edit_carrera(carrera_id: int, nombre: str, facultad_id: int, tipo_carrera_id: int) -> Carrera:

    carrera = get_carrera_by_id(carrera_id)
    carrera.nombre = nombre
    carrera.facultad_id = facultad_id
    carrera.tipo_carrera_id = tipo_carrera_id

    try:
        db.session.add(carrera)
        db.session.commit()
        return carrera
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating Carrera: {e}")

def get_carrera_by_id(carrera_id):
    """
    Gets a Carrera record by its ID.

    Args:
        carrera_id (int): The ID of the Carrera to retrieve.

    Returns:
        Carrera: The Carrera object with the specified ID, or None if not found.
    """

    return Carrera.query.get(carrera_id)

def get_carreras_by_facultad(facultad_id: int):
    """
    Gets all Carrera records from the database.

    Args:
        id_facultad (int): El ID de la facultad de la cual quiero las carreras.

    Returns:
        list: A list of Carrera objects.
    """
    query = Carrera.query.filter(Carrera.facultad_id == facultad_id)

    return query.filter(Carrera.deleted_at == None).all()

def get_carreras_grado_by_facultad(facultad_id: int):
    """
    Gets all Carrera records from the database.

    Args:
        id_facultad (int): El ID de la facultad de la cual quiero las carreras.

    Returns:
        list: A list of Carrera objects.
    """
    query = Carrera.query.filter(Carrera.facultad_id == facultad_id)

    return query.filter(Carrera.deleted_at == None and Carrera.tipo_carrera.nombre == "Grado").all()

def get_carreras_posgrado_by_facultad(facultad_id: int):
    """
    Gets all Carrera records from the database.

    Args:
        id_facultad (int): El ID de la facultad de la cual quiero las carreras.

    Returns:
        list: A list of Carrera objects.
    """
    query = Carrera.query.filter(Carrera.facultad_id == facultad_id)

    return query.filter(Carrera.deleted_at == None and Carrera.tipo_carrera.nombre != "Grado").all()

def get_carreras(nombre: str, facultad_id: int, asignatura_id: int):

    query = text("SELECT * " + 
                 "FROM carreras c " + 
                 "WHERE (c.facultad_id = :facultad_id OR :facultad_id IS NULL) " + 
                 "AND (LOWER(c.nombre) LIKE CONCAT('%', LOWER(:nombre), '%') OR :nombre IS NULL) " + 
                 "AND (c.deleted_at IS NULL) " +
                 "AND NOT EXISTS (SELECT * FROM asignaturas_carreras ac WHERE ac.asignatura_id = :asignatura_id AND c.id = ac.carrera_id)")

    resultado = db.session.query(Carrera).from_statement(query).params(asignatura_id=asignatura_id, nombre=nombre, facultad_id=facultad_id).all()
    return resultado

def get_carreras_filtradas(nombre: str | None, facultad_id: int, tipo_carrera_id: int | None):
    """Obtiene todas las carreras que se cursan en la facultad.

    Returns:
        list: Una lista de objetos Carrera únicos.
    """

    carreras = Carrera.query.filter(Carrera.facultad_id == facultad_id)
    carreras = carreras.filter(Carrera.deleted_at == None)

    if nombre and nombre != "":
        carreras = carreras.filter(Carrera.nombre.ilike(f"%{nombre}%"))
    if tipo_carrera_id:
        carreras = carreras.filter(Carrera.tipo_carrera_id == tipo_carrera_id)

    return carreras.order_by(Carrera.nombre.asc()).all()

def get_carrera_by_nombre_facultad(nombre, tipo_carrera_id, facultad_id):
    """Obtiene una carrera por su nombre y su facultad.

    Args:
        nombre (str): El nombre de la carrera.
        facultad_id (int): El id de la facultad de la que depende.

    Returns:
        Carrera: El objeto Carrera o None si no se encuentra.
    """

    return Carrera.query.filter(
            and_(
                func.binary(Carrera.nombre) == nombre,
                Carrera.facultad_id == facultad_id,
                Carrera.tipo_carrera_id == tipo_carrera_id,
                Carrera.deleted_at == None
            )
        ).first()
def get_carrera_grado_by_nombre_facultad(nombre, facultad_id):
    """Obtiene una carrera por su nombre y su facultad.

    Args:
        nombre (str): El nombre de la carrera.
        facultad_id (int): El id de la facultad de la que depende.

    Returns:
        Carrera: El objeto Carrera o None si no se encuentra.
    """

    return Carrera.query.filter(
            and_(
                func.binary(Carrera.nombre) == nombre,
                Carrera.facultad_id == facultad_id,
                Carrera.deleted_at == None,
                Carrera.tipo_carrera.nombre == "Grado"
            )
        ).first()

def get_carrera_posgrado_by_nombre_facultad(nombre, facultad_id):
    """Obtiene una carrera por su nombre y su facultad.

    Args:
        nombre (str): El nombre de la carrera.
        facultad_id (int): El id de la facultad de la que depende.

    Returns:
        Carrera: El objeto Carrera o None si no se encuentra.
    """

    return Carrera.query.filter(
            and_(
                func.binary(Carrera.nombre) == nombre,
                Carrera.facultad_id == facultad_id,
                Carrera.deleted_at == None,
                Carrera.tipo_carrera.nombre != "Grado"
            )
        ).first()

def update_carrera(carrera_id, nombre=None, facultad_id=None):
    """
    Updates a Carrera record in the database.

    Args:
        carrera_id (int): The ID of the Carrera to update.
        nombre (str, optional): The updated name of the carrera.
        id_facultad (int, optional): The updated ID of the facultad.

    Returns:
        Carrera: The updated Carrera object, or None if not found.

    Raises:
        Exception: If an error occurs while updating the Carrera record.
    """

    try:
        carrera_to_update = Carrera.query.get(carrera_id)
        if carrera_to_update:
            if nombre:
                carrera_to_update.nombre = nombre
            if facultad_id:
                carrera_to_update.facultad_id = facultad_id
            db.session.commit()
            return carrera_to_update
        else:
            return None
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error updating Carrera: {e}")

def delete_carrera(carrera_id):
    """
    Deletes a Carrera record from the database (soft deletion).

    Args:
        carrera_id (int): The ID of the Carrera to delete.

    Returns:
        bool: True if the Carrera was deleted successfully, False otherwise.

    Raises:
        Exception: If an error occurs while deleting the Carrera record.
    """

    try:
        carrera_to_delete = Carrera.query.get(carrera_id)
        if carrera_to_delete and not carrera_to_delete.deleted_at:
            carrera_to_delete.deleted_at = datetime.now()
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error deleting Carrera: {e}")
    
def list_carreras(carrera_ids):
    """
    Lista las carreras cuyos IDs se encuentran en la lista proporcionada.

    Args:
        carrera_ids (list): Una lista de IDs de carreras.

    Returns:
        list: Una lista de objetos Carrera que corresponden a los IDs proporcionados.
    """

    return Carrera.query.filter(Carrera.id.in_(carrera_ids)).all()

def crear_tipo_carrera(nombre: str) -> TipoCarrera:
    try:
        new_tipo_carrera = TipoCarrera(nombre=nombre)
        db.session.add(new_tipo_carrera)
        db.session.commit()
        return new_tipo_carrera
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating Carrera: {e}")
    
def get_tipos_carrera():
    return TipoCarrera.query.all()
from sqlalchemy import and_, exists, func, or_, select, union_all
from src.core.database import db
from datetime import datetime
from src.core.models.facultad import Facultad
from src.core.models.usuario import Usuario

def create_facultad(nombre, acronimo):
    """
    Creates a new Facultad record in the database.

    Args:
        nombre (str): The name of the facultad.

    Returns:
        Facultad: The newly created Facultad object.

    Raises:
        Exception: If an error occurs while creating the Facultad record.
    """

    try:
        new_facultad = Facultad(nombre=nombre, acronimo=acronimo)
        db.session.add(new_facultad)
        db.session.commit()
        return new_facultad
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating Facultad: {e}")

def get_facultad_by_id(facultad_id: int) -> Facultad:
    """
    Gets a Facultad record by its ID.

    Args:
        facultad_id (int): The ID of the Facultad to retrieve.

    Returns:
        Facultad: The Facultad object with the specified ID, or None if not found.
    """

    return Facultad.query.get(facultad_id)

def get_facultad_by_acronimo(acronimo: str) -> Facultad:
    """
    Gets a Facultad record by its acronimo.

    Args:
        acronimo (str): The acronimo of the Facultad to retrieve.

    Returns:
        Facultad: The Facultad object with the specified ID, or None if not found.
    """

    return Facultad.query.filter(Facultad.acronimo == acronimo).first()

def get_all_facultades():
    """
    Gets all Facultad records from the database.

    Returns:
        list: A list of Facultad objects.
    """

    return Facultad.query.all()

def listar_facultades(nombre: str|None = None):
    """
    Gets all Facultad records from the database whose name matches with "nombre".

    Returns:
        list: A list of Facultad objects.
    """
    if nombre and nombre != "":
        return Facultad.query.filter(or_(Facultad.nombre.ilike(f"%{nombre}%"), Facultad.acronimo.ilike(f"%{nombre}%"))).all()
    else:
        return get_all_facultades()

def update_facultad(facultad_id, nombre):
    """
    Updates a Facultad record in the database.

    Args:
        facultad_id (int): The ID of the Facultad to update.
        nombre (str): The updated name of the Facultad.

    Returns:
        Facultad: The updated Facultad object, or None if not found.

    Raises:
        Exception: If an error occurs while updating the Facultad record.
    """

    try:
        facultad_to_update = Facultad.query.get(facultad_id)
        if facultad_to_update:
            facultad_to_update.nombre = nombre
            db.session.commit()
            return facultad_to_update
        else:
            return None
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error updating Facultad: {e}")

def delete_facultad(facultad_id):
    """
    Deletes a Facultad record from the database (soft deletion).

    Args:
        facultad_id (int): The ID of the Facultad to delete.

    Returns:
        bool: True if the Facultad was deleted successfully, False otherwise.

    Raises:
        Exception: If an error occurs while deleting the Facultad record.
    """

    facultad_to_delete = Facultad.query.get(facultad_id)
    if facultad_to_delete:
        facultad_to_delete.deleted_at = datetime.now()
        db.session.commit()
        return True
    else:
        return False
    
def get_puntos_focales_by_facultades(facultad_ids):
    # Devuelve una lista de puntos focales únicos por facultades
    return db.session.query(Usuario).filter(Usuario.facultad_id.in_(facultad_ids)).all()
from src.core.database import db
from datetime import datetime
from src.core.models.carrera import Carrera

def create_carrera(nombre, id_facultad):
    """
    Creates a new Carrera record in the database.

    Args:
        nombre (str): The name of the carrera.
        id_facultad (int): The ID of the facultad to which this carrera belongs.

    Returns:
        Carrera: The newly created Carrera object.

    Raises:
        Exception: If an error occurs while creating the Carrera record.
    """

    try:
        new_carrera = Carrera(nombre=nombre, id_facultad=id_facultad)
        db.session.add(new_carrera)
        db.session.commit()
        return new_carrera
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

    return Carrera.query.filter(Carrera.id_facultad == facultad_id).all()

def update_carrera(carrera_id, nombre=None, id_facultad=None):
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
            if id_facultad:
                carrera_to_update.id_facultad = id_facultad
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
        if carrera_to_delete:
            carrera_to_delete.deleted_at = datetime.utcnow()
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
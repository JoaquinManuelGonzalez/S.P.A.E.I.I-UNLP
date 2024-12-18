from src.core.models.postulacion.postulacion import Postulacion
from src.core.database import db

def crear_postulacion(**data):
    """
    Crea una postulación.
    """
    postulacion = Postulacion(**data)
    db.session.add(postulacion)
    db.session.commit()
    return postulacion
from src.core.models.postulacion.tutor import Tutor
from src.core.database import db

def crear_tutor(**data):
    """
    Crea un tutor.
    """
    tutor = Tutor(**data)
    db.session.add(tutor)
    db.session.commit()
    return tutor
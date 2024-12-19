from src.core.models.archivo import Archivo
from src.core.database import db

def crear_archivo(**data):
    """
    Crea un archivo.
    """
    archivo = Archivo(**data)
    db.session.add(archivo)
    db.session.commit()
    return archivo
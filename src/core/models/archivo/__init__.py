from .archivo import Archivo
from src.core.database import db

class ServicioArchivo:
    @classmethod
    def crear_archivo(cls, **kwargs):
        archivo = Archivo(**kwargs)
        if archivo is None:
            return None
        db.session.add(archivo)
        db.session.commit()
        return archivo
    
    
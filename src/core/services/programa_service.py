from src.core.models.postulacion.programa import Programa
from src.core.database import db

def listar_programas():
    return Programa.query.all()

def crear_programa(nombre):
    programa = Programa(nombre=nombre)
    db.session.add(programa)
    db.session.commit()
    return programa

def get_programa_by_id(id_programa):
    return Programa.query.get(id_programa)
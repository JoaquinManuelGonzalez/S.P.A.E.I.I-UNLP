from src.core.models.postulacion.programa import Programa
from src.core.database import db

def listar_programas():
    return Programa.query.all()

def crear_programa(nombre, habilitado):
    programa = Programa(nombre=nombre, habilitado=habilitado)
    db.session.add(programa)
    db.session.commit()
    return programa

def get_programa_by_id(id_programa):
    return Programa.query.get(id_programa)

def actualizar_programa(id_programa, nombre, habilitado):
    programa = get_programa_by_id(id_programa)
    programa.nombre = nombre
    programa.habilitado = habilitado
    db.session.commit()

def eliminar_programa(id_programa):
    programa = get_programa_by_id(id_programa)
    db.session.delete(programa)
    db.session.commit()

def listar_programas_habilitados():
    return Programa.query.filter_by(habilitado=True).all()
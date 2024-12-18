from src.core.models.postulacion.estado import Estado
from src.core.database import db

def listar_estados():
    return Estado.query.all()

def crear_estado(**data):
    estado = Estado(**data)
    db.session.add(estado)
    db.session.commit()
    return estado

def get_estado_by_name(name):
    return Estado.query.filter_by(nombre=name).first()
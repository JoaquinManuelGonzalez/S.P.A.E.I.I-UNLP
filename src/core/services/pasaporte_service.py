from src.core.models.alumno import Pasaporte
from src.core.database import db


def crear_pasaporte(
        numero,
        id_pais,
        id_archivo
):
    pasaporte = Pasaporte(
        numero=numero,
        id_pais=id_pais,
        id_archivo=id_archivo
    )

    db.session.add(pasaporte)
    db.session.commit()

    return pasaporte


def actualizar_informacion_pasaporte(
        pasaporte,
        numero,
        pais,
):
    pasaporte.numero = numero
    pasaporte.pais = pais

    db.session.commit()

    return pasaporte

def get_pasaporte_by_id(id_pasaporte):
    pasaporte = Pasaporte.query.get(id_pasaporte)
    return pasaporte

def check_numero(numero):
    return bool(Pasaporte.query.filter_by(numero=numero).first())

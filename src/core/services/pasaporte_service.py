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
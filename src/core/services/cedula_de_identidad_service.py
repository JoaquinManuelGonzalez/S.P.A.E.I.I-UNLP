from src.core.models.alumno import CedulaDeIdentidad
from src.core.database import db


def crear_cedula_de_identidad(
        numero,
        id_pais,
        id_archivo
):
    cedula_de_identidad = CedulaDeIdentidad(
        numero=numero,
        id_pais=id_pais,
        id_archivo=id_archivo
    )

    db.session.add(cedula_de_identidad)
    db.session.commit()

    return cedula_de_identidad


def actualizar_informacion_cedula_de_identidad(
        cedula_de_identidad,
        numero,
        pais,
):
    cedula_de_identidad.numero = numero
    cedula_de_identidad.pais = pais

    db.session.commit()

    return cedula_de_identidad

def get_cedula_de_identidad_by_id(id_cedula_de_identidad):
    cedula_de_identidad = CedulaDeIdentidad.query.get(id_cedula_de_identidad)
    return cedula_de_identidad

def check_numero(numero):
    return bool(CedulaDeIdentidad.query.filter_by(numero=numero).first())

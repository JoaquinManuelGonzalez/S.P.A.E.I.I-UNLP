from src.core.models.alumno import CedulaDeIdentidad
from src.core.database import db
from src.core.services import archivo_service


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

def actualizar_cedula_con_archivo(
        cedula_de_identidad,
        numero,
        pais,
        archivo,
        filename
):
    cedula_de_identidad = actualizar_informacion_cedula_de_identidad(
        cedula_de_identidad,
        numero,
        pais,
    )

    archivo_original = archivo_service.obtener_archivo_por_id(cedula_de_identidad.id_archivo)
    archivo_original.titulo = archivo.filename
    archivo_original.path = filename

    archivo_service.save_file_minio(archivo.read(), filename)

    db.session.commit()

    return cedula_de_identidad

def crear_cedula_desde_edicion(
        numero,
        pais,
        archivo,
        filename
):
    nuevo_archivo = archivo_service.crear_archivo(
        titulo=filename,
        path=filename
    )
    cedula_de_identidad = CedulaDeIdentidad(
        numero=numero,
        id_pais=pais.id,
        id_archivo=nuevo_archivo.id
    )

    archivo_service.save_file_minio(archivo.read(), filename)

    db.session.add(cedula_de_identidad)
    db.session.commit()
    nuevo_archivo.id_cedula_de_identidad = cedula_de_identidad.id
    db.session.commit()

    return cedula_de_identidad
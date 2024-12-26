from src.core.models.alumno import Pasaporte
from src.core.database import db
from src.core.services import archivo_service


def crear_pasaporte_desde_edicion(
        numero,
        pais,
        archivo,
        filename
):
    nuevo_archivo = archivo_service.crear_archivo(
        titulo=archivo.filename,
        path=filename,
    )
    pasaporte = Pasaporte(
        numero=numero,
        id_pais=pais.id,
        id_archivo=nuevo_archivo.id
    )

    archivo_service.save_file_minio(archivo.read(), filename)

    db.session.add(pasaporte)
    db.session.commit()
    nuevo_archivo.id_pasaporte = pasaporte.id
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

def actualizar_pasaporte_con_archivo(
        pasaporte,
        numero,
        pais,
        archivo,
        filename
):
    pasaporte = actualizar_informacion_pasaporte(
        pasaporte,
        numero,
        pais
    )

    archivo_original = archivo_service.obtener_archivo_por_id(pasaporte.id_archivo)
    archivo_original.titulo = archivo.filename
    archivo_original.path = filename

    archivo_service.save_file_minio(archivo.read(), filename)

    db.session.commit()

    return pasaporte
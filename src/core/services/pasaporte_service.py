from src.core.models.alumno import Pasaporte
from src.core.database import db
from src.core.services import archivo_service
import base64


def crear_pasaporte(
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
    nuevo_archivo.id_pasaporte = pasaporte.id

    archivo_codificado = base64.b64encode(archivo.read())
    archivo_service.save_file_minio(archivo_codificado, filename)

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

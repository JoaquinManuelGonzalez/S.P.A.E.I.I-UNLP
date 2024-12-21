from src.core.models.archivo import Archivo
from src.core.database import db
from flask import current_app as app
import io

def crear_archivo(**data):
    """
    Crea un archivo.
    """
    archivo = Archivo(**data)
    db.session.add(archivo)
    db.session.commit()
    return archivo
    
def save_file_minio(file, filename):
    """
    Guarda un archivo en Minio.
    """
    try:
        client = app.storage.client
        # Convertir el archivo de bytes a un objeto BytesIO (simulando un archivo en memoria)
        file_data = io.BytesIO(file)
        size = len(file)  # Obtener el tamaño del archivo desde los bytes
        print(f"file_dara: {file_data}")
        # Subir el archivo a Minio
        client.put_object(
            "spaeii",  # Nombre del bucket
            filename,  # Nombre del archivo en Minio
            file_data,  # El archivo en formato BytesIO
            size,  # Tamaño del archivo
            content_type='application/octet-stream'  # Asumiendo un tipo de contenido genérico
        )
    except Exception as e:
        raise Exception(f"Error al guardar el archivo en Minio: {e}")
    

def get_archivo_by_path(path):
    """
    Obtiene un archivo por su path.
    """
    return Archivo.query.filter_by(path=path).first()

def get_archivos_by_postulacion(id_postulacion):
    """
    Obtiene los archivos de una postulación.
    """
    return Archivo.query.filter_by(id_postulacion=id_postulacion).all()
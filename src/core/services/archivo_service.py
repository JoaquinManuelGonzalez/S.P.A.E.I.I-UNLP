from src.core.models.archivo import Archivo
from src.core.database import db
from flask import current_app as app
import io
from flask import send_file

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

def obtener_archivo_por_palabra_clave(archivos, palabra_clave):
    return next(
        (archivo for archivo in archivos if palabra_clave in archivo.path), 
        "No posee información asociada."
    )

def obtener_archivo_por_id(id_archivo):
    return Archivo.query.get(id_archivo)

def generar_url_firmada(archivo):
    """
    Genera una URL firmada para un archivo en Minio.
    """
    client = app.storage.client
    url = client.presigned_get_object(
        "spaeii",  # Nombre del bucket
        archivo.path,  # Nombre del archivo en Minio
    )
    return url

def descargar_archivo(filename):
    try:
        client = app.storage.client
        bucket_name = "spaeii"
        response = client.get_object(bucket_name, filename)

        file_data = io.BytesIO(response.read())
        response.close()
        response.release_conn()

        return send_file(file_data, download_name=filename, as_attachment=True)
    except Exception:
        return "Error al descargar el archivo", 500
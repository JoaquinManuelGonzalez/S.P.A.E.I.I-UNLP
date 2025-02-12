from src.core.models.alumno.genero import Genero
from src.core.models.alumno.estado_civil import EstadoCivil
from src.core.models.alumno.pais import Pais
from src.core.models.alumno.cedula_de_identidad import CedulaDeIdentidad
from src.core.models.alumno.pasaporte import Pasaporte
from src.core.models.alumno.informacion_alumno_entrante import InformacionAlumnoEntrante
from src.core.models.asignatura import Asignatura
from src.core.models.postulacion.estado import Estado
from src.core.models.postulacion.postulacion import Postulacion
from src.core.models.postulacion.postulacion_asignatura import PostulacionAsignatura
from src.core.database import db
from src.core.services import usuario_service, postulacion_service, genero_service, paises_service, estado_civil_service, archivo_service


def ordenar_alumnos(
        query,
        ordenado_por,
        orden
):
    
    if orden == "asc":
        if ordenado_por == "nombre":
            return query.order_by(InformacionAlumnoEntrante.nombre.asc())
        elif ordenado_por == "apellido":
            return query.order_by(InformacionAlumnoEntrante.apellido.asc())
        else:
            return query.order_by(InformacionAlumnoEntrante.email.asc())
    else:
        if ordenado_por == "nombre":
            return query.order_by(InformacionAlumnoEntrante.nombre.desc())
        elif ordenado_por == "apellido":
            return query.order_by(InformacionAlumnoEntrante.apellido.desc())
        else:
            return query.order_by(InformacionAlumnoEntrante.email.desc())


def get_alumnos_con_postulaciones_activas(facultad_id, posgrado = None):
    # Estados que queremos excluir
    estados_excluir = [
        'Solicitud de Postulacion',
        'Solicitud Rechazada',
        'Postulacion Cancelada o Interrumpida',
        'Postulacion Finalizada',
    ]

    # Subconsulta para verificar si existe una postulación válida asociada al alumno
    if (posgrado == None):
        subconsulta = (
            db.session.query(Postulacion.id)
            .join(Postulacion.asignaturas)  # Unir con PostulacionAsignatura
            .join(PostulacionAsignatura.asignatura) # Unir con Asignatura
            .join(Asignatura.facultad)      # Unir con Facultad
            .join(Postulacion.estado)       # Unir con Estado
            .filter(
                Asignatura.facultad_id == facultad_id,   # Filtrar por facultad específica
                Estado.nombre.notin_(estados_excluir),   # Excluir estados no deseados
                Postulacion.id_informacion_alumno_entrante == InformacionAlumnoEntrante.id
            )
            .exists()  # Verificar si existe una postulación que cumpla con los filtros
        )
    else:
        subconsulta = (
            db.session.query(Postulacion.id)
            .join(Postulacion.asignaturas)  # Unir con PostulacionAsignatura
            .join(PostulacionAsignatura.asignatura) # Unir con Asignatura
            .join(Asignatura.facultad)      # Unir con Facultad
            .join(Postulacion.estado)       # Unir con Estado
            .filter(
                Asignatura.facultad_id == facultad_id,   # Filtrar por facultad específica
                Estado.nombre.notin_(estados_excluir),   # Excluir estados no deseados
                Postulacion.id_informacion_alumno_entrante == InformacionAlumnoEntrante.id,
                Postulacion.de_posgrado == posgrado
            )
            .exists()  # Verificar si existe una postulación que cumpla con los filtros
        )

    # Devuelve la consulta para que pueda ser extendida
    return db.session.query(InformacionAlumnoEntrante).filter(subconsulta)


def filtrar_alumnos(
        nombre,
        apellido,
        email,
        pagina,
        ordenado_por,
        orden,
        por_pagina,
        facultad,
        posgrado = None
):
    if facultad:
        query = get_alumnos_con_postulaciones_activas(facultad, posgrado)
    else:
        query = InformacionAlumnoEntrante.query

    if nombre:
        query = query.filter(InformacionAlumnoEntrante.nombre.ilike(f"{nombre}%"))
    if apellido:
        query = query.filter(InformacionAlumnoEntrante.apellido.ilike(f"{apellido}%"))
    if email:
        query = query.filter(InformacionAlumnoEntrante.email.ilike(f"{email}%"))
    
    if ordenado_por:
        query = ordenar_alumnos(query, ordenado_por, orden)

    return query.paginate(page=pagina, per_page=por_pagina, error_out=False)


def get_alumno_by_id(id_alumno):
    return InformacionAlumnoEntrante.query.get(id_alumno)

def get_alumno_by_email(email):
    return InformacionAlumnoEntrante.query.filter_by(email=email).first()

def crear_informacion_alumno_entrante(**data):

    alumno = None
    usuario = usuario_service.buscar_usuario_email(data['email'])
    if usuario:
        return alumno
    if postulacion_service.puede_postularse(data['email']):
        alumno = get_alumno_by_email(data['email'])
        if not alumno:
            alumno = InformacionAlumnoEntrante(**data)
            db.session.add(alumno)
            db.session.commit()
        else:
            genero = genero_service.get_genero_by_id(data['id_genero'])
            pais_de_nacimiento = paises_service.get_pais_by_id(data['id_pais_de_nacimiento'])
            pais_de_residencia = paises_service.get_pais_by_id(data['id_pais_de_residencia'])
            pais_nacionalidad = paises_service.get_pais_by_id(data['id_pais_nacionalidad'])
            estado_civil = estado_civil_service.get_estado_civil_by_id(data['id_estado_civil'])
            alumno = actualizar_informacion_alumno(
                alumno,
                data['nombre'],
                data['apellido'],
                data['email'],
                data['fecha_de_nacimiento'],
                genero,
                estado_civil,
                data['discapacitado'],
                pais_de_nacimiento,
                pais_de_residencia,
                pais_nacionalidad,
                data['domicilio_pais_de_residencia']
            )
        return alumno
    else:
        return alumno

def check_email(email):
    return bool(InformacionAlumnoEntrante.query.filter_by(email=email).first())


def actualizar_informacion_alumno(
    alumno,
    nombre,
    apellido,
    email,
    fecha_de_nacimiento,
    genero,
    estado_civil,
    discapacitado,
    pais_de_nacimiento,
    pais_de_residencia,
    pais_de_nacionalidad,
    domicilio_pais_de_residencia,
):
    alumno.nombre = nombre
    alumno.apellido = apellido
    alumno.email = email
    alumno.fecha_de_nacimiento = fecha_de_nacimiento
    alumno.genero = genero
    alumno.estado_civil = estado_civil
    alumno.discapacitado = discapacitado
    alumno.pais_de_nacimiento = pais_de_nacimiento
    alumno.pais_de_residencia = pais_de_residencia
    alumno.pais_nacionalidad = pais_de_nacionalidad
    alumno.domicilio_pais_de_residencia = domicilio_pais_de_residencia

    db.session.commit()

    return alumno


def actualizar_alumno(
    alumno,
    nombre,
    apellido,
    email,
):
    alumno.nombre = nombre
    alumno.apellido = apellido
    alumno.email = email

    db.session.commit()

    return alumno


def asignar_pasaporte_alumno(alumno, id_pasaporte):
    alumno.id_pasaporte = id_pasaporte
    db.session.commit()

def asignar_cedula_alumno(alumno, id_cedula_de_identidad):
    alumno.id_cedula_de_identidad = id_cedula_de_identidad
    db.session.commit()


def actualizar_certificado_discapacidad(archivo_nuevo, filename, archivo_viejo):
    archivo_viejo.titulo = archivo_nuevo.filename
    archivo_viejo.path = filename

    archivo_service.save_file_minio(archivo_nuevo.read(), filename)

    db.session.commit()

    return archivo_viejo


def crear_certificado_discapacidad(alumno, archivo, filename):
    nuevo_archivo = archivo_service.crear_archivo(
        titulo=archivo.filename,
        path=filename
    )
    alumno.archivos.append(nuevo_archivo)
    db.session.commit()

    archivo_service.save_file_minio(archivo.read(), filename)

    return nuevo_archivo


def actualizar_certificado_espanol(archivo_nuevo, filename, archivo_viejo):
    archivo_viejo.titulo = archivo_nuevo.filename
    archivo_viejo.path = filename

    archivo_service.save_file_minio(archivo_nuevo.read(), filename)

    db.session.commit()

    return archivo_viejo


def crear_certificado_espanol(alumno, archivo, filename):
    nuevo_archivo = archivo_service.crear_archivo(
        titulo=archivo.filename,
        path=filename
    )
    alumno.archivos.append(nuevo_archivo)
    db.session.commit()

    archivo_service.save_file_minio(archivo.read(), filename)

    return nuevo_archivo
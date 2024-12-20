from src.core.models.postulacion.postulacion import Postulacion
from src.core.database import db
from src.core.models.alumno.informacion_alumno_entrante import InformacionAlumnoEntrante
from src.core.models.postulacion.estado import Estado

def crear_postulacion(**data):
    """
    Crea una postulación.
    """
    postulacion = Postulacion(**data)
    db.session.add(postulacion)
    db.session.commit()
    return postulacion

def listar_postulaciones():
    """
    Lista todas las postulaciones.
    """
    return Postulacion.query.all()

def get_postulacion_by_id(id_postulacion):
    """
    Obtiene una postulación por su id.
    """
    return Postulacion.query.get(id_postulacion)

def get_postulaciones(
        nombre,
        apellido,
        email,
        estado,
        ordenado_por,
        orden,
):
    query = Postulacion.query

    if nombre:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.nombre.ilike(f"%{nombre}%")))
    if apellido:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.apellido.ilike(f"%{apellido}%")))
    if email:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.email.ilike(f"%{email}%")))
    if estado:
        query = query.filter(Postulacion.estado.has(Estado.nombre.ilike(f"%{estado}%")))
    
    if ordenado_por:
        query = ordenar_postulaciones(query, ordenado_por, orden)

    return query.all()
def filtrar_postulaciones(
        nombre,
        apellido,
        email,
        estado,
        pagina,
        ordenado_por,
        orden,
        por_pagina
):
    
    query = Postulacion.query

    if nombre:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.nombre.ilike(f"%{nombre}%")))
    if apellido:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.apellido.ilike(f"%{apellido}%")))
    if email:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.email.ilike(f"%{email}%")))
    if estado:
        query = query.filter(Postulacion.estado.has(Estado.nombre.ilike(f"%{estado}%")))
    
    if ordenado_por:
        query = ordenar_postulaciones(query, ordenado_por, orden)

    return query.paginate(page=pagina, per_page=por_pagina, error_out=False)

def ordenar_postulaciones(
        query,
        ordenado_por,
        orden
):
    query = query.join(InformacionAlumnoEntrante, InformacionAlumnoEntrante.id == Postulacion.id_informacion_alumno_entrante)

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
        

def aprobar_postulacion_etapa_1(id_postulacion):
    """
    Aprueba la postulación en la etapa 1.
    """
    postulacion = get_postulacion_by_id(id_postulacion)
    estado = Estado.query.filter_by(nombre="Postulacion Iniciada").first()
    postulacion.estado = estado
    postulacion.id_estado = estado.id
    db.session.commit()
    return postulacion
from src.core.models.postulacion.postulacion import Postulacion
from src.core.database import db
from src.core.models.alumno.informacion_alumno_entrante import InformacionAlumnoEntrante
from src.core.models.postulacion.estado import Estado
from sqlalchemy import or_, and_

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

def filtrar_postulaciones(
        nombre,
        apellido,
        email,
        estado,
        pagina,
        ordenado_por,
        orden,
        por_pagina,
        fecha_desde=None,
        fecha_hasta=None,
        id_periodo=None,
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
    if fecha_desde:
        query = query.filter(Postulacion.creacion >= fecha_desde)
    if fecha_hasta:
        query = query.filter(Postulacion.creacion <= fecha_hasta)
    if id_periodo:
        query = query.filter(Postulacion.id_periodo_postulacion == id_periodo)

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
        

def actualizar_estado_postulacion(postulacion, nuevo_estado):
    """
    Actualiza el estado de una postulación.
    """
    nuevo_estado = Estado.query.filter_by(nombre=nuevo_estado).first()
    if not nuevo_estado:
        return None
    else:
        postulacion.estado = nuevo_estado
        db.session.commit()
        return postulacion
    

def filtrar_postulaciones_por_alumno(
        estado,
        pagina,
        por_pagina,
        fecha_desde,
        fecha_hasta,
        id_alumno
):
    query = Postulacion.query

    if estado:
        query = query.filter(Postulacion.estado.has(Estado.nombre.ilike(f"%{estado}%")))
    if fecha_desde:
        query = query.filter(Postulacion.creacion >= fecha_desde)
    if fecha_hasta:
        query = query.filter(Postulacion.creacion <= fecha_hasta)
    if id_alumno:
        query = query.filter(Postulacion.id_informacion_alumno_entrante == id_alumno)

    return query.paginate(page=pagina, per_page=por_pagina, error_out=False)

def postulaciones_pendientes_presidencia(
        nombre = None,
        apellido = None,
        email = None,
        ordenado_por = None,
        orden = None,
        fecha_desde=None,
        fecha_hasta=None,
        id_periodo=None,
        pagina = None, 
        por_pagina = None):
    query = Postulacion.query
    if nombre:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.nombre.ilike(f"%{nombre}%")))
    if apellido:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.apellido.ilike(f"%{apellido}%")))
    if email:
        query = query.filter(Postulacion.informacion_alumno_entrante.has(InformacionAlumnoEntrante.email.ilike(f"%{email}%")))
    if fecha_desde:
        query = query.filter(Postulacion.creacion >= fecha_desde)
    if fecha_hasta:
        query = query.filter(Postulacion.creacion <= fecha_hasta)
    if id_periodo:
        query = query.filter(Postulacion.id_periodo_postulacion == id_periodo)
    
    query = query.filter(
        or_(
            Postulacion.estado.has(Estado.requiere_accion_presidencia),
            Postulacion.estado.has(Estado.requiere_accion_presidencia),
            Postulacion.estado.has(Estado.requiere_accion_presidencia)
        )
    )

    if ordenado_por:
        query = ordenar_postulaciones(query, ordenado_por, orden)


    if not pagina:
        return query.all()
    return query.paginate(page=pagina, per_page=por_pagina, error_out=False)

def postulaciones_pendientes_focal(idPuntoFocal): #TODO
    query = Postulacion.query.filter(
        and_(
            Postulacion.estado.name == "Postulacion en Proceso", #TODO: and facultad = puntofocal facultad
        )
    )
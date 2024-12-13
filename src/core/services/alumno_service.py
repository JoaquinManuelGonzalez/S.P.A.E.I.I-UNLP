from src.core.models.alumno.genero import Genero
from src.core.models.alumno.estado_civil import EstadoCivil
from src.core.models.alumno.pais import Pais
from src.core.models.alumno.cedula_de_identidad import CedulaDeIdentidad
from src.core.models.alumno.pasaporte import Pasaporte
from src.core.models.alumno.informacion_alumno_entrante import InformacionAlumnoEntrante


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


def filtrar_alumnos(
        nombre,
        apellido,
        email,
        pagina,
        ordenado_por,
        orden,
        por_pagina
):
    
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
from flask import Blueprint, request, render_template, session
from src.core.services import alumno_service, archivo_service, usuario_service
from src.web.handlers.auth import get_rol_sesion, get_id_sesion


alumnos_bp = Blueprint("alumnos_bp", __name__, url_prefix="/alumnos")


@alumnos_bp.get("/")
def listar_alumnos():

    """
    faltudad = None
    if get_rol_sesion(session) == "punto_focal":
        id_punto_focal = get_id_sesion(session)
        facultad = usuario_service.buscar_usuario(id_punto_focal)
        # NECESITO SABER LA FACULTAD DEL PUNTO FOCAL 
    """
    
    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")
    email = request.args.get("email")
    pagina = request.args.get("pagina", 1, type=int)
    ordenado_por = request.args.get("ordenado_por", "nombre")
    orden = request.args.get("orden", "asc")
    por_pagina = 5

    alumnos = alumno_service.filtrar_alumnos(
        nombre,
        apellido,
        email,
        pagina,
        ordenado_por,
        orden,
        por_pagina
    )

    return render_template("alumnos/listar-alumnos.html", alumnos=alumnos)


@alumnos_bp.get("ver-detalle-alumno/<int:id_alumno>")
def ver_detalle_alumno(id_alumno):
    
    alumno = alumno_service.get_alumno_by_id(id_alumno)
    return render_template("alumnos/ver-detalle-alumno.html", alumno=alumno)


@alumnos_bp.get("editar-alumno/<int:id_alumno>")
def editar_alumno(id_alumno):
    pass


@alumnos_bp.post("editar-alumno/<int:id_alumno>")
def actualizar_alumno(id_alumno):
    pass


@alumnos_bp.post("eliminar-alumno/<int:id_alumno>")
def eliminar_alumno(id_alumno):
    pass
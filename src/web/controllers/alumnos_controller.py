from flask import Blueprint, request, render_template
from src.core.services import alumno_service
from src.core.services import archivo_service


alumnos_bp = Blueprint("alumnos_bp", __name__, url_prefix="/alumnos")


@alumnos_bp.get("/")
def index():
    return render_template("alumnos/index.html")


@alumnos_bp.get("/listar-alumnos")
def listar_alumnos():

    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")
    email = request.args.get("email")
    pagina = request.args.get("pagina", 1, type=int)
    ordenado_por = request.args.get("ordenado_por", "nombre")
    orden = request.args.get("orden", "asc")
    por_pagina = 5

    alumnos = alumno_service.filtar_alumnos(
        nombre,
        apellido,
        email,
        pagina,
        ordenado_por,
        orden,
        por_pagina
    )

    return render_template("alumnos/listar-alumnos.html", alumnos=alumnos)

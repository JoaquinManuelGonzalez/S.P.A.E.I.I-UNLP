from flask import Blueprint, request, render_template
from src.core.services import alumno_service
from src.core.services import archivo_service


alumnos_bp = Blueprint("alumnos_bp", __name__, url_prefix="/alumnos")


@alumnos_bp.get("/")
def index():
    return render_template("alumnos/index.html")
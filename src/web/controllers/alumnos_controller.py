from flask import Blueprint, request, render_template
from src.core.services import alumno_service


alumnos_bp = Blueprint("alumnos_bp", __name__, url_prefix="/alumnos")

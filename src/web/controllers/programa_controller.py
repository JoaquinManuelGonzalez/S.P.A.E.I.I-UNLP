from flask import Blueprint, request
from src.core.models.postulacion.programa import Programa

bp = Blueprint('programa', __name__, url_prefix='/programas')  

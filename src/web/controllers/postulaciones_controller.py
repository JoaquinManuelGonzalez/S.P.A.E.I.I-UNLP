from flask import Blueprint, request
from src.core.models.postulacion import Postulacion


postulacion_bp = Blueprint('postulacion', __name__, url_prefix='/postulaciones')
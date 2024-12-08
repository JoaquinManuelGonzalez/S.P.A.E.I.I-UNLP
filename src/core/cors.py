from flask import Flask
from flask_cors import CORS
import os

def init_app(app: Flask) -> None:
    """Inicializa CORS para la aplicación.

    Args:
        app: Flask
            La instancia de la aplicación.
    """
    # Definir el origen permitido
    allowed_origin = "http://localhost:5173"
    
    # Configurar CORS solo para POST en /api/postulacion/primer-formulario
    CORS(app, resources={
        r"/api/postulacion/primer-formulario": {
            "origins": allowed_origin,
            "methods": ["POST"]
        },
        r"/api/postulacion/primer-formulario-data": {
            "origins": allowed_origin,
            "methods": ["GET"]
        }
    })

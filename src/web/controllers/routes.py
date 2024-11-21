from .alumnos_controller import alumnos_bp
from .facultades import facultades_bp


def registrar_rutas(app):

    app.register_blueprint(alumnos_bp)
    app.register_blueprint(facultades_bp)

    return app
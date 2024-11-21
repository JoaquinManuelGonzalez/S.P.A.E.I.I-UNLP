from .alumnos_controller import alumnos_bp
from .usuario_controller import usuario_bp


def registrar_rutas(app):

    app.register_blueprint(alumnos_bp)
    app.register_blueprint(usuario_bp)

    return app
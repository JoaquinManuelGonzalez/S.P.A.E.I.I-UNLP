from .alumnos_controller import alumnos_bp


def registrar_rutas(app):

    app.register_blueprint(alumnos_bp)

    return app
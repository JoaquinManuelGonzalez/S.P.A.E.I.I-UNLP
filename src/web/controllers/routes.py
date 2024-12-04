from .alumnos_controller import alumnos_bp
from src.web.api.primer_formulario import bp as primer_formulario_bpfrom .usuario_controller import usuario_bp


def registrar_rutas(app):

    app.register_blueprint(alumnos_bp)
    app.register_blueprint(primer_formulario_bp)
    app.register_blueprint(usuario_bp)

    return app
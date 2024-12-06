from .usuario_controller import usuario_bp
from .facultades import facultades_bp
from src.web.api.primer_formulario import bp as primer_formulario_bp
from .alumnos_controller import alumnos_bp
from .postulaciones_controller import postulacion_bp


def registrar_rutas(app):

    app.register_blueprint(alumnos_bp)
    app.register_blueprint(facultades_bp)
    app.register_blueprint(primer_formulario_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(postulacion_bp)

    return app
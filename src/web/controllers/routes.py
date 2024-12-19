from .usuario_controller import usuario_bp
from .facultades import facultades_bp
from .asignaturas import asignaturas_bp
from src.web.api.primer_formulario import bp as primer_formulario_bp
from src.web.controllers.auth_controller import bp as auth_bp
from .alumnos_controller import alumnos_bp
from .postulaciones_controller import postulacion_bp
from .carreras import carreras_bp
from .programa_controller import bp as programa_bp

def registrar_rutas(app):

    app.register_blueprint(auth_bp)
    app.register_blueprint(alumnos_bp)
    app.register_blueprint(facultades_bp)
    app.register_blueprint(primer_formulario_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(postulacion_bp)
    app.register_blueprint(programa_bp)
    app.register_blueprint(asignaturas_bp)
    app.register_blueprint(carreras_bp)

    return app
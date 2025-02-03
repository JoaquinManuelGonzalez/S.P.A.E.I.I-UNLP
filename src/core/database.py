from flask_sqlalchemy import SQLAlchemy
# from src.core.usuario.seeds import crear_seeds_usuarios

db = SQLAlchemy()

def init_app(app):
    """
    Instancia la base de datos y la configura

    Args:
        app: Aplicación de Flask

    Returns:
        app: Aplicación de Flask con la base de datos configurada
    """
    db.init_app(app)
    config(app)

    return app

def config(app):
    """
    Configura la base de datos

    Args:
        app: Aplicación de Flask

    Returns:
        app: Aplicación de Flask con la base de datos configurada
    """

    @app.teardown_appcontext
    def close_session(exception=None):
        db.session.close()
    
    return app


def reset():
    from src.core.models.usuario import Usuario
    from src.core.models.facultad import Facultad
    from src.core.models.carrera import Carrera
    from src.core.models.asignatura import Asignatura
    from src.core.models.postulacion import Postulacion, PostulacionAsignatura
    from src.core.models.alumno import InformacionAlumnoEntrante
    """
    Resetea la base de datos
    """
    print("Eliminando base de datos en cascada")
    db.drop_all()
    print("Creando base nuevamente")
    db.create_all()
    print("Done!")
    db.session.commit()
    

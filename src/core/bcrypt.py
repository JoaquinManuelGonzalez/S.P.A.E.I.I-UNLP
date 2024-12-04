from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def init_app(app):
    """
    Inicializa el objeto Bcrypt con la aplicación de Flask.

    Args:
        app: Aplicación de Flask.
    """
    bcrypt.init_app(app)
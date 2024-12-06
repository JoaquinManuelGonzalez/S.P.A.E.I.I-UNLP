from src.core.models.usuario import Usuario
from flask import abort, session, flash
from functools import wraps

def check_auth():
    """
    Decorador que verifica si un usuario está autenticado antes de ejecutar una función.
    
    Returns:
        function: La función decorada con la verificación de autenticación.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if is_authenticated(session):
                return abort(403)
            return f(*args, **kwargs)
        return wrapper
    return decorator

def is_authenticated(session):
    """
    Verifica si un usuario está autenticado basado en la información de la sesión.
    
    Args:
        session: El objeto de sesión que contiene la información del usuario.
    
    Returns:
        bool: True si el usuario está autenticado, False en caso contrario.
    """
    return session.get("user_id") is not None


def get_rol_sesion(session):
    """
    Obtiene el rol del usuario autenticado basado en la sesión actual.
    
    Args:
        session: El objeto de sesión que contiene la información del usuario.
    
    Returns:
        str: El nombre del rol del usuario si está autenticado, None en caso contrario.
    """
    email_usuario = session.get("user_email")
    if email_usuario:
        usuario = Usuario.query.filter_by(email=email_usuario).first()
        rol_usuario = usuario.rol.nombre
        print(type(rol_usuario))
        return rol_usuario
    return None


def get_id_sesion(session):
    """
    Obtiene el ID del usuario autenticado basado en la sesión actual.
    
    Args:
        session: El objeto de sesión que contiene la información del usuario.
    
    Returns:
        int: El ID del usuario si está autenticado, None en caso contrario.
    """

    return session.get("user_id") if is_authenticated(session) else None

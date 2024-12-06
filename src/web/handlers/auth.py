from src.core.models.usuario import Usuario

def is_authenticated(session):
    """
    Verifica si un usuario está autenticado basado en la información de la sesión.
    
    Args:
        session: El objeto de sesión que contiene la información del usuario.
    
    Returns:
        bool: True si el usuario está autenticado, False en caso contrario.
    """
    return session.get("user_email") is not None


def get_rol_sesion(session):
    """
    Obtiene el rol del usuario autenticado basado en la sesión actual.
    
    Args:
        session: El objeto de sesión que contiene la información del usuario.
    
    Returns:
        str: El nombre del rol del usuario si está autenticado, None en caso contrario.
    """
    email_usuario = session.get("user")
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

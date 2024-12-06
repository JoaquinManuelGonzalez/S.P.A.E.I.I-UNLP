from flask import abort, session, request
from functools import wraps
from src.core.services.usuario_service import buscar_usuario_email, buscar_permisos_usuario


def check(permiso):
    """
    Decorador que verifica si el usuario tiene el permiso necesario para acceder a la vista.

    Args:
        permiso (str): Nombre del permiso a verificar.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not check_permiso(session, permiso):
                return abort(403)
            return f(*args, **kwargs)
        return wrapper
    return decorator

def check_permiso(session, permiso):
    """
    Verifica si el usuario tiene el permiso necesario para acceder a la vista.

    Args:
        session: session de Flask.
        permiso: Nombre del permiso a verificar.

    Returns:
        bool: Retorna True si el usuario tiene el permiso, False en caso contrario.
    """
    email_usuario = session.get('user_email')
    if email_usuario is None:
        return False
    usuario = buscar_usuario_email(email=email_usuario)
    permisos = [permiso.permiso.nombre for permiso in buscar_permisos_usuario(usuario)]
    
    # if permiso not in permisos:
    #     id_usuario = int(request.path.split('/')[-1])
    #     if (id_usuario != session.get('user_id')):
    #         return False
    
    return permiso in permisos

def get_id_sesion(session):
    """
    Obtiene el id del usuario de la sesión.

    Args:
        session: session de Flask.

    Returns:
        int: Retorna el id del usuario de la sesión.
    """
    email_usuario = session.get("user")
    if email_usuario:
        usuario = buscar_usuario_email(email=email_usuario)
        id_usuario = usuario.id
        return id_usuario
    return None
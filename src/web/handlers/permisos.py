from flask import abort, session, request
from functools import wraps
from src.core.services.usuario_service import buscar_usuario_email, buscar_permisos_usuario, buscar_usuario
from src.core.services import postulacion_service


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
    #primero corroboro si hay un alumno en sesion
    id_usuario_sesion = session.get('user_id')
    usuario_sesion = buscar_usuario(id_usuario_sesion)
    if id_usuario_sesion is None:
        return False
    permisos = [permiso.permiso.nombre for permiso in buscar_permisos_usuario(usuario_sesion)]
    #si se busca ver detalle o edicion, se verifica que sea el mismo usuario
    if permiso.endswith('detalle') or permiso.endswith('editar'):
        id_buscado = int(request.path.split('/')[-1])
        if ("admin" in permisos) or ("gestor" in permisos):
            return True
        elif ("punto_focal" in permisos) and (id_buscado == id_usuario_sesion):
            return True
        
        if "alumno" in request.path:
            if (id_buscado != usuario_sesion.id_alumno):
                return False
        elif "usuarios" in request.path.split('/'):
            if (id_buscado != id_usuario_sesion):
                return False
        elif "postulaciones" in request.path.split('/'):
            if ("punto_focal" in permisos):
                return True
            postulacion = postulacion_service.get_postulacion_by_id(id_buscado)
            if (postulacion.id_informacion_alumno_entrante != usuario_sesion.id_alumno):
                return False
        elif ( (permiso.endswith('detalle')) and ("facultades" in request.path.split('/')) and ("punto_focal" in permisos) ):
            if id_buscado == usuario_sesion.facultad_id:
                return True
    elif permiso == "postulaciones_listar":
        if "alumno" in permisos or "punto_focal" in permisos:
            return False
        
    
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
from src.core.models.usuario import Usuario
from core.bcrypt import bcrypt

def find_user_by_email(email):
    """
    Busca un usuario en la base de datos por su dirección de correo electrónico.
    
    Args:
        email (str): La dirección de correo electrónico del usuario a buscar.
    
    Returns:
        Usuario: El objeto Usuario si se encuentra un usuario con el correo proporcionado, None en caso contrario.
    """
    user = Usuario.query.filter_by(email=email).first()
    return user


def check_user(email, password):
    """
    Verifica si las credenciales proporcionadas (correo electrónico y contraseña) son correctas.
    
    Args:
        email (str): La dirección de correo electrónico del usuario.
        password (str): La contraseña del usuario en texto plano.
    
    Returns:
        Usuario: El objeto Usuario si las credenciales son correctas, None en caso contrario.
    """
    user = find_user_by_email(email)

    if user and bcrypt.check_password_hash(user.contraseña, password):
        return user
    
    return None


def check_block(user):
    """
    Verifica si la cuenta del usuario está activa.
    
    Args:
        user (Usuario): El objeto Usuario a verificar.
    
    Returns:
        Usuario: El objeto Usuario si está activo, None en caso contrario.
    """
    if user.activo == True:
        return user
    return None

from src.core.models.usuario import Usuario, Rol, Permiso, RolPermiso
from flask import request, render_template, redirect, flash
from src.web.forms import Usuario_Form
from src.web.forms.recuperar_contraseña_form import RecuperarContraseñaForm as Recuperar_Form
from src.core.bcrypt import bcrypt
from src.core.database import db
from datetime import datetime
import string, secrets
from flask import session
from src.core.services import email_service


def listar_usuarios(pagina:int):
    usuarios = filtrar_usuarios(pagina)
    return usuarios

def filtrar_usuarios(pagina:int):
    filtro_nombre = request.args.get('nombre')
    filtro_email = request.args.get('email')
    filtro_rol = request.args.get('rol')
    filtro_orden = request.args.get('sort')
    filtro_orden_tipo = request.args.get('order')
    query = Usuario.query.filter(Usuario.id!=1)
    if filtro_email:
        query = query.filter(Usuario.email.ilike(f'%{filtro_email}%'))
    if filtro_nombre:
        query = query.filter(Usuario.nombre.ilike(f'%{filtro_nombre}%'))
    if filtro_rol:
        query = query.filter_by(id_rol=filtro_rol)
    if filtro_orden:
        columna = getattr(Usuario, filtro_orden, None)
        if columna:
            if filtro_orden_tipo == 'asc':
                query = query.order_by(columna.asc())
            else:
                query = query.order_by(columna.desc())
    else:
        query = query.order_by(Usuario.id.asc())
    
    return query.paginate(page=pagina, per_page=5, error_out=False)

def crear_usuario(formulario:Usuario_Form) -> None:
    hash = bcrypt.generate_password_hash(formulario.contraseña.data.encode('utf-8'))
    formulario.contraseña.data = hash.decode('utf-8')
    usuario = Usuario(
        nombre=formulario.nombre.data,
        apellido=formulario.apellido.data,
        email=formulario.email.data,
        contraseña=formulario.contraseña.data,
        id_rol=formulario.id_rol.data,
    )
    db.session.add(usuario)
    db.session.commit()
    flash('El usuario se ha creado correctamente', 'success')
    
def editar_usuario(usuario:Usuario, contraseña_nueva:str) -> None:
    '''
        Este método edita un usuario en la base de datos
        
        Args:
            usuario (Usuario): El usuario a editar
    '''
    print(session)
    if contraseña_nueva:
        hash_contraseña = bcrypt.generate_password_hash(contraseña_nueva.encode('utf-8')).decode('utf-8')
        usuario.contraseña = hash_contraseña
    db.session.add(usuario)
    db.session.commit()
    print(session)
    flash('El usuario se ha editado correctamente', 'success')

    
def recuperar_contraseña(formulario:Recuperar_Form):
    '''
        Este método recupera la contraseña de un usuario en la base de datos
        
        Args:
            formulario (Usuario_Form): El formulario de recuperación de contraseña
    '''
    usuario = Usuario.query.filter_by(email=formulario.email.data).first()
    if usuario:
        contraseña = generar_contraseña()
        hash = bcrypt.generate_password_hash(contraseña.encode('utf-8'))
        usuario.contraseña = hash.decode('utf-8')
        db.session.add(usuario)
        db.session.commit()
        mensaje = f'Su nueva contraseña es: {contraseña}, recuerde cambiarla en su próximo inicio de sesión'
        email_service.send_email('Recuperación de contraseña', mensaje, [usuario.email])
        flash('La contraseña se ha recuperado correctamente, revise su casilla de email', 'success')
    return usuario

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

def buscar_usuario(id_usuario:int) -> Usuario:
    return Usuario.query.get_or_404(id_usuario)

def buscar_usuario_email(email:str) -> Usuario:
    return Usuario.query.filter_by(email=email).first()

def crear_permiso(nombre:str) -> Permiso:
    permiso = Permiso(
        nombre=nombre
    )
    db.session.add(permiso)
    db.session.commit()
    return permiso

def listar_roles():
    return Rol.query.all()

def crear_rol(nombre:str) -> Rol:
    rol = Rol(
        nombre=nombre
    )
    db.session.add(rol)
    db.session.commit()
    return rol

def crear_rol_permiso(id_rol:int, id_permiso:int) -> RolPermiso:
    rol_permiso = RolPermiso(
        id_rol=id_rol,
        id_permiso=id_permiso
    )
    db.session.add(rol_permiso)
    db.session.commit()
    return rol_permiso
    
def buscar_permisos_usuario(id_usuario:int):
    permisos = RolPermiso.query.filter_by(id_rol=id_usuario.id_rol)
    return permisos

def get_puntos_focales_by_facultad(facultad_id: int):
    return Usuario.query.filter(Usuario.facultad_id == facultad_id).all()
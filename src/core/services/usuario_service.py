from src.core.models.usuario import Usuario, Rol, Permiso, RolPermiso
from flask import request, render_template, redirect, flash
from src.web.forms import Usuario_Form
from src.core.bcrypt import bcrypt
from src.core.database import db
from datetime import datetime


def listar_usuarios(pagina:int):
    usuarios = filtrar_usuarios(pagina)
    return usuarios

def filtrar_usuarios(pagina:int):
    query = Usuario.query.order_by(Usuario.id)
    return query.paginate(page=pagina, per_page=10, error_out=False)

def crear_usuario(formulario:Usuario_Form) -> None:
    hash = bcrypt.generate_password_hash(formulario.contraseña.data.encode('utf-8'))
    formulario.contraseña.data = hash.decode('utf-8')
    usuario = Usuario(
        nombre=formulario.alias.data,
        apellido=formulario.apellido.data,
        email=formulario.email.data,
        contraseña=formulario.contraseña.data,
        id_rol=formulario.id_rol.data,
    )
    db.session.add(usuario)
    db.session.commit()
    flash('El usuario se ha creado correctamente', 'success')
    
def editar_usuario(usuario:Usuario):
    '''
        Este método edita un usuario en la base de datos
        
        Args:
            usuario (Usuario): El usuario a editar
    '''
    db.session.add(usuario)
    db.session.commit()
    flash('El usuario se ha editado correctamente', 'success')

    
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
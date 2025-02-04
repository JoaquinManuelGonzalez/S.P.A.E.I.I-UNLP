from src.core.models.usuario import Usuario, Rol, Permiso, RolPermiso, EstadoUsuario
from flask import request, render_template, redirect, flash
from src.web.forms import Usuario_Form
from src.web.forms.recuperar_contraseña_form import RecuperarContraseñaForm as Recuperar_Form
from src.core.bcrypt import bcrypt
from src.core.database import db
from datetime import datetime
import string, secrets, random, string
from flask import session
from src.core.services import email_service, alumno_service
from sqlalchemy.orm import joinedload


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
#este crear es para el crud que utiliza el formulario
    contraseña_original = formulario.contraseña.data
    hash = bcrypt.generate_password_hash(formulario.contraseña.data.encode('utf-8'))
    formulario.contraseña.data = hash.decode('utf-8')
    es_de_posgrado = False
    es_de_grado = False
    if request.form.get('posgrado'):
        es_de_posgrado = True
    if request.form.get('grado'):
        es_de_grado = True
    usuario = Usuario(
        nombre=formulario.nombre.data,
        apellido=formulario.apellido.data,
        email=formulario.email.data,
        contraseña=formulario.contraseña.data,
        id_rol=formulario.id_rol.data,
        posgrado=es_de_posgrado,
        grado=es_de_grado,
        facultad_id=formulario.facultad_id.data,
    )
    db.session.add(usuario)
    db.session.commit()
    mensaje = f'Usted tiene un nuevo usuario registrado en SPAEII. Sus credenciales de ingreso son: usuario: {usuario.email}, contraseña: {contraseña_original} , recuerde cambiarla en su próximo inicio de sesión'
    email_service.send_email('Nuevo usuario registrado en SPAEII', mensaje, [usuario.email])
    flash('El usuario se ha creado correctamente', 'success')
    
def crear_usuario_solicitud_aprobada(nombre, apellido, email, id_alumno):
#este crear es cuando se aprueba una solicitud, considera si el usuario estaba eliminado
    usuario = buscar_usuario_email(email)
    id_rol_alumno = buscar_id_rol('alumno').id
    contraseña = generar_contraseña()
    contraseña_encriptada = encriptar_contraseña(contraseña)
    if usuario and usuario.estado.value == "eliminado":
        usuario.estado = EstadoUsuario.ACTIVO
        usuario.contraseña = contraseña_encriptada
    else:
        usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            contraseña=contraseña_encriptada,
            id_rol=id_rol_alumno,
            id_alumno=id_alumno,
        )
    db.session.add(usuario)
    db.session.commit()
    mensaje = f'Usted tiene un nuevo usuario registrado en SPAEII. Sus credenciales de ingreso son: usuario: {email}, contraseña: {contraseña} , recuerde cambiarla en su próximo inicio de sesión'
    email_service.send_email('Nuevo usuario registrado en SPAEII', mensaje, [email])

    
def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def encriptar_contraseña(contrasena):
    return bcrypt.generate_password_hash(contrasena).decode('utf-8')
    
def editar_usuario(usuario:Usuario, contraseña_nueva:str) -> None:
    '''
        Este método edita un usuario en la base de datos
        
        Args:
            usuario (Usuario): El usuario a editar
    '''
    if contraseña_nueva:
        hash_contraseña = bcrypt.generate_password_hash(contraseña_nueva.encode('utf-8')).decode('utf-8')
        usuario.contraseña = hash_contraseña
    db.session.add(usuario)
    db.session.commit()
    alumno = alumno_service.get_alumno_by_id(usuario.id_alumno)
    if alumno:
        alumno_service.actualizar_alumno(alumno, usuario.nombre, usuario.apellido, usuario.email)
    flash('El usuario se ha editado correctamente', 'success')
    
def eliminar_usuario(id_usuario:int) -> None:
    """
        Este método elimina logicamente un usuario en la base de datos
        
        Args:
            id_usuario (int): El id del usuario
    """
    usuario = buscar_usuario(id_usuario)
    usuario.estado = EstadoUsuario.ELIMINADO
    db.session.add(usuario)
    db.session.commit()
    flash('El usuario se ha eliminado correctamente', 'success')
    
def reactivar_usuario(id_usuario:int) -> None:
    """
        Este método reactiva un usuario en la base de datos
        
        Args:
            id_usuario (int): El id del usuario
    """
    usuario = buscar_usuario(id_usuario)
    usuario.estado = EstadoUsuario.ACTIVO
    db.session.add(usuario)
    db.session.commit()
    flash('El usuario se ha reactivado correctamente', 'success')

    
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

def buscar_id_rol (rol:str) -> int:
    return Rol.query.filter_by(nombre=rol).first()

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
    return Usuario.query.filter(Usuario.facultad_id == facultad_id and Usuario.estado == EstadoUsuario.ACTIVO).all()

def actualizar_informacion_usuario_alumno(
        usuario,
        nombre,
        apellido,
        email,
):
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.email = email

    db.session.commit()

def get_email_admin_presidencia():
    emails = Usuario.query.join(Rol).filter(Rol.nombre.in_(["presidencia_jefe", "presidencia_gestor"])).with_entities(Usuario.email).all()
    lista = []
    for email in emails:
        lista.append(email[0])

    return lista
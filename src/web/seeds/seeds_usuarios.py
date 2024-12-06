from src.core.services.usuario_service import crear_permiso, crear_rol, crear_rol_permiso, crear_usuario, buscar_permisos_usuario
from src.core.database import db
from src.core.models.usuario import Usuario
from src.web.forms import Usuario_Form
from src.core.bcrypt import bcrypt
from faker import Faker
import re

## Seeds de Usuarios
def seeds_usuarios():
    crear_permisos()        
    crear_roles()
    establecer_permisos_roles()
    crear_usuarios()

   
fake = Faker()
roles = []
permisos = []
def crear_permisos():
    permiso_0 = crear_permiso(nombre='admin')
    permiso_1 = crear_permiso(nombre='usuarios_eliminar')
    permiso_2 = crear_permiso(nombre='usuarios_listar')
    permiso_3 = crear_permiso(nombre='usuarios_crear')
    permiso_4 = crear_permiso(nombre='usuarios_editar')
    permiso_5 = crear_permiso(nombre='usuarios_detalle')
    permisos.append(permiso_0)
    permisos.append(permiso_1)
    permisos.append(permiso_2)
    permisos.append(permiso_3)
    permisos.append(permiso_4)
    permisos.append(permiso_5)
    
def crear_roles():
    rol_1 = crear_rol(nombre=f'presidencia_jefe')
    rol_2 = crear_rol(nombre=f'presidencia_gestor')
    rol_3 = crear_rol(nombre=f'punto_focal')
    rol_4 = crear_rol(nombre=f'alumno')
    roles.append(rol_1)
    roles.append(rol_2)
    roles.append(rol_3)
    roles.append(rol_4)
        
def establecer_permisos_roles():
    #PRESIDENCIA_JEFE
    for i in range(6):
        crear_rol_permiso(id_rol=roles[0].id, id_permiso=permisos[i].id)
    
    #PREISIDENCIA_GESTOR
    for i in range(2,6):
        crear_rol_permiso(id_rol=roles[1].id, id_permiso=permisos[i].id)
    
    #PUNTO_FOCAL
    crear_rol_permiso(id_rol=roles[2].id, id_permiso=permisos[4].id)
    crear_rol_permiso(id_rol=roles[2].id, id_permiso=permisos[5].id)
    #ALUMNO
    crear_rol_permiso(id_rol=roles[3].id, id_permiso=permisos[4].id)
    crear_rol_permiso(id_rol=roles[3].id, id_permiso=permisos[5].id)


def crear_usuarios():
    contraseña = '1234'
    hash = bcrypt.generate_password_hash(contraseña.encode('utf-8'))
    contraseña_hash = hash.decode('utf-8')
    usuarios = []

    usuario = Usuario(
        nombre= 'Jefe',
        apellido= 'Jefe',
        email= 'jefe@prueba.com',
        contraseña= contraseña_hash,
        id_rol= roles[0].id,
    )
    usuarios.append(usuario)
    
    usuario = Usuario(
        nombre= 'Gestor',
        apellido= 'Gestor',
        email= 'gestor@prueba.com',
        contraseña= contraseña_hash,
        id_rol= roles[1].id,
    )
    usuarios.append(usuario)
    
    for i in range(2):
        usuario = Usuario(
            nombre = f'Punto_Focal{i}',
            apellido = f'Punto_Focal{i}',
            email= f'punto{i}@prueba.com',
            contraseña= contraseña_hash,
            id_rol= roles[2].id,
        )
        usuarios.append(usuario)
        
    for i in range(2):
        usuario = Usuario(
            nombre = f'Alumno{i}',
            apellido = f'Alumno{i}',
            email= f'alumno{i}@prueba.com',
            contraseña= contraseña_hash,
            id_rol= roles[3].id,
        )
        usuarios.append(usuario)
        
    for i in range (len(usuarios)):
        db.session.add(usuarios[i])
    db.session.commit()

    
        
    
    
    

        
        
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
    
    usuarios = crear_usuarios()
    return usuarios

   
fake = Faker()
roles = []
permisos = []
permisos_presidencia_jefe = []
permisos_presidencia_gestor = []
permisos_punto_focal = []
permisos_alumno = []
def crear_permisos():

    permiso_0 = crear_permiso(nombre='admin')
    permiso_1 = crear_permiso(nombre='usuarios_eliminar')
    permiso_2 = crear_permiso(nombre='usuarios_listar')
    permiso_3 = crear_permiso(nombre='usuarios_crear')
    permiso_4 = crear_permiso(nombre='usuarios_editar')
    permiso_5 = crear_permiso(nombre='usuarios_detalle')
    permiso_6 = crear_permiso(nombre='postulaciones_listar')
    permiso_7 = crear_permiso(nombre='postulaciones_detalle')
    permiso_8 = crear_permiso(nombre='postulaciones_editar')
    permiso_9 = crear_permiso(nombre='postulacion_aceptar')
    permiso_10 = crear_permiso(nombre='postulacion_rechazar')
    permiso_11 = crear_permiso(nombre='solicitud_postulacion_listar')
    permiso_12 = crear_permiso(nombre='solicitud_postulacion_aceptar')
    permiso_13 = crear_permiso(nombre='solicitud_postulacion_rechazar')
    permiso_14 = crear_permiso(nombre='solicitud_postulacion_detalle')
    permiso_15 = crear_permiso(nombre='solicitud_postulacion_editar')
    permiso_16 = crear_permiso(nombre='archivo_listar')
    permiso_17 = crear_permiso(nombre='archivo_subir')
    permiso_18 = crear_permiso(nombre='archivo_descargar')
    permiso_19 = crear_permiso(nombre='archivo_editar')
    permiso_20 = crear_permiso(nombre='alumno')
    permiso_21 = crear_permiso(nombre='alumnos_listar')
    permiso_22 = crear_permiso(nombre='alumnos_editar')
    permiso_23 = crear_permiso(nombre='alumnos_eliminar')
    permiso_24 = crear_permiso(nombre='alumnos_detalle')
    permiso_25 = crear_permiso(nombre='gestor')
    permiso_26 = crear_permiso(nombre='punto_focal')
    permiso_27 = crear_permiso(nombre='facultades_listar')
    permiso_28 = crear_permiso(nombre='facultades_editar')
    permiso_29 = crear_permiso(nombre='facultades_eliminar')
    permiso_30 = crear_permiso(nombre='facultades_detalle')
    permiso_31 = crear_permiso(nombre='carreras_crud')
    permiso_32 = crear_permiso(nombre='asignaturas_crud')
    permiso_33 = crear_permiso(nombre='habilitar_periodo_postulacion')
    permiso_34 = crear_permiso(nombre='facultades_crear')
    permiso_35 = crear_permiso(nombre='carreras_editar')
    permiso_36 = crear_permiso(nombre='carreras_eliminar')
    permiso_37 = crear_permiso(nombre='asignaturas_editar')
    permiso_38 = crear_permiso(nombre='asignaturas_eliminar')
    permiso_39 = crear_permiso(nombre='carreras_detalle')
    permiso_40 = crear_permiso(nombre='asignaturas_detalle')
    permiso_41 = crear_permiso(nombre='asignaturas_crear')
    permiso_42 = crear_permiso(nombre='carreras_crear')


    permisos_presidencia_jefe.append(permiso_0)
    permisos_presidencia_jefe.append(permiso_1)
    permisos_presidencia_jefe.append(permiso_2)
    permisos_presidencia_jefe.append(permiso_3)
    permisos_presidencia_jefe.append(permiso_4)
    permisos_presidencia_jefe.append(permiso_5)
    permisos_presidencia_jefe.append(permiso_6)
    permisos_presidencia_jefe.append(permiso_7)
    permisos_presidencia_jefe.append(permiso_8)
    permisos_presidencia_jefe.append(permiso_9)
    permisos_presidencia_jefe.append(permiso_10)
    permisos_presidencia_jefe.append(permiso_11)
    permisos_presidencia_jefe.append(permiso_12)
    permisos_presidencia_jefe.append(permiso_13)
    permisos_presidencia_jefe.append(permiso_14)
    permisos_presidencia_jefe.append(permiso_16)
    permisos_presidencia_jefe.append(permiso_17)
    permisos_presidencia_jefe.append(permiso_18)
    permisos_presidencia_jefe.append(permiso_19)
    permisos_presidencia_jefe.append(permiso_21)
    permisos_presidencia_jefe.append(permiso_22)
    permisos_presidencia_jefe.append(permiso_23)
    permisos_presidencia_jefe.append(permiso_24)
    permisos_presidencia_jefe.append(permiso_27)
    permisos_presidencia_jefe.append(permiso_28)
    permisos_presidencia_jefe.append(permiso_29)
    permisos_presidencia_jefe.append(permiso_30)
    permisos_presidencia_jefe.append(permiso_31)
    permisos_presidencia_jefe.append(permiso_32)
    permisos_presidencia_jefe.append(permiso_33)
    permisos_presidencia_jefe.append(permiso_34)
    permisos_presidencia_jefe.append(permiso_35)
    permisos_presidencia_jefe.append(permiso_36)
    permisos_presidencia_jefe.append(permiso_37)
    permisos_presidencia_jefe.append(permiso_38)
    permisos_presidencia_jefe.append(permiso_39)
    permisos_presidencia_jefe.append(permiso_40)
    permisos_presidencia_jefe.append(permiso_41)
    permisos_presidencia_jefe.append(permiso_42)

    permisos_presidencia_gestor.append(permiso_2)
    permisos_presidencia_gestor.append(permiso_3)
    permisos_presidencia_gestor.append(permiso_4)
    permisos_presidencia_gestor.append(permiso_5)
    permisos_presidencia_gestor.append(permiso_6)
    permisos_presidencia_gestor.append(permiso_7)
    permisos_presidencia_gestor.append(permiso_9)
    permisos_presidencia_gestor.append(permiso_10)
    permisos_presidencia_gestor.append(permiso_11)
    permisos_presidencia_gestor.append(permiso_12)
    permisos_presidencia_gestor.append(permiso_13)
    permisos_presidencia_gestor.append(permiso_14)
    permisos_presidencia_gestor.append(permiso_16)
    permisos_presidencia_gestor.append(permiso_18)
    permisos_presidencia_gestor.append(permiso_21)
    permisos_presidencia_gestor.append(permiso_24)
    permisos_presidencia_gestor.append(permiso_25)
    permisos_presidencia_gestor.append(permiso_27)
    permisos_presidencia_gestor.append(permiso_31)
    permisos_presidencia_gestor.append(permiso_32)
    permisos_presidencia_gestor.append(permiso_34)
    permisos_presidencia_gestor.append(permiso_35)
    permisos_presidencia_gestor.append(permiso_36)
    permisos_presidencia_gestor.append(permiso_37)
    permisos_presidencia_gestor.append(permiso_38)
    permisos_presidencia_gestor.append(permiso_39)
    permisos_presidencia_gestor.append(permiso_40)
    permisos_presidencia_gestor.append(permiso_41)
    permisos_presidencia_gestor.append(permiso_42)

    permisos_punto_focal.append(permiso_4)
    permisos_punto_focal.append(permiso_5)
    permisos_punto_focal.append(permiso_6)
    permisos_punto_focal.append(permiso_7)
    permisos_punto_focal.append(permiso_9)
    permisos_punto_focal.append(permiso_10)
    permisos_punto_focal.append(permiso_21)
    permisos_punto_focal.append(permiso_24)
    permisos_punto_focal.append(permiso_26)
    permisos_punto_focal.append(permiso_39)
    permisos_punto_focal.append(permiso_40)

    permisos_alumno.append(permiso_4)
    permisos_alumno.append(permiso_5)
    permisos_alumno.append(permiso_6)
    permisos_alumno.append(permiso_7)
    permisos_alumno.append(permiso_8)
    permisos_alumno.append(permiso_16)
    permisos_alumno.append(permiso_17)
    permisos_alumno.append(permiso_18)
    permisos_alumno.append(permiso_19)
    permisos_alumno.append(permiso_20)
    permisos_alumno.append(permiso_22)
    permisos_alumno.append(permiso_24)
    
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
    for permiso in permisos_presidencia_jefe:
        crear_rol_permiso(id_rol=roles[0].id, id_permiso=permiso.id)
    
    #PREISIDENCIA_GESTOR
    for permiso in permisos_presidencia_gestor:
        crear_rol_permiso(id_rol=roles[1].id, id_permiso=permiso.id)
    
    #PUNTO_FOCAL
    for permiso in permisos_punto_focal:
        crear_rol_permiso(id_rol=roles[2].id, id_permiso=permiso.id)

    #ALUMNO
    for permiso in permisos_alumno:
        crear_rol_permiso(id_rol=roles[3].id, id_permiso=permiso.id)

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
    
    """
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
    """
        
    for i in range (len(usuarios)):
        db.session.add(usuarios[i])
    db.session.commit()
    
    return usuarios

    
        
    
    
    

        
        
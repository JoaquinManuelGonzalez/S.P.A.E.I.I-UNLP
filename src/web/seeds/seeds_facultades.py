from datetime import datetime
from src.core.database import db
from src.core.models.usuario import Usuario
from src.core.models.asignatura import Asignatura
from src.core.models.facultad import Facultad
from src.core.models.carrera import Carrera
from src.core.models.postulacion import Postulacion, Estado, Programa, PeriodoPostulacion
#from src.core.models.tipo_carrera import TipoCarrera.py
from src.core.models.alumno import InformacionAlumnoEntrante
from src.core.models.alumno.estado_civil import EstadoCivil
from src.core.models.alumno.pais import Pais
from src.core.models.alumno.genero import Genero
from src.web.forms import Usuario_Form
from src.core.bcrypt import bcrypt
from faker import Faker
import re

## Seeds de Facultades, Carreras, Materias, enlazar puntos focales y postulaciones
def seeds_facultades(usuarios):
    crear_facultades()
    crear_carreras()
    crear_asignaturas()
    enlazar_puntos_focales(usuarios)
    crear_estados()
    crear_programas()
    crear_periodos_de_inscripcion()
    crear_postulaciones(usuarios)

facultades = []
carreras = []
asignaturas = []
estados = []
programas = []
periodos_inscripcion = []

def crear_programas():
    for i in range(2):
        programa = Programa(
            nombre = f'Programa{i}',
        )
        programas.append(programa)
        db.session.add(programa)
    
    db.session.commit()

def crear_facultades():
    for i in range(2):
        facultad = Facultad(
            nombre = f'Facultad{i}',
            acronimo = f'F{i}',
        )
        facultades.append(facultad)
        db.session.add(facultad)
    
    db.session.commit()

def crear_carreras():
    for i in range(2):
        carrera = Carrera(
            nombre = f'Carrera{i}',
            facultad_id = facultades[i].id,
            tipo_carrera_id = 1
        )
        carreras.append(carrera)
        db.session.add(carrera)
    
    db.session.commit()

def crear_asignaturas():
    for i in range(2):
        asignatura = Asignatura(
            nombre = f'Asignatura{i}',
            facultad_id = facultades[i].id,
            carreras = [carreras[i]],
            carga_horaria = 130
        )
        asignaturas.append(asignatura)
        db.session.add(asignatura)

    db.session.commit()

def enlazar_puntos_focales(usuarios):
    puntos_focales = list(filter(lambda x: x.rol.nombre == "punto_focal", usuarios))
    for i in range(len(puntos_focales)):
        if i < len(facultades):
            puntos_focales[i].facultad_id = facultades[i].id
    puntos_focales[0].grado = True
    puntos_focales[1].posgrado = True
    db.session.commit()

def crear_estados():
    estados.append(Estado(
        nombre='Solicitud de Postulacion',
        requiere_accion_presidencia = True,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Solicitud Rechazada',
        requiere_accion_presidencia = False,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion Iniciada',
        requiere_accion_presidencia = False,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion en Proceso',
        requiere_accion_presidencia = False,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion Esperando Validacion por Facultad',
        requiere_accion_presidencia = False,
        requiere_accion_focal = True
    ))
    estados.append(Estado(
        nombre='Postulacion Validada por Facultad',
        requiere_accion_presidencia = False,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion Aceptada',
        requiere_accion_presidencia = False,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion Completada',
        requiere_accion_presidencia = False,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion Finalizada',
        requiere_accion_presidencia = False,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion Cancelada o Interrumpida', #estado para cuando no se llegó al estado 'Aceptada' antes de que comience un nuevo periodo de inscripcion
        requiere_accion_presidencia = False,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion en Espera de Aceptacion', #estado de la postulacion al finalizar el paso 5 del diagrama de flujo
        requiere_accion_presidencia = True,
        requiere_accion_focal = False
    ))
    estados.append(Estado(
        nombre='Postulacion en Espera de ser Completada', #estado de la postulacion al finalizar el paso 7 del diagrama de flujo
        requiere_accion_presidencia = True,
        requiere_accion_focal = False
    ))

    for i in range (len(estados)):
        db.session.add(estados[i])
    db.session.commit()    

def crear_periodos_de_inscripcion():

    periodo1 = PeriodoPostulacion(
        inicio = datetime(2024,1,1),
        fin = datetime(2024,3,1)
    )
    periodos_inscripcion.append(periodo1)
    db.session.add(periodo1)

    periodo2 = PeriodoPostulacion(
        inicio = datetime.now()
    )
    periodos_inscripcion.append(periodo2)
    db.session.add(periodo2)
    
    db.session.commit()


def crear_postulaciones(usuarios):
    alumnos = list(filter(lambda x: x.rol.nombre == "alumno", usuarios))

    genero = Genero.query.first()
    estado_civil = EstadoCivil.query.first()
    pais= Pais.query.first()

    for i in range(len(alumnos)):
        alumno = InformacionAlumnoEntrante(
            nombre = alumnos[i].nombre,
            apellido = alumnos[i].apellido,
            email = alumnos[i].email,
            domicilio_pais_de_residencia = f'DomicilioAlumno{i}',
            fecha_de_nacimiento = datetime(2000, 1, 1),
            discapacitado = False,
            genero = genero,
            estado_civil = estado_civil,
            pais_de_nacimiento = pais,
            pais_de_residencia = pais,
            pais_nacionalidad = pais,
            pasaporte = None,
            cedula_de_identidad = None,
        )       
        db.session.add(alumno)
        db.session.commit()
        alumnos[i].id_alumno = alumno.id
        db.session.commit()
        
        postulacion = Postulacion(
            de_posgrado= False,
            universidad_origen="Universidad de Ejemplo",
            consulado_visacion="Consulado X",
            convenio=None,
            estado=estados[3],
            informacion_alumno_entrante= alumno,
            programa=programas[i],
            periodo_postulacion = periodos_inscripcion[1]
        )
        db.session.add(postulacion)
    db.session.commit()
        


    
        
    
    
    

        
        
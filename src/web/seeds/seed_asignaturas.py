from src.core.services import carreras as carreras_service
from src.core.services import asignaturas as asignaturas_service

def seed_asignaturas():
    # FCAG (Facultad de Ciencias Astronómicas y Geofísicas)
    asignaturas_service.create_asignatura(nombre="Análisis matemático 1", facultad_id=1, carga_horaria=240, id_carreras=[1,2,3])
    asignaturas_service.create_asignatura(nombre="Análisis matemático 2", facultad_id=1, carga_horaria=120, id_carreras=[1,2,3])
    asignaturas_service.create_asignatura(nombre="Física General 1", facultad_id=1, carga_horaria=120, id_carreras=[1,2,3])
    asignaturas_service.create_asignatura(nombre="Física General 2", facultad_id=1, carga_horaria=120, id_carreras=[1,2,3])
    asignaturas_service.create_asignatura(nombre="Física General 3", facultad_id=1, carga_horaria=120, id_carreras=[1,2,3])
    asignaturas_service.create_asignatura(nombre="Álgebra", facultad_id=1, carga_horaria=240, id_carreras=[1,2,3])
    asignaturas_service.create_asignatura(nombre="Astronomía general", facultad_id=3, carga_horaria=250, id_carreras=[1])

    print("Seed completado para la tabla 'asignaturas'.")
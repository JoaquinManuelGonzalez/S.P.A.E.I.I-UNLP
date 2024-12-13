from src.core.services import carreras as carreras_service
from src.core.services import asignaturas as asignaturas_service

def seed_asignaturas():
    # FCAG (Facultad de Ciencias Astronómicas y Geofísicas)
    asignaturas_service.create_asignatura("Análisis matemático 1", 1, [1,2,3])
    asignaturas_service.create_asignatura("Análisis matemático 2", 1, [1,2,3])
    asignaturas_service.create_asignatura("Álgebra", 1, [1,2,3])
    asignaturas_service.create_asignatura("Astronomía general", 3, [1])

    print("Seed completado para la tabla 'asignaturas'.")
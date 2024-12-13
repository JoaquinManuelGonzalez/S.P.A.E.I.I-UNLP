from src.core.services import facultades as facultades_service
from src.core.database import db
from src.core.models.facultad import Facultad

def seed_facultades():
    # Ciencias Exactas y Naturales
    facultades_service.create_facultad(nombre="Facultad de Ciencias Exactas", acronimo="FCE")
    facultades_service.create_facultad(nombre="Facultad de Ciencias Naturales y Museo", acronimo="FCNyM")
    facultades_service.create_facultad(nombre="Facultad de Ciencias Astronómicas y Geofísicas", acronimo="FCAG")
    facultades_service.create_facultad(nombre="Facultad de Informática", acronimo="FINF")

    # Ciencias de la Salud
    facultades_service.create_facultad(nombre="Facultad de Ciencias Médicas", acronimo="FCM")
    facultades_service.create_facultad(nombre="Facultad de Odontología", acronimo="FO")
    facultades_service.create_facultad(nombre="Facultad de Ciencias Veterinarias", acronimo="FCV")

    # Ingeniería
    facultades_service.create_facultad(nombre="Facultad de Ingeniería", acronimo="FING")

    # Ciencias Sociales
    facultades_service.create_facultad(nombre="Facultad de Ciencias Jurídicas y Sociales", acronimo="FCJS")
    facultades_service.create_facultad(nombre="Facultad de Humanidades y Ciencias de la Educación", acronimo="FHCE")
    facultades_service.create_facultad(nombre="Facultad de Trabajo Social", acronimo="FTS")

    # Artes y Diseño
    facultades_service.create_facultad(nombre="Facultad de Bellas Artes", acronimo="FBA")
    facultades_service.create_facultad(nombre="Facultad de Arquitectura y Urbanismo", acronimo="FAU")

    # Ciencias Agrarias
    facultades_service.create_facultad(nombre="Facultad de Ciencias Agrarias y Forestales", acronimo="FCAyF")

    # Comunicación
    facultades_service.create_facultad(nombre="Facultad de Periodismo y Comunicación Social", acronimo="FPyCS")

    print("Seed completado para la tabla 'facultades'.")
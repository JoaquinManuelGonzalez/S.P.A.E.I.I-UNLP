from src.core.services import carreras as carreras_service
from src.core.services import facultades as facultades_service

def seed_carreras():
    # Tipos de carrera
    carreras_service.crear_tipo_carrera(nombre="Grado")
    carreras_service.crear_tipo_carrera(nombre="Especialización")
    carreras_service.crear_tipo_carrera(nombre="Doctorado")
    carreras_service.crear_tipo_carrera(nombre="Maestría")
    
    # FCAG (Facultad de Ciencias Astronómicas y Geofísicas)
    facultad = facultades_service.get_facultad_by_acronimo("FCAG")
    carreras_service.create_carrera(nombre="Licenciatura en Astronomía", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Licenciatura en Meteorología", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Geofísica", facultad_id=facultad.id, tipo_carrera_id=1)

    # FI (Facultad de Ingeniería)
    facultad = facultades_service.get_facultad_by_acronimo("FING")
    carreras_service.create_carrera(nombre="Ingeniería Civil", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Ingeniería Eléctrica", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Ingeniería Mecánica", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Ingeniería Química", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Ingeniería en Computación", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Ingeniería en Sistemas de Información", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Ingeniería Electrónica", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Ingeniería Industrial", facultad_id=facultad.id, tipo_carrera_id=1)

    # FINF (Facultad de Informática)
    facultad = facultades_service.get_facultad_by_acronimo("FINF")
    carreras_service.create_carrera(nombre="Licenciatura en Sistemas", facultad_id=facultad.id, tipo_carrera_id=1)
    carreras_service.create_carrera(nombre="Licenciatura en Informática", facultad_id=facultad.id, tipo_carrera_id=1)

    print("Seed completado para la tabla 'carreras'.")
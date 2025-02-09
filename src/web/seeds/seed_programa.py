from src.core.services import programa_service
from src.core.models.postulacion.programa import Programa
from src.core.database import db

def seed_programa():
    programas = [
        {
            'nombre': 'Programa 1',
            'habilitado': True
        },
        {
            'nombre': 'Programa 2',
            'habilitado': True
        },
        {
            'nombre': 'Programa 3',
            'habilitado': True
        }
    ]

    for programa in programas:
        p = programa_service.crear_programa(**programa)
        db.session.add(p)
    
    db.session.commit()
    print("Seed completado para la tabla 'Programa'")

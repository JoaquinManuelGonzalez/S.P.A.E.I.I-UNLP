from datetime import datetime
from src.core.database import db
from src.core.models.alumno.genero import Genero

def seed_generos():
    """
    Seed para la tabla 'Genero' con los valores:
    - Masculino
    - Femenino
    - No Binario
    """

    generos = [
        {
            "nombre_es": "Masculino",
            "nombre_en": "Male",
            "nombre_pt": "Masculino",
        },
        {
            "nombre_es": "Femenino",
            "nombre_en": "Female",
            "nombre_pt": "Feminino",
        },
        {
            "nombre_es": "No Binario",
            "nombre_en": "Non-binary",
            "nombre_pt": "Não binário",
        },
    ]

    for genero in generos:
        try:
            nuevo_genero = Genero(
                nombre_es=genero["nombre_es"],
                nombre_en=genero["nombre_en"],
                nombre_pt=genero["nombre_pt"],
                creacion=datetime.now(),
                actualizacion=datetime.now(),
            )
            db.session.add(nuevo_genero)
        except Exception as e:
            print(f"Error al agregar el género {genero['nombre_es']}: {e}")

    db.session.commit()
    print("Seed completado para la tabla 'Genero'.")
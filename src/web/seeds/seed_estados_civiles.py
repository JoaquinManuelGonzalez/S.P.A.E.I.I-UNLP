from datetime import datetime
from src.core.database import db
from src.core.models.alumno.estado_civil import EstadoCivil

def seed_estados_civiles():
    """
    Seed para la tabla 'EstadoCivil' con los valores más comunes en tres idiomas.
    """

    estados_civiles = [
        {
            "nombre_es": "Soltero/a",
            "nombre_en": "Single",
            "nombre_pt": "Solteiro/a",
        },
        {
            "nombre_es": "Casado/a",
            "nombre_en": "Married",
            "nombre_pt": "Casado/a",
        },
        {
            "nombre_es": "Divorciado/a",
            "nombre_en": "Divorced",
            "nombre_pt": "Divorciado/a",
        },
        {
            "nombre_es": "Viudo/a",
            "nombre_en": "Widowed",
            "nombre_pt": "Viúvo/a",
        },
        {
            "nombre_es": "Separado/a",
            "nombre_en": "Separated",
            "nombre_pt": "Separado/a",
        },
        {
            "nombre_es": "Unión libre",
            "nombre_en": "Common-law union",
            "nombre_pt": "União estável",
        },
        {
            "nombre_es": "Comprometido/a",
            "nombre_en": "Engaged",
            "nombre_pt": "Comprometido/a",
        },
        {
            "nombre_es": "Pareja de hecho",
            "nombre_en": "Domestic partnership",
            "nombre_pt": "Parceria doméstica",
        },
    ]

    for estado in estados_civiles:
        try:
            nuevo_estado = EstadoCivil(
                nombre_es=estado["nombre_es"],
                nombre_en=estado["nombre_en"],
                nombre_pt=estado["nombre_pt"],
                creacion=datetime.now(),
                actualizacion=datetime.now(),
            )
            db.session.add(nuevo_estado)
        except Exception as e:
            print(f"Error al agregar el estado civil {estado['nombre_es']}: {e}")

    db.session.commit()
    print("Seed completado para la tabla 'EstadoCivil'.")

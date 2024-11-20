from datetime import datetime
from src.core.database import db
from src.core.models.alumno.estado_civil import EstadoCivil

def seed_estados_civiles():
    """
    Seed para la tabla 'EstadoCivil' con los valores más comunes en tres idiomas.
    """

    estados_civiles = [
        {
            "nombre_esp": "Soltero/a",
            "nombre_eng": "Single",
            "nombre_port": "Solteiro/a",
        },
        {
            "nombre_esp": "Casado/a",
            "nombre_eng": "Married",
            "nombre_port": "Casado/a",
        },
        {
            "nombre_esp": "Divorciado/a",
            "nombre_eng": "Divorced",
            "nombre_port": "Divorciado/a",
        },
        {
            "nombre_esp": "Viudo/a",
            "nombre_eng": "Widowed",
            "nombre_port": "Viúvo/a",
        },
        {
            "nombre_esp": "Separado/a",
            "nombre_eng": "Separated",
            "nombre_port": "Separado/a",
        },
        {
            "nombre_esp": "Unión libre",
            "nombre_eng": "Common-law union",
            "nombre_port": "União estável",
        },
        {
            "nombre_esp": "Comprometido/a",
            "nombre_eng": "Engaged",
            "nombre_port": "Comprometido/a",
        },
        {
            "nombre_esp": "Pareja de hecho",
            "nombre_eng": "Domestic partnership",
            "nombre_port": "Parceria doméstica",
        },
    ]

    for estado in estados_civiles:
        try:
            nuevo_estado = EstadoCivil(
                nombre_esp=estado["nombre_esp"],
                nombre_eng=estado["nombre_eng"],
                nombre_port=estado["nombre_port"],
                creacion=datetime.now(),
                actualizacion=datetime.now(),
            )
            db.session.add(nuevo_estado)
        except Exception as e:
            print(f"Error al agregar el estado civil {estado['nombre_esp']}: {e}")

    db.session.commit()
    print("Seed completado para la tabla 'EstadoCivil'.")

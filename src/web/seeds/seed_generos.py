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
            "nombre_esp": "Masculino",
            "nombre_eng": "Male",
            "nombre_port": "Masculino",
        },
        {
            "nombre_esp": "Femenino",
            "nombre_eng": "Female",
            "nombre_port": "Feminino",
        },
        {
            "nombre_esp": "No Binario",
            "nombre_eng": "Non-binary",
            "nombre_port": "Não binário",
        },
    ]

    for genero in generos:
        try:
            nuevo_genero = Genero(
                nombre_esp=genero["nombre_esp"],
                nombre_eng=genero["nombre_eng"],
                nombre_port=genero["nombre_port"],
                creacion=datetime.now(),
                actualizacion=datetime.now(),
            )
            db.session.add(nuevo_genero)
        except Exception as e:
            print(f"Error al agregar el género {genero['nombre_esp']}: {e}")

    db.session.commit()
    print("Seed completado para la tabla 'Genero'.")
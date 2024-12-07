import requests
from datetime import datetime
from src.core.database import db
from src.core.models.alumno.pais import Pais


def fetch_countries():

    url = "https://restcountries.com/v3.1/all"

    response = requests.get(url, stream=False, timeout=60)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al consumir la API: {response.status_code}")
        return []

def seed_countries():

    countries = fetch_countries()

    if not countries:
        print("No se pudieron obtener los datos de países.")
        return

    for country in countries:
        try:
            nombre_es = country["translations"]["spa"]["common"] if "spa" in country["translations"] else country["name"]["common"]
            nombre_en = country["name"]["common"]
            nombre_pt = country["translations"]["por"]["common"] if "por" in country["translations"] else country["name"]["common"]
            hispanohablante = nombre_es in ["España", "México", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panamá", "Cuba", "República Dominicana", "Puerto Rico", "Argentina", "Bolivia", "Chile", "Colombia", "Ecuador", "Paraguay", "Perú", "Uruguay", "Venezuela", "Guinea Ecuatorial"]

            nuevo_pais = Pais(
                nombre_es=nombre_es,
                nombre_en=nombre_en,
                nombre_pt=nombre_pt,
                hispanohablante=hispanohablante,
                creacion=datetime.now(),
                actualizacion=datetime.now()
            )
            db.session.add(nuevo_pais)
            
        except Exception as e:
            print(f"Error al agregar el país {country.get('name', {}).get('common', 'Desconocido')}: {e}")

    db.session.commit()
    print("Seed completado con todos los países.")
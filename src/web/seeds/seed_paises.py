import requests
from datetime import datetime
from src.web import db
from src.core.models.alumno.pais import Pais


def fetch_countries():

    url = "https://restcountries.com/v3.1/all"

    response = requests.get(url)

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
            nombre_esp = country["translations"]["spa"]["common"] if "spa" in country["translations"] else country["name"]["common"]
            nombre_eng = country["name"]["common"]
            nombre_port = country["translations"]["por"]["common"] if "por" in country["translations"] else country["name"]["common"]
            gentilicio_esp = country["demonyms"]["spa"]["m"] if "spa" in country["demonyms"] else "Desconocido"
            gentilicio_eng = country["demonyms"]["eng"]["m"] if "eng" in country["demonyms"] else "Unknown"
            gentilicio_port = country["demonyms"]["por"]["m"] if "por" in country["demonyms"] else "Desconhecido"
            hispanohablante = nombre_esp in ["España", "México", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panamá", "Cuba", "República Dominicana", "Puerto Rico", "Argentina", "Bolivia", "Chile", "Colombia", "Ecuador", "Paraguay", "Perú", "Uruguay", "Venezuela", "Guinea Ecuatorial"]

            nuevo_pais = Pais(
                nombre_esp=nombre_esp,
                nombre_eng=nombre_eng,
                nombre_port=nombre_port,
                gentilicio_esp=gentilicio_esp,
                gentilicio_eng=gentilicio_eng,
                gentilicio_port=gentilicio_port,
                hispanohablante=hispanohablante,
                creacion=datetime.now(),
                actualizacion=datetime.now()
            )
            db.session.add(nuevo_pais)
            
        except Exception as e:
            print(f"Error al agregar el país {country.get('name', {}).get('common', 'Desconocido')}: {e}")

    db.session.commit()
    print("Seed completado con todos los países.")
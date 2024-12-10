from src.core.models.alumno import Pais


def listar_paises():
    paises = Pais.query.all()
    return paises


def get_pais_by_id(id_pais):
    return Pais.query.get(id_pais)
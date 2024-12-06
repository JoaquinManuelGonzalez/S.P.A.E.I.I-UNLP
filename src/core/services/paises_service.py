from src.core.models.alumno import Pais


def listar_paises():
    paises = Pais.query.all()
    return paises
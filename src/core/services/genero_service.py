from src.core.models.alumno import Genero


def listar_generos():
    generos = Genero.query.all()
    return generos
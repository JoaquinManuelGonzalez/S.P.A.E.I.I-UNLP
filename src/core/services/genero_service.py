from src.core.models.alumno import Genero


def listar_generos():
    generos = Genero.query.all()
    return generos

def get_genero_by_id(id_genero):
    genero = Genero.query.get(id_genero)
    return genero
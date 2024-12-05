from src.core.models.alumno import EstadoCivil


def listar_estados_civiles():
    estados_civiles = EstadoCivil.query.all()
    return estados_civiles
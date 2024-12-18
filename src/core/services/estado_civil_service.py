from src.core.models.alumno import EstadoCivil


def listar_estados_civiles():
    estados_civiles = EstadoCivil.query.all()
    return estados_civiles


def get_estado_civil_by_id(id_estado_civil):
    estado_civil = EstadoCivil.query.filter_by(id=id_estado_civil).first()
    return estado_civil
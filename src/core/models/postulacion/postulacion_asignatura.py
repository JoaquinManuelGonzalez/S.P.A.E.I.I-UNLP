from src.core.database import db

postulacion_asignatura = db.Table('postulacion_asignatura',
    db.Column('postulacion_id', db.Integer, db.ForeignKey('postulacion.id'), primary_key=True),
    db.Column('asignatura_id', db.Integer, db.ForeignKey('asignaturas.id'), primary_key=True)
)
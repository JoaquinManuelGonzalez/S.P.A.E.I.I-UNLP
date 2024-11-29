from src.core.database import db

postulacion_tutor = db.Table('postulacion_tutor',
    db.Column('postulacion_id', db.Integer, db.ForeignKey('postulacion.id'), primary_key=True),
    db.Column('tutor_id', db.Integer, db.ForeignKey('tutor.id'), primary_key=True)
)
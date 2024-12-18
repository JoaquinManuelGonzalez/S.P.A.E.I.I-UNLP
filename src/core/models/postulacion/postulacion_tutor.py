from src.core.database import db

postulacion_tutor = db.Table('postulacion_tutor',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('postulacion_id', db.Integer, db.ForeignKey('postulacion.id')),
    db.Column('tutor_id', db.Integer, db.ForeignKey('tutor.id'))
)
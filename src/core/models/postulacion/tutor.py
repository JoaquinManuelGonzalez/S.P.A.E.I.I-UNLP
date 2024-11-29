from src.core.database import db
from datetime import datetime

class Tutor(db.Model):
    __tablename__ = 'tutor'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    es_institucional = db.Column(db.Boolean, nullable=False)
    
    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    postulaciones = db.relationship('Postulacion', secondary='postulacion_tutor', back_populates='tutores')

    def __repr__(self):
        return f'<Tutor id-{self.id}, nombre-{self.nombre}, apellido-{self.apellido}, email-{self.email}, es_institucional-{self.es_institucional}>'
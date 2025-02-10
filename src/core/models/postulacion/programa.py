from src.core.database import db
from datetime import datetime

class Programa(db.Model):
    __tablename__ = 'programa'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    habilitado = db.Column(db.Boolean, default=True)
    
    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    postulaciones = db.relationship('Postulacion', back_populates='programa')

    def __repr__(self):
        return f'<Programa id-{self.id}, nombre-{self.nombre}>'
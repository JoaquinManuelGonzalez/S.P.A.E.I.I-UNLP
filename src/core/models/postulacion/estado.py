from src.core.database import db
from datetime import datetime

class Estado(db.Model):
    __tablename__ = 'estado'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    
    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    postulaciones = db.relationship('Postulacion', back_populates='estado')

    def __repr__(self):
        return f'<Estado id-{self.id}, nombre-{self.nombre}>'
from datetime import datetime
from src.web import db


class Genero(db.Model):
    __tablename__ = "genero"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    informacion_alumnos_entrantes = db.relationship('InformacionAlumnoEntrante', back_populates='genero')

    def __repr__(self):
        return f"<Genero id-{self.id}, nombre-{self.nombre}"

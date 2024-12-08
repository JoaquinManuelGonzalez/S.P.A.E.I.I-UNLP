from datetime import datetime
from src.core.database import db


class EstadoCivil(db.Model):
    __tablename__ = "estado_civil"

    id = db.Column(db.Integer, primary_key=True)
    nombre_es = db.Column(db.String(50), nullable=False)
    nombre_en = db.Column(db.String(50), nullable=False)
    nombre_pt = db.Column(db.String(50), nullable=False)

    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    informacion_alumnos_entrantes = db.relationship('InformacionAlumnoEntrante', back_populates='estado_civil')

    def __repr__(self):
        return f"<EstadoCivil id-{self.id}, nombre-{self.nombre}"
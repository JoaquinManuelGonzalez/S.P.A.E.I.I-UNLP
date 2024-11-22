from src.core.database import db
from datetime import datetime
from src.core.models.facultad import Facultad

class Carrera(db.Model):
    __tablename__ = "carreras"
    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)
    facultad_id = db.Column(db.Integer, db.ForeignKey("facultades.id"), nullable=False)
    facultad = db.relationship("Facultad")

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    deleted_at = db.Column(db.DateTime, nullable=True, default=None)

    def repr(self):
        return f'<Carrera {self.nombre}>'
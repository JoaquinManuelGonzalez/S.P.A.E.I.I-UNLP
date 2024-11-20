from src.core.database import db
from datetime import datetime

class Carrera(db.Model):
    tablename = "carreras"
    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)
    #facultad_id = db.Column(db.Integer, db.ForeignKey("facultades.id"), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    deleted_at = db.Column(db.DateTime, nullable=True, default=None)

    def repr(self):
        return f'<Carrera {self.nombre}>'
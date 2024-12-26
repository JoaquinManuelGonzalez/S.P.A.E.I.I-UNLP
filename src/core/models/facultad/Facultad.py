from src.core.database import db
from datetime import datetime

class Facultad(db.Model):
    __tablename__ = "facultades"
    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)
    acronimo = db.Column(db.String(10), nullable=False)

    puntos_focales = db.relationship(
        'Usuario',
        back_populates='facultad',
        lazy='select'
    )

    carreras = db.relationship("Carrera", back_populates="facultad")

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    deleted_at = db.Column(db.DateTime, nullable=True, default=None)

    def __repr__(self):
        return f'<Facultad {self.nombre}>'
from src.core.database import db
from src.core.models.postulacion import postulacion_asignatura
from datetime import datetime

asignaturas_carreras = db.Table('asignaturas_carreras',
    db.Column('asignatura_id', db.Integer, db.ForeignKey('asignaturas.id'), primary_key=True),
    db.Column('carrera_id', db.Integer, db.ForeignKey('carreras.id'), primary_key=True)
)

class Asignatura(db.Model):
    __tablename__ = "asignaturas"
    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)
    facultad_id = db.Column(db.Integer, db.ForeignKey("facultades.id"), nullable=False)
    facultad = db.relationship("Facultad")
    carreras = db.relationship("Carrera", secondary=asignaturas_carreras, back_populates="asignaturas")
    postulaciones = db.relationship('PostulacionAsignatura', back_populates='asignatura')

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    deleted_at = db.Column(db.DateTime, nullable=True, default=None)

    def repr(self):
        return f'<Asignatura {self.nombre}>'

from src.web import db
from datetime import datetime


class Pasaporte(db.Model):
    __tablename__ = 'pasaporte'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=False)
    id_pais = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    #id_archivos

    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    pais = db.relationship('Pais', back_populates='pasaportes')
    informacion_alumno_entrante = db.relationship('InformacionAlumnoEntrante', back_populates='pasaporte')

    def __repr__(self):
        return f'<Pasaporte id-{self.id}, numero-{self.numero}, pais-{self.pais}'
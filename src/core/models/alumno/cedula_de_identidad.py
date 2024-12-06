from datetime import datetime
from src.core.database import db


class CedulaDeIdentidad(db.Model):
    __tablename__ = 'cedula_de_identidad'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=False)
    id_pais = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    id_archivo = db.Column(db.Integer, db.ForeignKey('archivo.id'), nullable=False)

    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    pais = db.relationship('Pais', back_populates='cedulas_de_identidad')
    informacion_alumno_entrante = db.relationship('InformacionAlumnoEntrante', back_populates='cedula_de_identidad')
    archivo = db.relationship('Archivo', back_populates='cedula_identidad', foreign_keys='Archivo.id_cedula_de_identidad')

    def __repr__(self):
        return f'<CedulaDeIdentidad id-{self.id}, numero-{self.numero}, pais-{self.pais}'
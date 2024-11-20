from datetime import datetime
from src.core.database import db


class Pais(db.Model):
    __tablename__ = 'pais'

    id = db.Column(db.Integer, primary_key=True)
    nombre_esp = db.Column(db.String(100), nullable=False)
    nombre_eng = db.Column(db.String(100), nullable=False)
    nombre_port = db.Column(db.String(100), nullable=False)
    hispanohablante = db.Column(db.Boolean, default=False)

    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    cedulas_de_identidad = db.relationship('CedulaDeIdentidad', back_populates='pais')
    pasaportes = db.relationship('Pasaporte', back_populates='pais')
    nacimientos = db.relationship(
        'InformacionAlumnoEntrante', 
        foreign_keys='InformacionAlumnoEntrante.id_pais_de_nacimiento', 
        back_populates='pais_de_nacimiento'
    )
    residencias = db.relationship(
        'InformacionAlumnoEntrante', 
        foreign_keys='InformacionAlumnoEntrante.id_pais_de_residencia', 
        back_populates='pais_de_residencia'
    )
    nacionalidades = db.relationship(
        'InformacionAlumnoEntrante', 
        foreign_keys='InformacionAlumnoEntrante.id_pais_nacionalidad', 
        back_populates='pais_nacionalidad'
    )

    def __repr__(self):
        return f'<Pais id-{self.id}, nombre-{self.nombre_esp}, hispanohablante-{self.hispanohablante}>'
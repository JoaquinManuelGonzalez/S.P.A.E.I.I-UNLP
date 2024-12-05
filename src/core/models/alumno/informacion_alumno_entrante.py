from src.core.database import db
from datetime import datetime


class InformacionAlumnoEntrante(db.Model):
    __tablename__ = 'informacion_alumno_entrante'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(320), nullable=False)
    domicilio_pais_de_residencia = db.Column(db.String(320), nullable=False)
    fecha_de_nacimiento = db.Column(db.Date, nullable=False)
    discapacitado = db.Column(db.Boolean, nullable=False)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id'), nullable=False)
    id_estado_civil = db.Column(db.Integer, db.ForeignKey('estado_civil.id'), nullable=False)
    id_pais_de_nacimiento = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    id_pais_de_residencia = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    id_pais_nacionalidad = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    id_pasaporte = db.Column(db.Integer, db.ForeignKey('pasaporte.id'), nullable=True)
    id_cedula_de_identidad = db.Column(db.Integer, db.ForeignKey('cedula_de_identidad.id'), nullable=True)

    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    genero = db.relationship('Genero', back_populates='informacion_alumnos_entrantes')
    estado_civil = db.relationship('EstadoCivil', back_populates='informacion_alumnos_entrantes')
    pais_de_nacimiento = db.relationship('Pais', foreign_keys=[id_pais_de_nacimiento], back_populates='nacimientos')
    pais_de_residencia = db.relationship('Pais', foreign_keys=[id_pais_de_residencia], back_populates='residencias')
    pais_nacionalidad = db.relationship('Pais', foreign_keys=[id_pais_nacionalidad], back_populates='nacionalidades')
    pasaporte = db.relationship('Pasaporte', back_populates='informacion_alumno_entrante')
    cedula_de_identidad = db.relationship('CedulaDeIdentidad', back_populates='informacion_alumno_entrante')
    usuario = db.relationship('Usuario', back_populates='informacion_alumno_entrante')
    archivos = db.relationship('Archivo', back_populates='informacion_alumno_entrante')
    postulaciones = db.relationship('Postulacion', back_populates='informacion_alumno_entrante')

    def __repr__(self):
        return f'<InformacionAlumnoEntrante id-{self.id}, nombre-{self.nombre}, apellido-{self.apellido}>'
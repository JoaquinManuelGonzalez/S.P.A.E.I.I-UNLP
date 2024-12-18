from src.core.database import db
from datetime import datetime

class Postulacion(db.Model):
    __tablename__ = 'postulacion'

    id = db.Column(db.Integer, primary_key=True)
    de_posgrado = db.Column(db.Boolean, nullable=False)
    universidad_origen = db.Column(db.String(50), nullable=False)
    consulado_visacion = db.Column(db.String(50), nullable=False)
    convenio = db.Column(db.String(50), nullable=True)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id'), nullable=False)
    id_informacion_alumno_entrante = db.Column(db.Integer, db.ForeignKey('informacion_alumno_entrante.id'), nullable=False)
    id_programa = db.Column(db.Integer, db.ForeignKey('programa.id'), nullable=True)
    
    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    estado = db.relationship('Estado', back_populates='postulaciones')
    informacion_alumno_entrante = db.relationship('InformacionAlumnoEntrante', back_populates='postulaciones')
    tutores = db.relationship('Tutor', secondary='postulacion_tutor', back_populates='postulaciones')
    asignaturas = db.relationship('Asignatura', secondary='postulacion_asignatura', back_populates='postulaciones')
    programa = db.relationship('Programa', back_populates='postulaciones')
    archivos = db.relationship('Archivo', back_populates='postulacion', foreign_keys='Archivo.id_postulacion')

    def __repr__(self):
        return f'<Postulacion id-{self.id}, alumno-{self.informacion_alumno_entrante}, de_posgrado-{self.de_posgrado}, estado-{self.estado}>'
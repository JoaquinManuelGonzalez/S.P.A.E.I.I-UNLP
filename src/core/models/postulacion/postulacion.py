from src.core.database import db
from datetime import datetime

class Postulacion(db.Model):
    __tablename__ = 'postulacion'

    id = db.Column(db.Integer, primary_key=True)
    de_posgrado = db.Column(db.Boolean, nullable=False)
    universidad_origen = db.Column(db.String(50), nullable=False)
    consulado_visacion = db.Column(db.String(50), nullable=False)
    convenio = db.Column(db.String(50), nullable=True)
    
    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    estado = db.relationship('Estado', back_populates='postulaciones')
    informacion_alumno_entrante = db.relationship('InformacionAlumnoEntrante', back_populates='postulaciones')
    tutores = db.relationship('Tutor', secondary='postulacion_tutor', back_populates='postulaciones')
    programa = db.relationship('Programa', back_populates='postulaciones')
    archivo = db.relationship('Archivo', back_populates='postulacion')

    def __repr__(self):
        return f'<Postulacion id-{self.id}, alumno-{self.informacion_alumno_entrante}, de_posgrado-{self.de_posgrado}, estado-{self.estado}>'
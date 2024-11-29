from src.core.database import db

class Archivo(db.Model):
    __tablename__ = 'archivo'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    path = db.Column(db.String(50), nullable=False)
    
    postulacion = db.relationship('Postulacion', back_populates='archivos')
    informacion_alumno_entrante = db.relationship('InformacionAlumnoEntrante', back_populates='archivos')
    pasaporte = db.relationship('Pasaporte', back_populates='archivo')
    cedula_identidad = db.relationship('CedulaDeIdentidad', back_populates='archivo')



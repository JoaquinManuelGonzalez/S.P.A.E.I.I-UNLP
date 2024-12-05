from src.core.database import db

class Archivo(db.Model):
    __tablename__ = 'archivo'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    path = db.Column(db.String(50), nullable=False)

    id_postulacion = db.Column(db.Integer, db.ForeignKey('postulacion.id'), nullable=True)
    id_informacion_alumno_entrante = db.Column(db.Integer, db.ForeignKey('informacion_alumno_entrante.id'), nullable=True)

    postulacion = db.relationship('Postulacion', back_populates='archivos')
    informacion_alumno_entrante = db.relationship('InformacionAlumnoEntrante', back_populates='archivos')
    pasaporte = db.relationship('Pasaporte', back_populates='archivo')
    cedula_identidad = db.relationship('CedulaDeIdentidad', back_populates='archivo')



from src.core.database import db

class Archivo(db.Model):
    __tablename__ = 'archivo'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    path = db.Column(db.String(50), nullable=True)
    id_informacion_alumno_entrante = db.Column(db.Integer, db.ForeignKey('informacion_alumno_entrante.id', name='fk_archivo_informacion'), nullable=True)
    id_pasaporte = db.Column(db.Integer, db.ForeignKey('pasaporte.id', name='fk_archivo_pasaporte'), nullable=True)
    id_cedula_de_identidad = db.Column(db.Integer, db.ForeignKey('cedula_de_identidad.id', name='fk_archivo_cedula'), nullable=True)
    id_postulacion = db.Column(db.Integer, db.ForeignKey('postulacion.id', name='fk_archivo_postulacion'), nullable=True)
    
    postulacion = db.relationship('Postulacion', back_populates='archivos', foreign_keys=[id_postulacion])
    informacion_alumno_entrante = db.relationship('InformacionAlumnoEntrante', back_populates='archivos', foreign_keys=[id_informacion_alumno_entrante])
    pasaporte = db.relationship('Pasaporte', back_populates='archivo', foreign_keys=[id_pasaporte])
    cedula_identidad = db.relationship('CedulaDeIdentidad', back_populates='archivo', foreign_keys=[id_cedula_de_identidad])



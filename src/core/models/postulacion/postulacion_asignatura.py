from src.core.database import db
from datetime import datetime
from src.core.models.postulacion import Postulacion
from src.core.models.asignatura import Asignatura


class PostulacionAsignatura(db.Model):
    __tablename__ ='postulacion_asignatura'

    postulacion_id = db.Column(db.Integer, db.ForeignKey("postulacion.id"), nullable=False, primary_key=True)
    asignatura_id = db.Column(db.Integer, db.ForeignKey("asignaturas.id"), nullable=False, primary_key=True)
    postulacion = db.relationship('Postulacion', back_populates='asignaturas')
    asignatura = db.relationship('Asignatura', back_populates='postulaciones')

    aprobado = db.Column('aprobado', db.Boolean, default=False)
    validado = db.Column('validado', db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    deleted_at = db.Column(db.DateTime, nullable=True, default=None)


'''
postulacion_asignatura = db.Table('postulacion_asignatura',
    db.Column('postulacion_id', db.Integer, db.ForeignKey('postulacion.id'), primary_key=True),
    db.Column('asignatura_id', db.Integer, db.ForeignKey('asignaturas.id'), primary_key=True),
    db.Column('aprobado', db.Boolean, default=False)
    db.Column('validado', db.Boolean, default=False)
)
'''
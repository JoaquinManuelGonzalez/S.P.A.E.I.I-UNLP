from src.core.database import db
from datetime import datetime
from src.core.models.postulacion import Postulacion
from src.core.models.asignatura import Asignatura


class PostulacionAsignatura(db.Model):
    __tablename__ ='postulacion_asignatura'

    postulacion_id = db.Column(db.Integer, db.ForeignKey("postulacion.id", ondelete='CASCADE'), nullable=False, primary_key=True)
    asignatura_id = db.Column(db.Integer, db.ForeignKey("asignaturas.id", ondelete='CASCADE'), nullable=False, primary_key=True)
    postulacion = db.relationship('Postulacion', back_populates='asignaturas')
    asignatura = db.relationship('Asignatura', back_populates='postulaciones')

    aprobado = db.Column('aprobado', db.Integer, default=-1, nullable=False) #Setear el valor a la nota final cuando termina la cursada
    validado = db.Column('validado', db.Boolean, default=False, nullable=False)
    estado = db.Column('estado_cursada', db.String(50), default="Esperando validacion", nullable=False)
    '''
    ESTADOS POSIBLES:
        Esperando validacion -> solo cuando el punto focal todavía no la aceptó. Nunca debería volver a este estado
        Cursando
        Cursada abandonada
        Cursada completada
    '''

    
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
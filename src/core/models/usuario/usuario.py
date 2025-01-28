from datetime import datetime
from src.core.database import db
import enum

class EstadoUsuario(enum.Enum):
    ACTIVO = "activo"
    ELIMINADO = "eliminado"

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.Enum(EstadoUsuario), default=EstadoUsuario.ACTIVO)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=True)
    rol = db.relationship('Rol', back_populates='usuarios')
    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    id_alumno = db.Column(db.Integer, db.ForeignKey('informacion_alumno_entrante.id'), nullable=True)
    informacion_alumno_entrante = db.relationship('InformacionAlumnoEntrante', back_populates='usuario')

    #relacion opcional para puntos focales
    facultad_id = db.Column(db.Integer, db.ForeignKey('facultades.id'), nullable=True)
    facultad = db.relationship('Facultad', back_populates='puntos_focales')
    #atributo para saber si un punto focal atiende grado, posgrado u ambos
    posgrado = db.Column(db.Boolean, default=False)
    grado = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Usuario {self.id} {self.nombre} {self.apellido} {self.email} {self.rol.nombre}>"

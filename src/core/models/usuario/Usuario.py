from src.core.database import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    alias = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    # declaro que voy a tener una columna id_rol a completar con un id de la tabla roles (roles.id)
    # establezco la relacion con la tabla roles
    # id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    # rol = db.relationship('Rol', back_populates='usuarios')
    

    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'<Usuario id-{self.id}, alias-{self.alias}, email-{self.email}, activo-{self.activo}, rol-{self.rol}>'

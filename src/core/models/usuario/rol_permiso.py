from src.core.database import db
from datetime import datetime

class RolPermiso(db.Model):
    __tablename__ = 'rol_permiso'
    
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    rol = db.relationship('Rol', back_populates='rol_permiso')
    id_permiso = db.Column(db.Integer, db.ForeignKey('permiso.id'), nullable=False)
    permiso = db.relationship('Permiso', back_populates='rol_permiso')
    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f"<RolPermiso {self.id} {self.rol.nombre} {self.permiso.nombre}>"
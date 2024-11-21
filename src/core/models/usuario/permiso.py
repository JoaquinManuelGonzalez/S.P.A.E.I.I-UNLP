from src.core.database import db
from datetime import datetime

class Permiso(db.Model):
    __tablename__ = 'permiso'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rol_permiso = db.relationship('RolPermiso', back_populates='permiso')
    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f"<Permiso {self.id} {self.nombre}>"
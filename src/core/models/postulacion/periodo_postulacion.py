from src.core.database import db
from datetime import datetime

class PeriodoPostulacion(db.Model):
    __tablename__ = 'periodo_postulacion'

    id = db.Column(db.Integer, primary_key=True)
    
    inicio = db.Column(db.DateTime, default=datetime.now)
    fin = db.Column(db.DateTime, default=None, nullable = True)

    creacion = db.Column(db.DateTime, default=datetime.now)
    actualizacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    postulaciones = db.relationship('Postulacion', back_populates='periodo_postulacion')

    def activo(self):
        if (self.inicio <= datetime.now()) and ((not self.fin) or self.fin > datetime.now()): #si el inicio ya pasó pero el fin no llegó o no existe
            return True
        else: return False

    def __repr__(self):
        activo = ""
        inicio = self.inicio.strftime("%d-%m-%Y")
        if self.fin: 
            fin = self.fin.strftime("%d-%m-%Y")
        else:
            fin = "En curso"
        if (self.activo()):
            activo = " - Activo"

        return f'{inicio} - {fin}{activo}'
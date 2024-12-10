from src.core.database import db

facultad_punto_focal = db.Table('facultad_punto_focal',
    db.Column('facultad_id', db.Integer, db.ForeignKey('facultad.id'), primary_key=True),
    db.Column('punto_focal_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
)
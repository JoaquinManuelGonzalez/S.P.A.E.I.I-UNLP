from marshmallow import Schema, fields, validate
from src.core.models.postulacion.postulacion import Postulacion

class PostulacionSchema(Schema):
    id = fields.Int(dump_only=True)
    de_posgrado = fields.Bool(required=True)
    universidad_origen = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    consulado_visacion = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    convenio = fields.Str(validate=validate.Length(min=2, max=50))
    id_estado = fields.Int(required=True)
    id_informacion_alumno_entrante = fields.Int(required=True)
    id_programa = fields.Int(required=True)
    
    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

postulacion_schema = PostulacionSchema()
postulaciones_schema = PostulacionSchema(many=True) 
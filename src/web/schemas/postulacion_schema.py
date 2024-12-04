from marshmallow import Schema, fields, validate
from src.core.models.postulacion.postulacion import Postulacion

class PostulacionSchema(Schema):
    id = fields.Int(dump_only=True)
    de_posgrado = fields.Bool(required=True)
    universidad_origen = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    consulado_visacion = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    convenio = fields.Str(validate=validate.Length(min=2, max=50))
    
    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

    @post_load
    def crear_postulacion(self, data, **kwargs):
        return Postulacion(**data)

postulacion_schema = PostulacionSchema()
postulaciones_schema = PostulacionSchema(many=True) 
from marshmallow import Schema, fields, validate


class GeneroSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre_es = fields.Str(required=True, validate=validate.Length(min=2, max=30))
    nombre_en = fields.Str(required=True, validate=validate.Length(min=2, max=30))
    nombre_pt = fields.Str(required=True, validate=validate.Length(min=2, max=30))
    
    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

genero_schema = GeneroSchema()
generos_schema = GeneroSchema(many=True)
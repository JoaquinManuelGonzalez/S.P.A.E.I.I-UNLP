from marshmallow import Schema, fields, validate


class PaisSchema(Schema):
    id = fields.Int(dump_only=True)
    hispanohablante = fields.Bool(required=True)
    nombre_es = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    nombre_en = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    nombre_pt = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    
    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

pais_schema = PaisSchema()
paises_schema = PaisSchema(many=True) 
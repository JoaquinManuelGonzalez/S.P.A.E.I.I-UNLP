from marshmallow import Schema, fields, validate


class EstadoCivilSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre_es = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    nombre_en = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    nombre_pt = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    
    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

estado_civil_schema = EstadoCivilSchema()
estados_civiles_schema = EstadoCivilSchema(many=True)
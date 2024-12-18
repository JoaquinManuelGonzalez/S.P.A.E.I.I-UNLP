from marshmallow import Schema, fields, validate

class ProgramaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(max=50))
    
    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

programa_schema = ProgramaSchema()
programas_schema = ProgramaSchema(many=True)
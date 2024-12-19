from marshmallow import Schema, fields, validate

class TutorSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    apellido = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    es_institucional = fields.Bool(required=True)

    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

tutor_schema = TutorSchema()
tutores_schema = TutorSchema(many=True)
from marshmallow import Schema, fields, validate

class CedulaDeIdentidadSchema(Schema):
    id = fields.Int(dump_only=True)
    numero = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    id_pais = fields.Int(required=True)
    id_archivo = fields.Int(required=True)

    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)
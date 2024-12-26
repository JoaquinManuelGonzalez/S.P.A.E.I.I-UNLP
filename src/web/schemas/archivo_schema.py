from marshmallow import Schema, fields, validate

class ArchivoSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True, validate=validate.Length(min=1, max=320))
    path = fields.Str(validate=validate.Length(min=1, max=320))
    id_informacion_alumno_entrante = fields.Int()
    id_pasaporte = fields.Int()
    id_cedula_de_identidad = fields.Int()
    id_postulacion = fields.Int()

    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

archivo_schema = ArchivoSchema()
archivos_schema = ArchivoSchema(many=True)
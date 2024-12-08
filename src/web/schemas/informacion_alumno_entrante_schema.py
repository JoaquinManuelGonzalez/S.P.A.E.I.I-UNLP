from marshmallow import Schema, fields, validate

class InformacionAlumnoEntranteSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    apellido = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True, validate=validate.Length(min=3, max=320))
    domicilio_pais_de_residencia = fields.Str(required=True, validate=validate.Length(min=3, max=320))
    fecha_de_nacimiento = fields.DateTime(required=True)
    discapacitado = fields.Bool(required=False)
    id_genero = fields.Int(required=True)
    id_estado_civil = fields.Int(required=True)
    id_pais_de_nacimiento = fields.Int(required=True)
    id_pais_de_residencia = fields.Int(required=True)
    id_pais_nacionalidad = fields.Int(required=True)
    id_pasaporte = fields.Int(required=False)
    id_cedula_de_identidad = fields.Int(required=False)

    creacion = fields.DateTime(dump_only=True)
    actualizacion = fields.DateTime(dump_only=True)

informacion_alumno_entrante_schema = InformacionAlumnoEntranteSchema()
informacion_alumnos_entrantes_schema = InformacionAlumnoEntranteSchema(many=True)
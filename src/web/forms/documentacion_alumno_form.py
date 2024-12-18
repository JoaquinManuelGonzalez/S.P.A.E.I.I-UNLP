from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import Optional

class DocumentacionAlumnoForm(FlaskForm):
    pasaporte = FileField('Foto/Archivo de Pasaporte', validators=[Optional()])
    cedula_identidad = FileField('Foto/Archivo de Cédula de Identidad', validators=[Optional()])
    certificado_espanol = FileField('Certificado B1 o Superior de Español', validators=[Optional()])
    certificado_discapacidad = FileField('Certificado de Discapacidad', validators=[Optional()])
    submit = SubmitField('Actualizar Documentación')

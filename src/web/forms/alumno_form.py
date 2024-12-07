from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Optional
from src.core.models.alumno import Pais, Genero, EstadoCivil

# Funciones para cargar opciones en SelectFields
def obtener_paises_choices():
    return [(pais.id, pais.nombre_es) for pais in Pais.query.all()]

def obtener_generos_choices():
    return [(genero.id, genero.nombre_es) for genero in Genero.query.all()]

def obtener_estados_civiles_choices():
    return [(estado.id, estado.nombre_es) for estado in EstadoCivil.query.all()]

class AlumnoForm(FlaskForm):
    # Información del alumno
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    domicilio_pais_de_residencia = StringField('Domicilio País de Residencia', validators=[DataRequired()])
    fecha_de_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    discapacitado = BooleanField('Discapacitado')

    # Relaciones con tablas de referencia
    genero = SelectField('Género', choices=[], validators=[DataRequired()])
    estado_civil = SelectField('Estado Civil', choices=[], validators=[DataRequired()])
    pais_de_nacimiento = SelectField('País de Nacimiento', choices=[], validators=[DataRequired()])
    pais_de_residencia = SelectField('País de Residencia', choices=[], validators=[DataRequired()])
    pais_nacionalidad = SelectField('País de Nacionalidad', choices=[], validators=[DataRequired()])

    # Pasaporte
    numero_pasaporte = StringField('Número de Pasaporte', validators=[Optional()])
    pais_emision_pasaporte = SelectField('País de Emisión del Pasaporte', choices=[], validators=[Optional()])

    # Cédula de identidad
    numero_cedula = StringField('Número de Cédula de Identidad', validators=[Optional()])
    pais_emision_cedula = SelectField('País de Emisión de la Cédula', choices=[], validators=[Optional()])

    # Botón de envío
    submit = SubmitField('Guardar Cambios')

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Optional
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from src.core.models import Pais, Genero, EstadoCivil


# Funciones para cargar opciones en SelectFields
def obtener_paises():
    return Pais.query.all()


def obtener_generos():
    return Genero.query.all()


def obtener_estados_civiles():
    return EstadoCivil.query.all()


class EditarAlumnoForm(FlaskForm):
    # Información del alumno
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    domicilio_pais_de_residencia = StringField('Domicilio País de Residencia', validators=[DataRequired()])
    fecha_de_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    discapacitado = BooleanField('Discapacitado')

    # Relaciones con tablas de referencia
    genero = QuerySelectField('Género', query_factory=obtener_generos, get_label='nombre_es', validators=[DataRequired()])
    estado_civil = QuerySelectField('Estado Civil', query_factory=obtener_estados_civiles, get_label='nombre_es', validators=[DataRequired()])
    pais_de_nacimiento = QuerySelectField('País de Nacimiento', query_factory=obtener_paises, get_label='nombre_es', validators=[DataRequired()])
    pais_de_residencia = QuerySelectField('País de Residencia', query_factory=obtener_paises, get_label='nombre_es', validators=[DataRequired()])
    pais_nacionalidad = QuerySelectField('País de Nacionalidad', query_factory=obtener_paises, get_label='nombre_es', validators=[DataRequired()])

    # Pasaporte
    numero_pasaporte = StringField('Número de Pasaporte', validators=[Optional()])
    pais_emision_pasaporte = QuerySelectField('País de Emisión del Pasaporte', query_factory=obtener_paises, get_label='nombre_es', validators=[Optional()])

    # Cédula de identidad
    numero_cedula = StringField('Número de Cédula de Identidad', validators=[Optional()])
    pais_emision_cedula = QuerySelectField('País de Emisión de la Cédula', query_factory=obtener_paises, get_label='nombre_es', validators=[Optional()])

    # Botón de envío
    submit = SubmitField('Guardar Cambios')

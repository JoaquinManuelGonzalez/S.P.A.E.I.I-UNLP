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
    id_genero = SelectField('Género', choices=[], validators=[DataRequired()])
    id_estado_civil = SelectField('Estado Civil', choices=[], validators=[DataRequired()])
    id_pais_de_nacimiento = SelectField('País de Nacimiento', choices=[], validators=[DataRequired()])
    id_pais_de_residencia = SelectField('País de Residencia', choices=[], validators=[DataRequired()])
    id_pais_nacionalidad = SelectField('País de Nacionalidad', choices=[], validators=[DataRequired()])

    # Pasaporte
    numero_pasaporte = StringField('Número de Pasaporte', validators=[Optional()])
    id_pais_emision_pasaporte = SelectField('País de Emisión del Pasaporte', choices=[], validators=[Optional()])

    # Cédula de identidad
    numero_cedula = StringField('Número de Cédula de Identidad', validators=[Optional()])
    id_pais_emision_cedula = SelectField('País de Emisión de la Cédula', choices=[], validators=[Optional()])

    # Botón de envío
    submit = SubmitField('Guardar Cambios')

    # Sobrescribir el método __init__ para poblar los campos SelectField y precargar datos
    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)

        # Poblar las opciones para los SelectFields
        self.id_genero.choices = obtener_generos_choices()
        self.id_estado_civil.choices = obtener_estados_civiles_choices()
        self.id_pais_de_nacimiento.choices = obtener_paises_choices()
        self.id_pais_de_residencia.choices = obtener_paises_choices()
        self.id_pais_nacionalidad.choices = obtener_paises_choices()
        self.id_pais_emision_pasaporte.choices = obtener_paises_choices()
        self.id_pais_emision_cedula.choices = obtener_paises_choices()
        

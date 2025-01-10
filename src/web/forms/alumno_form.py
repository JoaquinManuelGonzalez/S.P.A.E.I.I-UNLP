import re
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    BooleanField,
    SubmitField,
    ValidationError,
)
from wtforms.validators import DataRequired, Email, Optional, Length
from src.core.models.alumno import Pais, Genero, EstadoCivil


# Funciones para cargar opciones en SelectFields
def obtener_paises_choices():
    return [(pais.id, pais.nombre_es) for pais in Pais.query.all()]


def obtener_generos_choices():
    return [(genero.id, genero.nombre_es) for genero in Genero.query.all()]


def obtener_estados_civiles_choices():
    return [(estado.id, estado.nombre_es) for estado in EstadoCivil.query.all()]


class AlumnoForm(FlaskForm):

    def validate_only_letters(self, field):
        """
        Validates that the field contains only letters.

        Args:
            field (Field): The field to validate.

        Raises:
            ValidationError: If the field contains characters other than letters.
        """

        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", field.data):
            raise ValidationError("El campo solo puede contener letras.")

    def validate_only_numbers(self, field):
        """
        Validates that the field contains only numbers.

        Args:
            field (Field): The field to validate.

        Raises:
            ValidationError: If the field contains characters other than numbers.
        """

        if not re.match(r"^\d+$", field.data):
            raise ValidationError("El campo solo puede contener números.")

    def validate_only_letters_and_numbers(self, field):
        """
        Validates that the field contains only letters and numbers.

        Args:
            field (Field): The field to validate.

        Raises:
            ValidationError: If the field contains characters other than letters and numbers.
        """

        if not re.match(r"^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ\s]+$", field.data):
            raise ValidationError("El campo solo puede contener letras y números.")

    # Información del alumno
    nombre = StringField(
        "Nombre",
        validators=[
            DataRequired(message="Este campo es requerido"),
            validate_only_letters,
            Length(max=50, message="El nombre no puede tener más de 50 caracteres"),
        ],
    )
    apellido = StringField(
        "Apellido",
        validators=[
            DataRequired(message="Este campo es requerido"),
            validate_only_letters,
            Length(max=50, message="El apellido no puede tener más de 50 caracteres"),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Este campo es requerido"),
            Email(message="El email ingresado no es válido."),
            Length(max=320, message="El email no puede tener más de 320 caracteres"),
        ],
    )
    domicilio_pais_de_residencia = StringField(
        "Domicilio País de Residencia",
        validators=[
            DataRequired(message="Este campo es requerido"),
            validate_only_letters_and_numbers,
            Length(
                max=320, message="El domicilio no puede tener más de 320 caracteres"
            ),
        ],
    )
    fecha_de_nacimiento = DateField(
        "Fecha de Nacimiento",
        validators=[DataRequired(message="Este campo es requerido")],
    )
    discapacitado = BooleanField("Discapacitado")

    # Relaciones con tablas de referencia
    id_genero = SelectField(
        "Género",
        choices=[],
        validators=[DataRequired(message="Este campo es requerido")],
    )
    id_estado_civil = SelectField(
        "Estado Civil",
        choices=[],
        validators=[DataRequired(message="Este campo es requerido")],
    )
    id_pais_de_nacimiento = SelectField(
        "País de Nacimiento",
        choices=[],
        validators=[DataRequired(message="Este campo es requerido")],
    )
    id_pais_de_residencia = SelectField(
        "País de Residencia",
        choices=[],
        validators=[DataRequired(message="Este campo es requerido")],
    )
    id_pais_nacionalidad = SelectField(
        "País de Nacionalidad",
        choices=[],
        validators=[DataRequired(message="Este campo es requerido")],
    )

    # Botón de envío
    submit = SubmitField("Guardar Cambios")

    # Sobrescribir el método __init__ para poblar los campos SelectField y precargar datos
    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)

        # Poblar las opciones para los SelectFields
        self.id_genero.choices = obtener_generos_choices()
        self.id_estado_civil.choices = obtener_estados_civiles_choices()
        self.id_pais_de_nacimiento.choices = obtener_paises_choices()
        self.id_pais_de_residencia.choices = obtener_paises_choices()
        self.id_pais_nacionalidad.choices = obtener_paises_choices()


class PasaporteForm(FlaskForm):

    def validate_only_letters_and_numbers(self, field):
        """
        Validates that the field contains only letters and numbers.

        Args:
            field (Field): The field to validate.

        Raises:
            ValidationError: If the field contains characters other than letters and numbers.
        """

        if not re.match(r"^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ\s]+$", field.data):
            raise ValidationError("El campo solo puede contener letras y números.")

    numero = StringField(
        "Número de Pasaporte",
        validators=[
            Optional(),
            validate_only_letters_and_numbers,
        ],
    )
    id_pais = SelectField(
        "País de Emisión del Pasaporte",
        choices=[],
        validators=[Optional()],
    )
    submit = SubmitField("Guardar Cambios")

    def __init__(self, *args, **kwargs):
        super(PasaporteForm, self).__init__(*args, **kwargs)

        # Poblar las opciones para los SelectFields
        self.id_pais.choices = obtener_paises_choices()


class CedulaForm(FlaskForm):

    def validate_only_letters_and_numbers(self, field):
        """
        Validates that the field contains only letters and numbers.

        Args:
            field (Field): The field to validate.

        Raises:
            ValidationError: If the field contains characters other than letters and numbers.
        """

        if not re.match(r"^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ\s]+$", field.data):
            raise ValidationError("El campo solo puede contener letras y números.")

    numero = StringField(
        "Número de Cédula de Identidad",
        validators=[
            Optional(),
            validate_only_letters_and_numbers,
        ],
    )
    id_pais = SelectField(
        "País de Emisión de la Cédula de Identidad",
        choices=[],
        validators=[Optional()],
    )
    submit = SubmitField("Guardar Cambios")

    def __init__(self, *args, **kwargs):
        super(CedulaForm, self).__init__(*args, **kwargs)

        # Poblar las opciones para los SelectFields
        self.id_pais.choices = obtener_paises_choices()
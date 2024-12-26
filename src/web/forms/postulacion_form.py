from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    SubmitField, 
    SelectField, 
    DateField, 
    IntegerField,
    BooleanField,
    EmailField,
    FileField
)
from flask_wtf.file import FileAllowed
from wtforms.validators import (
    DataRequired, 
    Length, 
    Email, 
    ValidationError,
    Optional
)
from typing import TypedDict
from src.web.forms.validators import file_size_limit
from src.core.models.alumno.estado_civil import EstadoCivil
from src.core.models.alumno.genero import Genero
from src.core.models.alumno.pais import Pais
from src.core.models.postulacion.programa import Programa
import re
from wtforms_sqlalchemy.fields import QuerySelectField

class PostulacionFormValues(TypedDict):	
    apellido: str
    nombre: str
    email: str
    genero: str
    fecha_nacimiento: datetime
    pais_nacimiento: str
    pais_residencia: str
    domicilio: str
    nacionalidad: str
    numero_pasaporte: str
    pais_emision_pasaporte: str
    foto_pasaporte: str
    numero_cedula_identidad: str
    foto_cedula_identidad: str
    pais_emision_cedula_identidad: str
    estado_civil: str
    certificado_b1: str
    universidad_origen: str
    de_grado: bool
    de_posgrado: bool
    plan_trabajo: str
    consulado_visacion: str
    por_convenio: bool
    por_programa: bool
    convenio: str
    programa: str
    carta_recomendacion: str
    apellido_tutor_institucional: str
    nombre_tutor_institucional: str
    email_tutor_institucional: str
    apellido_tutor_academico: str
    nombre_tutor_academico: str
    email_tutor_academico: str

class PostulacionForm(FlaskForm):
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


    apellido = StringField(
        "Apellido",
        validators=[DataRequired(), Length(min=2, max=50), validate_only_letters]
    )
    nombre = StringField(
        "Nombre",
        validators=[DataRequired(), Length(min=2, max=50), validate_only_letters]
    )
    email = EmailField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    genero = QuerySelectField(
        "Género conforme pasaporte",
        query_factory=lambda: Genero.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Seleccione un género",
        validators=[DataRequired()]
    )
    fecha_nacimiento = DateField(
        "Fecha de nacimiento",
        validators=[DataRequired()]
    )
    pais_nacimiento = QuerySelectField(
        "País de nacimiento",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[DataRequired()]
    )
    pais_residencia = QuerySelectField(
        "País de residencia",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[DataRequired()]
    )
    domicilio = StringField(
        "Domicilio del país de residencia",
        validators=[DataRequired(), Length(min=2, max=100), validate_only_letters_and_numbers]
    )
    nacionalidad = QuerySelectField(
        "Nacionalidad",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[DataRequired()]
    )
    numero_pasaporte = StringField(
        "Número de pasaporte",
        validators=[Length(min=2, max=20), validate_only_letters_and_numbers]
    )
    pais_emision_pasaporte = QuerySelectField(
        "País de emisión del pasaporte",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[]
    )
    foto_pasaporte = FileField(
        "Foto del pasaporte",
        validators=[
            FileAllowed(["jpg", "jpng", "png", "pdf"], "Solo se permiten archivos .jpg, .jpeg, .png y .pdf"),
            file_size_limit(5),]
    )
    numero_cedula_identidad = StringField(
        "Número de cédula de identidad",
        validators=[Length(min=2, max=20), validate_only_numbers]
    )
    pais_emision_cedula_identidad = QuerySelectField(
        "País de emisión de la cédula de identidad",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[]
    )
    foto_cedula_identidad = FileField(
        "Foto de la cédula de identidad",
        validators=[
            FileAllowed(["jpg", "jpng", "png", "pdf"], "Solo se permiten archivos .jpg, .jpeg, .png y .pdf"),
            file_size_limit(5),]
    )
    estado_civil = QuerySelectField(
        "Estado civil",
        query_factory=lambda: EstadoCivil.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Seleccione su estado civil",
        validators=[DataRequired()]
    )
    certificado_b1 = FileField(
        "Certificado B1 o superior de español",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5), Optional()]
    )
    universidad_origen = StringField(
        "Universidad de origen",
        validators=[DataRequired(), Length(min=2, max=100), validate_only_letters_and_numbers]
    )
    de_grado = BooleanField(
        "¿Es estudiante de grado?"
    )
    de_posgrado = BooleanField(
        "¿Es estudiante de posgrado?"
    )
    plan_trabajo = FileField(
        "Plan de trabajo",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5),]
    )
    consulado_visacion = StringField(
        "Consulado de visación",
        validators=[Length(min=2, max=100)]
    )
    por_convenio = BooleanField(
        "Estudiante de grado"
    )
    por_programa = BooleanField(
        "Estudiante de posgrado"
    )
    convenio = StringField(
        "Convenio",
        validators=[Length(min=2, max=50)]
    )
    programa = QuerySelectField(
        "Programa",
        query_factory=lambda: Programa.query.all(),
        get_label="nombre",
        allow_blank=True,
        blank_text="Selecciona un programa",
        validators=[Length(min=2, max=50)]
    )
    carta_recomendacion = FileField(
        "Carta de recomendación",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5),]
    )
    apellido_tutor_institucional = StringField(
        "Apellido del tutor institucional",
        validators=[DataRequired(), Length(min=2, max=50), validate_only_letters]
    )
    nombre_tutor_institucional = StringField(
        "Nombre del tutor institucional",
        validators=[DataRequired(), Length(min=2, max=50), validate_only_letters]
    )
    email_tutor_institucional = EmailField(
        "Email del tutor institucional",
        validators=[DataRequired(), Email()]
    )
    apellido_tutor_academico = StringField(
        "Apellido del tutor académico",
        validators=[DataRequired(), Length(min=2, max=50), validate_only_letters]
    )
    nombre_tutor_academico = StringField(
        "Nombre del tutor académico",
        validators=[DataRequired(), Length(min=2, max=50), validate_only_letters]
    )  
    email_tutor_academico = EmailField(
        "Email del tutor académico",
        validators=[DataRequired(), Email()]
    )
    

    def values(self) -> PostulacionFormValues:
        return {
            "apellido": self.apellido.data,
            "nombre": self.nombre.data,
            "email": self.email.data,
            "genero": self.genero.data,
            "fecha_nacimiento": self.fecha_nacimiento.data,
            "pais_nacimiento": self.pais_nacimiento.data,
            "pais_residencia": self.pais_residencia.data,
            "domicilio": self.domicilio.data,
            "nacionalidad": self.nacionalidad.data,
            "numero_pasaporte": self.numero_pasaporte.data,
            "pais_emision_pasaporte": self.pais_emision_pasaporte.data,
            "foto_pasaporte": self.foto_pasaporte.data,
            "numero_cedula_identidad": self.numero_cedula_identidad.data,
            "pais_emision_cedula_identidad": self.pais_emision_cedula_identidad.data,
            "foto_cedula_identidad": self.foto_cedula_identidad.data,
            "estado_civil": self.estado_civil.data,
            "certificado_b1": self.certificado_b1.data,
            "universidad_origen": self.universidad_origen.data,
            "de_grado": self.de_grado.data,
            "de_posgrado": self.de_posgrado.data,
            "plan_trabajo": self.plan_trabajo.data,
            "consulado_visacion": self.consulado_visacion.data,
            "por_convenio": self.por_convenio.data,
            "por_programa": self.por_programa.data,
            "convenio": self.convenio.data,
            "programa": self.programa.data,
            "carta_recomendacion": self.carta_recomendacion.data,
            "apellido_tutor_institucional": self.apellido_tutor_institucional.data,
            "nombre_tutor_institucional": self.nombre_tutor_institucional.data,
            "email_tutor_institucional": self.email_tutor_institucional.data,
            "apellido_tutor_academico": self.apellido_tutor_academico.data,
            "nombre_tutor_academico": self.nombre_tutor_academico.data,
            "email_tutor_academico": self.email_tutor_academico.data,
        }
    
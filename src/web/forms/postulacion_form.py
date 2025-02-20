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
    Optional,
    InputRequired
)
from typing import TypedDict
from src.web.forms.validators import file_size_limit
from src.core.models.alumno.estado_civil import EstadoCivil
from src.core.models.alumno.genero import Genero
from src.core.models.alumno.pais import Pais
from src.core.models.postulacion.programa import Programa
import re
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import RadioField

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
    certificado_discapacidad: str
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
        
    def optional_only_numbers(self, field):
        if field.data:
            pattern = re.compile(r"^\d+$")
            if not pattern.match(field.data):
                raise ValidationError("Solo se permiten números")

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
        
    def optional_only_letters_and_numbers(self, field):
        if field.data:  # Si el campo tiene un valor, aplica la validación
            pattern = re.compile(r"^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ\s]+$")
            if not pattern.match(field.data):
                raise ValidationError("Solo se permiten letras y números.")
            
    def validate_pais_emision_pasaporte(self, field):
        # Si el usuario ingresó datos en el pasaporte, el país debe ser obligatorio
        if self.numero_pasaporte.data or self.foto_pasaporte.data:
            if not field.data:
                raise ValidationError("Debe seleccionar un país de emisión del pasaporte")
            
    def validate_pais_emision_cedula_identidad(self, field):
        # Si el usuario ingresó datos en la cédula de identidad, el país debe ser obligatorio
        if self.numero_cedula_identidad.data or self.foto_cedula_identidad.data:
            if not field.data:
                raise ValidationError("Debe seleccionar un país de emisión de la cédula de identidad")
            
    def validate_consulado_visacion(self, field):
        if not self.plan_trabajo.data:
            if not field.data:
                raise ValidationError("Debe ingresar el consulado de visación")
            
    def optional_length(self, field):
        if field.data:
            if len(field.data) < 2 or len(field.data) > 20:
                raise ValidationError("El campo debe tener entre 2 y 20 caracteres")
            
    def validate_programa(self, field):
            if not self.convenio.data:
                if not field.data:
                    raise ValidationError("Debe seleccionar un programa")
                
    def validate_convenio(self, field):
            if not self.programa.data:
                if not field.data:
                    raise ValidationError("Debe ingresar un convenio")
                else:
                    if len(field.data) < 2 or len(field.data) > 50:
                        raise ValidationError("El campo debe tener entre 2 y 50 caracteres")
                    
    def validate_fecha_nacimiento(self, field):
        if field.data:  # Si hay una fecha ingresada
            fecha_actual = datetime.today().date()  # Fecha de hoy (solo la parte de la fecha)
            if field.data >= fecha_actual:
                raise ValidationError("La fecha de nacimiento debe ser anterior a la fecha actual.")


    genero = QuerySelectField(
        "Género conforme pasaporte",
        query_factory=lambda: Genero.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Seleccione un género",
        validators=[DataRequired(message="Debe seleccionar un género")]
    )
    pais_residencia = QuerySelectField(
        "País de residencia",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[DataRequired(message="Debe seleccionar un país de residencia")]
    )
    domicilio = StringField(
        "Domicilio del país de residencia",
        validators=[DataRequired(message="Debe ingresar su domicilio"), Length(min=2, max=100, message="El domicilio debe tener 2 letras como mínimo y 100 como máximo"), validate_only_letters_and_numbers]
    )
    nacionalidad = QuerySelectField(
        "Nacionalidad",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[DataRequired(message="Debe seleccionar una nacionalidad")],
        render_kw={"id": "nacionalidad"}
    )
    numero_pasaporte = StringField(
        "Número de pasaporte",
        validators=[optional_length, optional_only_letters_and_numbers]
    )
    pais_emision_pasaporte = QuerySelectField(
        "País de emisión del pasaporte",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[validate_pais_emision_pasaporte]
    )
    foto_pasaporte = FileField(
        "Foto del pasaporte",
        validators=[
            FileAllowed(["jpg", "jpng", "png", "pdf"], "Solo se permiten archivos .jpg, .jpeg, .png y .pdf"),
            file_size_limit(5),]
    )
    numero_cedula_identidad = StringField(
        "Número de cédula de identidad",
        validators=[optional_length, optional_only_numbers]
    )
    pais_emision_cedula_identidad = QuerySelectField(
        "País de emisión de la cédula de identidad",
        query_factory=lambda: Pais.query.all(),
        get_label="nombre_es",
        allow_blank=True,
        blank_text="Selecciona un país",
        validators=[validate_pais_emision_cedula_identidad]
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
        validators=[DataRequired(message="Debe seleccionar un estado civil")]
    )
    certificado_b1 = FileField(
        "Certificado B1 o superior de español",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5), Optional()]
    )
    certificado_discapacidad = FileField(
        "Certificado de discapacidad",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5), Optional()]
    )
    universidad_origen = StringField(
        "Universidad de origen",
        validators=[DataRequired(message="Debe ingresar su universidad de origen"), Length(min=2, max=100, message="La universidad debe tener 2 letras como mínimo y 100 como máximo"), validate_only_letters_and_numbers]
    )
    plan_trabajo = FileField(
        "Plan de trabajo",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5),
            Optional()
        ]
    )
    consulado_visacion = StringField(
        "Consulado de visación",
        validators=[validate_consulado_visacion]
    )
    convenio = StringField(
        "Convenio",
        validators=[validate_convenio]
    )
    programa = QuerySelectField(
        "Programa",
        query_factory=lambda: Programa.query.filter_by(habilitado=True).all(),
        get_label="nombre",
        allow_blank=True,
        blank_text="Selecciona un programa",
        validators=[validate_programa]
    )
    carta_recomendacion = FileField(
        "Carta de recomendación",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5),
            DataRequired(message="Debe adjuntar una carta de recomendación")
        ]
    )
    apellido_tutor_institucional = StringField(
        "Apellido del tutor institucional",
        validators=[DataRequired(message="Debe ingresar el apellido del tutor institucional"), Length(min=2, max=50, message="El apellido debe tener 2 letras como mínimo y 50 como máximo"), validate_only_letters]
    )
    nombre_tutor_institucional = StringField(
        "Nombre del tutor institucional",
        validators=[DataRequired(message="Debe ingresar el nombre del tutor institucional"), Length(min=2, max=50, message="El nombre debe tener 2 letras como mínimo y 50 como máximo"), validate_only_letters]
    )
    email_tutor_institucional = EmailField(
        "Email del tutor institucional",
        validators=[DataRequired(message="Debe ingresar el email del tutor institucional"), Email(message="Debe ingresar un mail válido")]
    )
    apellido_tutor_academico = StringField(
        "Apellido del tutor académico",
        validators=[DataRequired(message="Debe ingresar el apellido del tutor académico"), Length(min=2, max=50, message="El apellido debe tener 2 letras como mínimo y 50 como máximo"), validate_only_letters]
    )
    nombre_tutor_academico = StringField(
        "Nombre del tutor académico",
        validators=[DataRequired(message="Debe ingresar el nombre del tutor académico"), Length(min=2, max=50, message="El nombre debe tener 2 letras como mínimo y 50 como máximo"), validate_only_letters]
    )  
    email_tutor_academico = EmailField(
        "Email del tutor académico",
        validators=[DataRequired(message="Debe ingresar el email del tutor académico"), Email(message="Debe ingresar un mail válido")]
    )
    

    def values(self) -> PostulacionFormValues:
        return {
            "genero": self.genero.data,
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
            "certificado_discapacidad": self.certificado_discapacidad.data,
            "universidad_origen": self.universidad_origen.data,
            "plan_trabajo": self.plan_trabajo.data,
            "consulado_visacion": self.consulado_visacion.data,
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
    
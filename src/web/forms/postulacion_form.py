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
    ValidationError
)
from typing import TypedDict
from src.web.forms.validators import file_size_limit

class PostulacionFormValues(TypedDict):	
    apellido: str
    nombre: str
    email: str
    genero: str
    domicilio: str
    fecha_nacimiento: datetime
    nacionalidad: str
    numero_pasaporte: str
    foto_pasaporte: str
    pais_emision_pasaporte: str
    numero_cedula_identidad: str
    foto_cedula_identidad: str
    pais_emision_cedula_identidad: str
    estado_civil: str
    pais_nacimiento: str
    pais_residencia: str
    universidad_origen: str
    de_grado: bool
    de_posgrado: bool
    consulado_visacion: str
    plan_trabajo: str
    apellido_tutor_institucional: str
    nombre_tutor_institucional: str
    email_tutor_institucional: str
    apellido_tutor_academico: str
    nombre_tutor_academico: str
    email_tutor_academico: str
    por_convenio: bool
    por_programa: bool
    convenio: str
    programa: str
    carta_recomendacion: str
    es_hispanohalante: bool
    certificado_ingles: str


class PostulacionForm(FlaskForm):
    apellido = StringField(
        "Apellido",
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    nombre = StringField(
        "Nombre",
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    email = EmailField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    genero = SelectField(
        "Género conforme pasaporte",
        choices=[("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")],
        validators=[DataRequired()]
    )
    domicilio = StringField(
        "Domicilio del país de residencia",
        validators=[DataRequired(), Length(min=2, max=100)]
    )
    fecha_nacimiento = DateField(
        "Fecha de nacimiento",
        validators=[DataRequired()]
    )
    nacionalidad = SelectField(
        "Nacionalidad",
        choices=[("AR", "Argentina"), ("BR", "Brasil"), ("UY", "Uruguay")],
        validators=[DataRequired()]
    )
    numero_pasaporte = StringField(
        "Número de pasaporte",
        validators=[Length(min=2, max=20)]
    )
    foto_pasaporte = FileField(
        "Foto del pasaporte",
        validators=[
            FileAllowed(["jpg", "jpng", "png"], "Solo se permiten archivos .jpg, .jpeg y .png"),
            file_size_limit(5),]
    )
    pais_emision_pasaporte = SelectField(
        "País de emisión del pasaporte",
        choices=[("AR", "Argentina"), ("BR", "Brasil"), ("UY", "Uruguay")],
        validators=[]
    )
    numero_cedula_identidad = StringField(
        "Número de cédula de identidad",
        validators=[Length(min=2, max=20)]
    )
    foto_cedula_identidad = FileField(
        "Foto de la cédula de identidad",
        validators=[
            FileAllowed(["jpg", "jpng", "png"], "Solo se permiten archivos .jpg, .jpeg y .png"),
            file_size_limit(5),]
    )
    pais_emision_cedula_identidad = SelectField(
        "País de emisión de la cédula de identidad",
        choices=[("AR", "Argentina"), ("BR", "Brasil"), ("UY", "Uruguay")],
        validators=[]
    )
    estado_civil = SelectField(
        "Estado civil",
        choices=[("S", "Soltero/a"), ("C", "Casado/a"), ("D", "Divorciado/a"), ("V", "Viudo/a")],
        validators=[DataRequired()]
    )
    pais_nacimiento = SelectField(
        "País de nacimiento",
        choices=[("AR", "Argentina"), ("BR", "Brasil"), ("UY", "Uruguay")],
        validators=[DataRequired()]
    )
    pais_residencia = SelectField(
        "País de residencia",
        choices=[("AR", "Argentina"), ("BR", "Brasil"), ("UY", "Uruguay")],
        validators=[DataRequired()]
    )
    universidad_origen = StringField(
        "Universidad de origen",
        validators=[DataRequired(), Length(min=2, max=100)]
    )
    de_grado = BooleanField(
        "¿Es estudiante de grado?"
    )
    de_posgrado = BooleanField(
        "¿Es estudiante de posgrado?"
    )
    consulado_visacion = StringField(
        "Consulado de visación",
        validators=[Length(min=2, max=100)]
    )
    plan_trabajo = FileField(
        "Plan de trabajo",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5),]
    )
    apellido_tutor_institucional = StringField(
        "Apellido del tutor institucional",
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    nombre_tutor_institucional = StringField(
        "Nombre del tutor institucional",
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    email_tutor_institucional = EmailField(
        "Email del tutor institucional",
        validators=[DataRequired(), Email()]
    )
    apellido_tutor_academico = StringField(
        "Apellido del tutor académico",
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    nombre_tutor_academico = StringField(
        "Nombre del tutor académico",
        validators=[DataRequired(), Length(min=2, max=50)]
    )  
    email_tutor_academico = EmailField(
        "Email del tutor académico",
        validators=[DataRequired(), Email()]
    )
    por_convenio = BooleanField(
        "¿Viene por convenio?"
    )
    por_programa = BooleanField(
        "¿Viene por programa?"
    )
    convenio = StringField(
        "Convenio",
        validators=[Length(min=2, max=50)]
    )
    programa = StringField(
        "Programa",
        validators=[Length(min=2, max=50)]
    )
    carta_recomendacion = FileField(
        "Carta de recomendación",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5),]
    )
    es_hispanohalante = BooleanField(
        "¿Es hispanohablante?"
    )
    certificado_ingles = FileField(
        "Certificado de inglés",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            file_size_limit(5),]
    )

    def values(self) -> PostulacionFormValues:
        return {
            "apellido": self.apellido.data,
            "nombre": self.nombre.data,
            "email": self.email.data,
            "genero": self.genero.data,
            "domicilio": self.domicilio.data,
            "fecha_nacimiento": self.fecha_nacimiento.data,
            "nacionalidad": self.nacionalidad.data,
            "numero_pasaporte": self.numero_pasaporte.data,
            "foto_pasaporte": self.foto_pasaporte.data,
            "pais_emision_pasaporte": self.pais_emision_pasaporte.data,
            "numero_cedula_identidad": self.numero_cedula_identidad.data,
            "foto_cedula_identidad": self.foto_cedula_identidad.data,
            "pais_emision_cedula_identidad": self.pais_emision_cedula_identidad.data,
            "estado_civil": self.estado_civil.data,
            "pais_nacimiento": self.pais_nacimiento.data,
            "pais_residencia": self.pais_residencia.data,
            "universidad_origen": self.universidad_origen.data,
            "de_grado": self.de_grado.data,
            "de_posgrado": self.de_posgrado.data,
            "consulado_visacion": self.consulado_visacion.data,
            "plan_trabajo": self.plan_trabajo.data,
            "apellido_tutor_institucional": self.apellido_tutor_institucional.data,
            "nombre_tutor_institucional": self.nombre_tutor_institucional.data,
            "email_tutor_institucional": self.email_tutor_institucional.data,
            "apellido_tutor_academico": self.apellido_tutor_academico.data,
            "nombre_tutor_academico": self.nombre_tutor_academico.data,
            "email_tutor_academico": self.email_tutor_academico.data,
            "por_convenio": self.por_convenio.data,
            "por_programa": self.por_programa.data,
            "convenio": self.convenio.data,
            "programa": self.programa.data,
            "carta_recomendacion": self.carta_recomendacion.data,
            "es_hispanohalante": self.es_hispanohalante.data,
            "certificado_ingles": self.certificado_ingles.data
        }


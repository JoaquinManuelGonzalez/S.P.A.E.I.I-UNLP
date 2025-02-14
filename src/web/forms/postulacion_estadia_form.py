from flask_wtf import FlaskForm
from wtforms import FileField, BooleanField, DateField, IntegerField, StringField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileAllowed
from src.web.forms.validators import file_size_limit






class PostulacionEstadiaForm(FlaskForm):
    psicofisico = FileField(
        "Psicofísico",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            DataRequired()]
    )
    politicas_institucionales = FileField(
        "Políticas institucionales",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            DataRequired()]
    )
    fecha_ingreso = DateField(
        "Fecha de ingreso al país",
        validators=[DataRequired()]
    )
    duracion_estadia = IntegerField(
        "Duración de la estadía en meses",
        validators=[DataRequired()]
    )
    consulado_visacion = StringField(
        "Consulado de visación",
        validators=[Length(max=50)]
    )

    def values(self):
        return {
            "psicofisico": self.psicofisico.data,
            "politicas_institucionales": self.politicas_institucionales.data,
            "discapacidad": self.discapacidad.data,
            "certificado_discapacidad": self.certificado_discapacidad.data,
            "fecha_ingreso": self.fecha_ingreso.data,
            "duracion_estadia": self.duracion_estadia.data,
            "consulado_visacion": self.consulado_visacion.data
        }
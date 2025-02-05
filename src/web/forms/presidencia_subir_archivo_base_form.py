from flask_wtf import FlaskForm
from wtforms import FileField, BooleanField, DateField, IntegerField, StringField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileAllowed
from src.web.forms.validators import file_size_limit

class PresidenciaArchivoBase(FlaskForm):
    archivo = FileField(
        "Subir archivo",
        validators=[
            FileAllowed(["pdf"], "Solo se permiten archivos .pdf"),
            DataRequired()],
        render_kw={"accept": ".pdf"}
    )

    def values(self):
        return {
            "archivo": self.archivo.data
        }
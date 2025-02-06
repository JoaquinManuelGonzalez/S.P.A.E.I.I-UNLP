from flask_wtf import FlaskForm
from wtforms import FileField, StringField, HiddenField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed
from src.web.forms.validators import file_size_limit

class PresidenciaArchivoBaseForm(FlaskForm):
    titulo = HiddenField()
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
from flask_wtf import FlaskForm 
from wtforms import FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class VisadoSeguroMedicoForm(FlaskForm):
    visado = FileField('Visado', validators=[DataRequired(), FileAllowed(["pdf"], "Solo se permiten archivos .pdf")])
    seguro_medico = FileField('Seguro Médico', validators=[DataRequired(), FileAllowed(["pdf"], "Solo se permiten archivos .pdf")])

    def values(self):
        return {
            'visado': self.visado.data,
            'seguro_medico': self.seguro_medico.data
        }
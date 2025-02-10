from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField)
from wtforms.validators import DataRequired, Length

class ProgramaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50)])
    habilitado = BooleanField('Habilitado')
    submit = SubmitField('Guardar')
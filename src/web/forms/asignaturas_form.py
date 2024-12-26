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

from src.core.models.asignatura import Asignatura

class AsignaturasForm(FlaskForm):
    asignatura_1 = SelectField('Seleccione la asignatura', choices=[], validators=[])
    asignatura_2 = SelectField('Seleccione la asignatura', choices=[], validators=[])
    asignatura_3 = SelectField('Seleccione la asignatura', choices=[], validators=[])
    asignatura_4 = SelectField('Seleccione la asignatura', choices=[], validators=[])
    asignatura_5 = SelectField('Seleccione la asignatura', choices=[], validators=[])
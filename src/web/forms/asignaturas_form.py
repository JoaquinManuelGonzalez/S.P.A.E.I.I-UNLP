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
    asignatura_0 = SelectField('Asignatura', choices=[], validators=[])
    asignatura_1 = SelectField('Asignatura', choices=[], validators=[])
    asignatura_2 = SelectField('Asignatura', choices=[], validators=[])
    asignatura_3 = SelectField('Asignatura', choices=[], validators=[])
    asignatura_4 = SelectField('Asignatura', choices=[], validators=[])
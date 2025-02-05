from wtforms import StringField, SelectField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from flask_wtf import FlaskForm
import re


class AsignaturaForm(FlaskForm):
    id = HiddenField()
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    facultad_id = SelectField('Facultad en la que se dicta', choices=[], validators=[DataRequired()])
    carga_horaria = IntegerField('Carga horaria (Horas totales)', validators=[DataRequired(), NumberRange(min=1, message="Debe ser un número mayor a 0")])
    

    def validate_nombre(self, field):
        from src.core.services import asignaturas as asignaturas_service
        facultad_id = self.facultad_id.data
        asignatura_repetida = asignaturas_service.get_asignatura_by_nombre_facultad(field.data, facultad_id)
        if asignatura_repetida and asignatura_repetida.id != self.id.data:
            raise ValidationError('Ya existe una asignatura con ese nombre en esta facultad.')
from wtforms import StringField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf import FlaskForm
import re


class CarreraForm(FlaskForm):
    id = HiddenField()
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    facultad_id = SelectField('Facultad de la que depende', choices=[], validators=[DataRequired()])
    tipo_carrera_id = SelectField('Tipo de carrera', choices=[], validators=[DataRequired()])
    

    def validate_nombre(self, field):
        from src.core.services import carreras as carreras_service
        facultad_id = self.facultad_id.data
        tipo_carrera_id = self.tipo_carrera_id.data
        carrera_repetida = carreras_service.get_carrera_by_nombre_facultad(field.data, tipo_carrera_id, facultad_id)
        if carrera_repetida and carrera_repetida.id != self.id.data:
            raise ValidationError('Esta carrera ya existe.')
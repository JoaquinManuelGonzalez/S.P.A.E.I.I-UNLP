from wtforms import StringField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf import FlaskForm
import re


class FacultadForm(FlaskForm):
    id = HiddenField()
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    acronimo = StringField('Acronimo', validators=[DataRequired(), Length(min=2, max=10)])

    def validate_nombre(self, field):
        """Valida que el nombre de la facultad no exista en la base de datos."""
        from src.core.services import facultades as facultades_service
        facultad = facultades_service.get_facultad_by_nombre(field.data)
        if facultad and facultad.id != self.id.data:
            raise ValidationError('Ya existe una facultad con este nombre.')

    def validate_acronimo(self, field):
        """Valida que el acrónimo de la facultad no exista en la base de datos."""
        from src.core.services import facultades as facultades_service
        facultad = facultades_service.get_facultad_by_acronimo(field.data)
        if facultad and facultad.id != self.id.data:
            raise ValidationError('Ya existe una facultad con este acrónimo.')
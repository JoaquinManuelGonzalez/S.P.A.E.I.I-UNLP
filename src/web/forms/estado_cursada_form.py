from flask_wtf import FlaskForm
from wtforms import (RadioField, IntegerField, SubmitField)
from wtforms.validators import NumberRange, ValidationError, Optional

class EstadoCursadaForm(FlaskForm):
    estado = RadioField(u'Estado de cursada', choices=[('Cursando', 'Cursando'), ('Cursada abandonada', 'Cursada abandonada'), ('Cursada completada', 'Cursada completada')])
    nota = IntegerField('Nota', validators=[NumberRange(min=0, max=10), Optional()])
    submit = SubmitField('Actualizar estado')

    def validate_nota(form, field):
        if (form.estado.data == 'Cursada completada' and (field.data is None or field.data == '')):
            raise ValidationError('Para cambiar el estado de la cursada a completada, debe indicar la nota final de la cursada.')
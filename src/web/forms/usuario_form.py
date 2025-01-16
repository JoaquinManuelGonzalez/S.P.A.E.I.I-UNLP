from wtforms import StringField, PasswordField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from src.core.services import usuario_service
from flask_wtf import FlaskForm
import re


class Usuario_Form(FlaskForm):
    id = HiddenField()
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=100)])
    id_rol = SelectField('Rol', choices=[], validators=[DataRequired()])
    id_usuario_editado = HiddenField('id_usuario_editado')
    

    def validate_email(form, field):
        id_usuario_editado = form.id_usuario_editado.data
        usuario_repetido = usuario_service.buscar_usuario_email(field.data)
        if usuario_repetido and usuario_repetido.id != id_usuario_editado:
            raise ValidationError('El email ya está registrado por otro usuario.')


    def validate_contraseña(form, field):
        password = field.data
        if (not re.search("[a-z]", password) or
            not re.search("[A-Z]", password) or
            not re.search("[0-9]", password) or
            not re.search("[!@#$%^&*(),.?\":{}|<>_]", password)):
            raise ValidationError(
                'La contraseña debe tener al menos una letra minúscula, una letra mayúscula, un número, '
                'un carácter especial y un mínimo de 8 caracteres.'
            )

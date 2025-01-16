from wtforms import PasswordField
from wtforms.validators import ValidationError
from flask_wtf import FlaskForm
import re


class Nueva_Contraseña_Form(FlaskForm):
    nueva_contraseña = PasswordField('Nueva Contraseña')
    confirmar_contraseña = PasswordField('Confirmar Nueva Contraseña')
                
    def validate_nueva_contraseña(form, field):
        password = field.data
        if password:
            if (not re.search("[a-z]", password) or
                not re.search("[A-Z]", password) or
                not re.search("[0-9]", password) or
                not re.search("[!@#$%^&*(),.?\":{}|<>_]", password)):
                raise ValidationError(
                    'La contraseña debe tener al menos una letra minúscula, una letra mayúscula, un número, '
                    'un carácter especial y un mínimo de 8 caracteres.'
                )
                
    def validate_confirmar_contraseña(form, field):
        if form.nueva_contraseña.data and field.data != form.nueva_contraseña.data:
            raise ValidationError('Las contraseñas no coinciden.')

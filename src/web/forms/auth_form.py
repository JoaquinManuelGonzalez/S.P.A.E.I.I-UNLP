from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class Auth_Form(FlaskForm):
    """
    Formulario para iniciar sesión.

    Args:
        FlaskForm (Form): Formulario de Flask.
    """
    email = StringField('Email', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesion')


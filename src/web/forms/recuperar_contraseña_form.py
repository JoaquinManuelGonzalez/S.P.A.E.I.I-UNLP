from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class RecuperarContraseñaForm(FlaskForm):
    """
    Formulario para la recuperación de contraseña.
    """
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Recuperar Contraseña')
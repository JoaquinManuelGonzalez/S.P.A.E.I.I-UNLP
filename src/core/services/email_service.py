from flask import current_app
from flask_mail import Mail, Message

mail = Mail()

def send_email(titulo, cuerpo, receptores, archivos=None):
    try:
        # Crear el mensaje
        msg = Message(titulo, recipients=receptores)
        msg.body = cuerpo

        # Adjuntar los archivos si se pasan como parámetro
        if archivos:
            for archivo in archivos:
                msg.attach(archivo.filename, archivo.content_type, archivo.read())

        # Enviar el correo
        with current_app.app_context():
            mail.send(msg)
    except Exception as e:
        print(f"Hubo un error al enviar el correo: {str(e)}")

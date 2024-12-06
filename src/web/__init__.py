from flask import Flask, render_template, jsonify
# from src.web.handlers import error
from src.core import database
from src.core.bcrypt import bcrypt
from src.core.config import config
from flask_wtf.csrf import CSRFProtect
from src.web.seeds import seed_countries, seed_generos, seed_estados_civiles, seeds_usuarios
from src.web.controllers.routes import registrar_rutas
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from flask_mail import Mail, Message


#session = Session()
def create_app(env="development", static_folder="../../static", template_folders=""):
    """
    Crea una instancia de la aplicación de Flask con la configuración dada.
    Args:
        env (str, optional): Defaults to "development".
        static_folder (str, optional): Defaults to "../../static".
        template_folders (str, optional): Defaults to "".
    Returns:
        Flask: Retorna la instancia de la aplicación de Flask.
    """
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    database.init_app(app)
    bcrypt.init_app(app)
    csrf = CSRFProtect(app)
    app = registrar_rutas(app)
    jwt = JWTManager(app)
    mail = Mail(app)
    
    #session.init_app(app)

    @app.route("/send_email")
    def send_email():
        try:
            # Crear el mensaje
            msg = Message("Prueba de correo desde Flask", recipients=["joaquinmgonzalez16@outlook.com"])
            msg.body = "Este es un correo de prueba desde Flask utilizando Gmail."

            # Enviar el correo
            mail.send(msg)
            return "Correo enviado con éxito"
        except Exception as e:
            return f"Hubo un error al enviar el correo: {str(e)}"

    @app.route("/")
    def home():
        """
        Función que renderiza el template layout.html
        Returns:
            render_template: Retorna el template layout.html
        """
        token = create_access_token(identity="usuario")
        print("Hola, esto es un JWT")
        print(type(token))
        return render_template("home.html")

    @app.cli.command(name="reset-db")
    def reset_db():
        """
        Comando para resetear la base de datos
        """
        database.reset()
   
    @app.cli.command(name="seeds-db")
    def usuarios_roles_seed():
        """
        Comando para crear los seeds de la base de datos
        """
        seeds_usuarios()
        seed_countries()
        seed_generos()
        seed_estados_civiles()

    return app
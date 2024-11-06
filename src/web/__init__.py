
from flask import Flask, render_template
# from src.web.handlers import error
from src.core import database
from src.core.config import config

db = database.db #TODAS LAS REFERENCIAS A LA BASE DE DATOS DEBEN LLAMAR A ÉSTE

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
    db.init_app(app)
    
    #app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
    #csrf = CSRFProtect(app)
    #session.init_app(app)
    #bcrypt.init_app(app)
    #storage.init_app(app)
    print(config["development"].SQLALCHEMY_DATABASE_URI)

    @app.route("/")
    def home():
        """
        Función que renderiza el template layout.html
        Returns:
            render_template: Retorna el template layout.html
        """
        return render_template("layout.html")
    
    #app.register_error_handler(404, error.error_not_found)
    #app.register_error_handler(403, error.sin_permisos)

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
        print("aca crearia los seeds")
    return app
from os import environ, getenv

class Config(object):
    """
    Clase de configuración base.

    Args:
        object (class): Clase base de Python.
    """
    TESTING = False
    SECRET_KEY= "tu_clave_secreta_aqui"
    SESSION_TYPE = "filesystem"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = environ.get("MAIL_USERNAME")


class ProductionConfig(Config):
    """
    Clase de configuración para producción.

    Args:
        Config (class): Clase de configuración base.
    """
    MINIO_SERVER = environ.get("MINIO_SERVER")
    MINIO_ACCESS_KEY = environ.get("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = environ.get("MINIO_SECRET_KEY")
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")
    MINIO_SECURE = True
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "pool_recycle": 60,
        "pool_pre_ping": True,
    }


class DevelopmentConfig(Config):
    """
    Clase de configuración para desarrollo.

    Args:
        Config (class): Clase de configuración base.
    """
    MINIO_SERVER = "minio:9000"
    MINIO_ACCESS_KEY = environ.get("MINIO_ACCESS_KEY")
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")
    MINIO_SECRET_KEY = environ.get("MINIO_SECRET_KEY")
    MINIO_SECURE = False
    DB_USER = "admin"
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_HOST = "db"
    DB_PORT = "3306"
    DB_NAME = "SPAEIIDatabase"
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )



class TestingConfig(Config):
    """
    Clase de configuración para pruebas.

    Args:
        Config (class): Clase de configuración base.
    """
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}

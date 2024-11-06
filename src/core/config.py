from os import environ

class Config(object):
    """
    Clase de configuración base.

    Args:
        object (class): Clase base de Python.
    """
    TESTING = False
    SECRET_KEY= "tu_clave_secreta_aqui"
    SESSION_TYPE = "filesystem"


class ProductionConfig(Config):
    """
    Clase de configuración para producción.

    Args:
        Config (class): Clase de configuración base.
    """
    MINIO_SERVER = environ.get("MINIO_SERVER")
    MINIO_ACCESS_KEY = environ.get("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = environ.get("MINIO_SECRET_KEY")
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
    MINIO_SERVER = "localhost:9000"
    MINIO_ACCESS_KEY = "nVXLhZDmsc3geR4RhWN8"
    MINIO_SECRET_KEY = "F1DLtTyznvp4h9QUm0QNK1rWM0074uQah1dv2I6x"
    MINIO_SECURE = False
    DB_USER = "admin"
    DB_PASSWORD = "admin"
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DB_NAME = "spaeii"
    SQLALCHEMY_DATABASE_URI = (
        f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
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

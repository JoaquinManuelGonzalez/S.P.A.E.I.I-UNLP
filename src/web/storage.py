from minio import Minio


class Storage:
    def __init__(self, app=None):
        self.client = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """ Initialize the storage client """

        minio_server = app.config.get("MINIO_SERVER")
        access_key = app.config.get("MINIO_ACCESS_KEY")
        secret_key = app.config.get("MINIO_SECRET_KEY")
        secure = app.config.get("MINIO_SECURE", False)


        # Initialize the client
        self._client = Minio(
            minio_server,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )
        # adjunta al cliente el contexto de la app
        app.storage = self

        return app

    @property
    def client(self):
        """Return the storage client"""
        return self._client

    @client.setter
    def client(self, value):
        self._client = value


storage = Storage()
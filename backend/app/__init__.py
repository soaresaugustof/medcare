from flask import Flask
from .config import Config
from backend.app.routes.userRoutes import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Carrega as configurações
    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

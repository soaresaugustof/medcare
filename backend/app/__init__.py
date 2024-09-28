from flask import Flask
from .config import Config
from .routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #Registrando rotas
    app.register_blueprint(main_bp)

    #Registrando outras extensões

    return app
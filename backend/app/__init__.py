from flask import Flask
from .config import Config  # Certifique-se de que Config está definido corretamente

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Carrega as configurações
    
    # Importa o módulo de rotas para registrar as rotas
    from routes import *  # Não deve causar erro de sintaxe

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

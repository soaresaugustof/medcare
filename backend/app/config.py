import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'o-paulo-ta-no-limite-das-faltas')
    
    #Exemplo de configuração do bd, será alterado para o mysql
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
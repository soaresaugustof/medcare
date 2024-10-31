import os
import mysql.connector

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'o-paulo-ta-no-limite-das-faltas')
    
    #Exemplo de configuração do bd, será alterado para o mysql
    SQLALCHEMY_DATABASE_URI        = os.getenv('DATABASE_URL', 'mysql://root:dbDev!6421@localhost/medcare')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def mydb = mysql.connector.connect(
    host        ="localhost",
    user        ="root",
    passwd      ="dbDev!6421",
    database    ="medcare",
    auth_plugin ='mysql_native_password'
)

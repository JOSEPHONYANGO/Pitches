# from logging import root
import os

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app=Flask(__name__)

# user="postgres"
# password="root"
# host="44.200.116.238"
# database="pitches"

# uri=f"postgresql://{user}:{password}@{host}/{database}"
# app.config["SQLALCHEMY_DATABASE_URI"]=uri
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


class Config:
    debug = True
    SECRET_KEY = "joseph"
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:root@localhost/new'
    SQLALCHEMY_DATABASE_URI = "postgres://hefpwasarrepud:862bfe61f42443b398c27ddf2cf00a558c8161b619f7e3767198cd368a0705d8@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d3vqpr7p2rrdma"

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch It Up!'
    SENDER_EMAIL = 'otienojoe14@gmail.com'

    @staticmethod
    def init_app(app):
        pass
    
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:root@localhost/new'
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
     uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI=uri
   
class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:root@localhost/new'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:root@localhost/new'
    
    
    DEBUG = False
    # ENV = 'development'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}




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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:root@localhost/new'

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
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL').replace ('://', 'ql://', 1) 
   
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




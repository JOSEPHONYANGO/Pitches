from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import config_options

# from config import Config
app = Flask(__name__)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
mail = Mail(app)
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'


def create_app(config_name):
    app.config.from_object(config_options[config_name])

    # print (app.config)
    # print(config_options[config_name])
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    # create_db()



    # return app
    app.run(port=3002,host='0.0.0.0')


def create_db():
    db.create_all()
    print ("Tables Created")



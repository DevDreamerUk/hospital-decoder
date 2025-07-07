from flask import Flask
from flask_login import LoginManager

from . import routes
from .config import Config
from .extensions import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    from . import config
    from .models import post
    app.register_blueprint(routes.bp)

    return app

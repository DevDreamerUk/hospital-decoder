from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import routes
from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from . import config
    from .models import post
    app.register_blueprint(routes.bp)

    return app

from flask import Flask
from flask_login import LoginManager

from . import routes
from .config import Config
from .extensions import db
from .models.user import User
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from . import config
    from .models import post
    app.register_blueprint(routes.bp)
    print(app.url_map)

    return app
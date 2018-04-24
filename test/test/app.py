from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from .config import configs
from .models import User, Course, db

def register_extension(a):
    db.init_app(a)
    Migrate(a, db)
    l = LoginManager()
    l.init_app(a)

    @l.user_loader
    def user_loader(id):
        return User.query.get(id)

    l.login_view = 'front.login'


def register_blueprint(app):
    from .handler import front, admin, course
    for i in (front, admin, course):
        app.register_blueprint(i)

def create_app(c):
    app = Flask(__name__)
    app.config.from_object(configs.get(c))
    register_extension(app)
    register_blueprint(app)
    return app

from flask import Flask, render_template
from flask_migrate import Migrate
from .models import db, Course, User
from .config import configs

def register_blueprints(a):
    from .handlers import admin, course, front
    a.register_blueprint(admin)
    a.register_blueprint(course)
    a.register_blueprint(front)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    Migrate(app, db)

    return app

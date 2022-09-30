# application/__init__.py
import config
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# 
from application.base import app
from application.database import db
from application.trace import *


login_manager = LoginManager()

def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(app):

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Register blueprints
        from .user_api import user_api_blueprint
        app.register_blueprint(user_api_blueprint)
        return app


app = create_app(app)
configure_database(app)
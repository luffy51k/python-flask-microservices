# application/__init__.py
import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from application.base import app
from application.database import db

from application.trace import *


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(app):

    db.init_app(app)

    with app.app_context():
        from .product_api import product_api_blueprint
        app.register_blueprint(product_api_blueprint)
        return app

app = create_app(app)
configure_database(app)
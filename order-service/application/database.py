from flask_sqlalchemy import SQLAlchemy

from application.base import app

db = SQLAlchemy(app)
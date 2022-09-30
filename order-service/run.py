# run.py
from application import create_app, db
from flask_migrate import Migrate
from application import models

from application import app

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

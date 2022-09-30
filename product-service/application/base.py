import os
from flask import Flask


app = Flask(__name__)

environment_configuration = os.environ['CONFIGURATION_SETUP']
app.config.from_object(environment_configuration)
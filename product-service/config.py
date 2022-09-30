# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OTLP_ENDPOINT = 'http://10.100.120.188:4318/v1/traces'
    

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cloudacademy:pfm_2020@localhost:3306/product_dev'


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cloudacademy:pfm_2020@product-db:3306/product'

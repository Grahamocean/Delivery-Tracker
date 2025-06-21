import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-fallback-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get('FLASK_DEBUG', False)
    ENV = os.environ.get('FLASK_ENV', 'production')

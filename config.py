import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    UPLOAD_DIR = os.getenv('UPLOAD_DIR') or 'uploads'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = (os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', '').lower() == 'true') or False
    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.getenv('MAIL_PORT', 25))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') or 'my@domain.com'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') or 'password'
    MAIL_USE_TLS = (os.getenv('MAIL_USE_TLS', '').lower() == 'true') or False
    MAIL_USE_SSL = (os.getenv('MAIL_USE_SSL', '').lower() == 'true') or True

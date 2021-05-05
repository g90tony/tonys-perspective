import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    QUOTES_URL = os.environ.get('QUOTES_URL')
    PIXELBAY_API_URL = os.environ.get('PIXELBAY_API_URL')
    PIXELBAY_API_KEY = os.environ.get('PIXELBAY_API_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://caleb:admin@localhost/tonys_perspective'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    SIMPLEMDE_JS_IIFE =True
    SIMPLEMDE_USE_CDN = True
    
    @staticmethod
    def init_app(app):
        pass
    
class DevConfig(Config):
    
    DEBUG = True
    
class ProdConfig(Config):
    pass
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
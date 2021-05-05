import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.environ.get('SECRET_KEY')
    
    QUOTES_URL = os.environ.get('QUOTES_URL')
    PIXELBAY_API_URL = os.environ.get('PIXELBAY_API_URL')
    PIXELBAY_API_KEY = os.environ.get('PIXELBAY_API_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://caleb:admin@localhost/tonys_perspective'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    
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
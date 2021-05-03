import os

class Config:
    
    QUOTES_URL = os.environ.get('QUOTES_URL')
    PEXELS_API_KEY = os.environ.get('PEXELS_API_KEY')
    PEXELS_URL = os.environ.get('PEXELS_URL')
    
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
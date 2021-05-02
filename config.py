import os

class Config:
    
    QUOTES_URL = os.environ.get('QUOTES_URL')
    PEXELS_API_KEY = os.environ.get('PEXELS_API_KEY')
    PEXELS_URL = os.environ.get('PEXELS_URL')
    
    @staticmethod
    def init_app(app):
        pass
    
class DevConfig(Config):
    pass
    
class Prod(Config):
    pass
    
config_options {
    'development':DevConfig,
    'production': ProdConfig
}
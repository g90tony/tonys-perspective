import os

class Config:
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
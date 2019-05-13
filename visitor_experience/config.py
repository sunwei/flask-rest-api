import os


class Config:
    # Flask-Restplus settings
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False


class DevelopmentConfig(Config):
    # Flask settings
    SERVER_NAME = 'localhost:1234'
    DEBUG = True  # Do not use debug mode in production


class TestingConfig(Config):
    TESTING = True


class StageConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'string'


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'string'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'stage': StageConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

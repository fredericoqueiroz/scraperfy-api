class BaseConfig():
    API_PREFIX = '/scraperfy'
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy_dev'
    SQLALCHEMY_ECHO = True

class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy_test?charset=utf8mb4'
    SQLALCHEMY_ECHO = True

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy_prod?charset=utf8mb4'


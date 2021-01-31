import os
from typing import List, Type

#basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    CONFIG_NAME = 'base'
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = 'dev'
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "And I knew exactly what to do. But in a much more real sense, I had no idea what to do."
    )
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy_dev?charset=utf8mb4'
    SQLALCHEMY_ECHO = True

class TestingConfig(BaseConfig):
    CONFIG_NAME = 'test'
    SECRET_KEY = os.getenv(
        "TEST_SECRET_KEY", "Make friends first, make sales second, make love third. In no particular order."
    )
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy_test?charset=utf8mb4'
    SQLALCHEMY_ECHO = True

class ProductionConfig(BaseConfig):
    CONFIG_NAME = 'prod'
    SECRET_KEY = os.getenv(
        "PROD_SECRET_KEY", "I love inside jokes. I hope to be a part of one someday."
    )
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy_prod?charset=utf8mb4'
    SQLALCHEMY_ECHO = False

EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
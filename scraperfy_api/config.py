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
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy-dev?charset=utf8mb4'

class TestingConfig(BaseConfig):
    CONFIG_NAME = 'test'
    SECRET_KEY = os.getenv(
        "TEST_SECRET_KEY", "Make friends first, make sales second, make love third. In no particular order."
    )
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy-test?charset=utf8mb4'

class ProductionConfig(BaseConfig):
    CONFIG_NAME = 'prod'
    SECRET_KEY = os.getenv(
        "PROD_SECRET_KEY", "I love inside jokes. I hope to be a part of one someday."
    )
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fred:fred@localhost/scraperfy-prod?charset=utf8mb4'

EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
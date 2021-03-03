from flask import Flask

from financial_data.extensions import configuration


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    app.config.load_extensions()
    return app

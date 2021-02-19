import logging
import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import config
from scraperfy_api import scraperfy_api

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


db = SQLAlchemy()


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')

    app = Flask(__name__)
    app.config.from_object('config')
    scraperfy_api.init_app(app)
    
    # initialize SQLAlchemy
    db.init_app(app)

    @app.route('/health')
    def health():
        return jsonify('healthy')
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()

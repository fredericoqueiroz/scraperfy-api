from flask import Blueprint
from flask_restx import Api

from .routes import register_routes

URL_PREFIX = '/api/v1/scraperfy/'

bp = Blueprint('scraperfy_api', __name__, url_prefix=URL_PREFIX)

api = Api(bp, version='1.0', title='Scraperfy API',
        description='A RESTful API that serves data from the Scraperfy Package'
    )

register_routes(api)

def init_app(app):
    app.register_blueprint(bp)

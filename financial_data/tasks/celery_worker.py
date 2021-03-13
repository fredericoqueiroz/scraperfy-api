from financial_data.app import create_app

from . import celery, init_celery

flask_app = create_app()
init_celery(celery, flask_app)

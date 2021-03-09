from financial_data.app import minimal_app

from . import celery, init_celery

app = minimal_app()
init_celery(celery, app)

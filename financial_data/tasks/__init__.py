from celery import Celery


def make_celery(app_name=__name__):
    celery = Celery(app_name)
    return celery

celery = make_celery()


def init_celery(celery, app):
    celery.conf.timezone = 'America/Sao_Paulo'
    celery.conf.result_backend = app.config['RESULT_BACKEND']
    celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

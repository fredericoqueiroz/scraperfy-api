from celery import Celery


def make_celery(app_name=__name__):
    celery = Celery(
        app_name,
        backend='db+mysql+pymysql://fred:fred@localhost/tasks?charset=utf8mb4',
        broker='amqp://localhost//'
    )
    return celery

celery = make_celery()


def init_celery(celery, app):
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

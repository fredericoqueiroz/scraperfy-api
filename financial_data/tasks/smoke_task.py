from . import celery


@celery.task(name='smoke_task')
def smoke_task():
    print("Running smoke test...")

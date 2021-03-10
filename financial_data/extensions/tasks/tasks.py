from . import celery

from.current_price import smoke_task, get_current_price_task

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, get_current_price_task, name='current price')
    sender.add_periodic_task(60.0, smoke_task, name='smoke task')


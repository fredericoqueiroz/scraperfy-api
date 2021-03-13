from . import celery
from .current_price import get_current_price_task
from .smoke_task import smoke_task

assets = ['IBOV', 'IFIX', 'ITSA4']

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, get_current_price_task.s('ITSA4'), name='current price')
    sender.add_periodic_task(30.0, smoke_task, name='smoke task')


from . import celery
from .current_price import get_current_price_task
from .smoke_task import smoke_task
from .theoretical_portifolio import get_theoretical_portifolio_task


""" 
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, smoke_task, name='smoke task')
"""

@celery.on_after_configure.connect
def setup_current_price_tasks(sender, **kwargs):
    assets = ['IBOV', 'BBAS3', 'RBRP11', 'ITSA4', 'RAIL3']
    for asset in assets:
        sender.add_periodic_task(60.0, get_current_price_task.s(asset), name=f'current {asset} price')

@celery.on_after_configure.connect
def setup_theoretical_portifolio_tasks(sender, **kwargs):
    indexes = ['IBOV', 'IFIX']
    for index in indexes:
        sender.add_periodic_task(120.0, get_theoretical_portifolio_task.s(index), name=f'{index} daily theoretical portifolio')
       
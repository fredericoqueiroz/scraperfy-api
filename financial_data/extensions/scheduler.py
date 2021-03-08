from flask_apscheduler import APScheduler
from financial_data.blueprint.tasks.current_price import smoke_task, get_current_price_task

scheduler = APScheduler()
scheduler.api_enabled = True

#scheduler.add_job(id='Current Price Task', func=get_current_price_task('IBOV'), trigger='interval', seconds=60)
scheduler.add_job(id='Current Price Task', func=smoke_task, trigger='interval', seconds=60)

def init_app(app):
    scheduler.init_app(app)
    scheduler.start()

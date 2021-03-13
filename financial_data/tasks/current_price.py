from financial_data.blueprint.scraperfy_api.asset_scraper.current_price.model import \
    CurrentPrice
from financial_data.extensions.database import db
from financial_data.extensions.webdriver import init_chrome_driver
from scraperfy.intraday_scraper import current_price as cp

from . import celery
from .celery_worker import celery, flask_app


@celery.task(name='current_price_task')
def get_current_price_task(asset):

    driver = init_chrome_driver()

    price = cp.CurrentPrice(driver, asset)

    new_cp = CurrentPrice(asset_symbol=price.asset_symbol.upper(),
                        asset_price=price.asset_price,
                        asset_oscilation=price.asset_oscilation)

    with flask_app.app_context():
        db.session.add(new_cp)
        db.session.commit()

    #return new_cp

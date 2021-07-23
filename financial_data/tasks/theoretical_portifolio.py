from financial_data.blueprint.scraperfy_api.index_scraper.theoretical_portifolio.model import \
    TheoreticalPortifolio
from financial_data.extensions.database import db
from financial_data.extensions.webdriver import init_firefox_driver
from scraperfy.index_scraper import theoretical_portifolio as tp

from . import celery
from .celery_worker import celery, flask_app


@celery.task(name='theoretical_portifolio_task')
def get_theoretical_portifolio_task(index_symbol):

    driver = init_firefox_driver()

    portifolio = tp.TheoreticalDailyPortifolio(driver, index_symbol)

    assets = portifolio.get_data_frame()

    for idx, asset in assets.iterrows():

        new_asset = TheoreticalPortifolio(
            index_symbol=index_symbol,
            asset_symbol=idx,
            asset_name=asset['nome'],
            asset_type=asset['tipo'],
            theoretical_quantity=asset['quantidadeTeorica'],
            percentage_share=asset['participacao'],
            portifolio_date=portifolio.get_portifolio_date()
        )
    
        with flask_app.app_context():
            db.session.add(new_asset)
            db.session.commit()

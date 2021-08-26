from financial_data.blueprint.scraperfy_api.asset_scraper.company_indicators.valuation_indicators.model import \
    ValuationIndicators
from financial_data.extensions.database import db
from financial_data.extensions.webdriver import init_firefox_driver
from scraperfy.company_indicators import company_indicators as ci

from . import celery
from .celery_worker import celery, flask_app

import json

@celery.task(name='company_indicators_task')
def get_company_indicators_task(asset):

    driver = init_firefox_driver()

    company_indicators = ci.CompanyIndicators(driver, asset)

    valuation = json.loads(company_indicators.get_valuation_indicators())

    new_ci = ValuationIndicators(asset_symbol=company_indicators.get_asset(),
                                 search_date=company_indicators.get_search_date(),
                                 dividend_yield=valuation['DividendYield']['valor'],
                                 price_earnings=valuation['PrecoLucro']['valor'],
                                 peg_ratio=valuation['PegRatio']['valor'],
                                 price_book_value=valuation['PrecoValorPatrimonial']['valor'],
                                 ev_ebitda=valuation['EvEbitda']['valor'],
                                 ev_ebit=valuation['EvEbit']['valor'],
                                 price_ebitda=valuation['PrecoEbitda']['valor'],
                                 price_ebit=valuation['PrecoEbit']['valor'],
                                 book_value_share=valuation['ValorPatrimonialAcao']['valor'],
                                 price_asset=valuation['PrecoAtivo']['valor'],
                                 earnings_share=valuation['LucroAcao']['valor'],
                                 prices_sales_ratio=valuation['PrecoReceitaLiquida']['valor'],
                                 prices_working_capital=valuation['PrecoCapitalGiro']['valor'],
                                 price_net_current_assets=valuation['PrecoAtivoCirculanteLiquido']['valor']
                                 )
    
    with flask_app.app_context():
        db.session.add(new_ci)
        db.session.commit()

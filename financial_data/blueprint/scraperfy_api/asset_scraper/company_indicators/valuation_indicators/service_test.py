import datetime
from typing import List

from financial_data.tests.fixtures import app, db
from flask_sqlalchemy import SQLAlchemy

from .interface import ValuationIndicatorsInterface
from .model import ValuationIndicators
from .service import ValuationIndicatorsService


def test_get_all(db: SQLAlchemy):

    asset_1: ValuationIndicators = ValuationIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828', dividend_yield=6.48, price_earnings=22.22, 
                                                       peg_ratio=0.56, price_book_value=4.00, ev_ebitda=12.57, ev_ebit=14.73,
                                                       price_ebitda=13.77, price_ebit=16.15, book_value_share=3.97, price_asset=2.11,
                                                       earnings_share=0.72, prices_sales_ratio=9.92, prices_working_capital=13.20, price_net_current_assets=-3.32)
    
    asset_2: ValuationIndicators = ValuationIndicators(asset_id=2, asset_symbol='PETR4', search_date='2021-08-09T11:23:52.277828', dividend_yield=4.28, price_earnings=22.22, 
                                                       peg_ratio=0.56, price_book_value=4.00, ev_ebitda=12.57, ev_ebit=14.73,
                                                       price_ebitda=13.77, price_ebit=16.15, book_value_share=3.97, price_asset=2.11,
                                                       earnings_share=0.72, prices_sales_ratio=9.92, prices_working_capital=13.20, price_net_current_assets=-3.32)
    
    db.session.add(asset_1)
    db.session.add(asset_2)
    db.session.commit()

    results: List[ValuationIndicators] = ValuationIndicatorsService.get_all()

    assert len(results) == 2
    assert asset_1 in results and asset_2 in results

def test_update(db: SQLAlchemy):

    asset: ValuationIndicators = ValuationIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828', dividend_yield=6.48, price_earnings=22.22, 
                                                     peg_ratio=0.56, price_book_value=4.00, ev_ebitda=12.57, ev_ebit=14.73,
                                                     price_ebitda=13.77, price_ebit=16.15, book_value_share=3.97, price_asset=2.11,
                                                     earnings_share=0.72, prices_sales_ratio=9.92, prices_working_capital=13.20, price_net_current_assets=-3.32)
    
    db.session.add(asset)
    db.session.commit()

    updates: ValuationIndicatorsInterface = dict(price_earnings=9999, dividend_yield=99.99)

    ValuationIndicatorsService.update(asset, updates)

    results: ValuationIndicators = ValuationIndicators.query.get((asset.asset_id, asset.asset_symbol))
    assert results.price_earnings == 9999
    assert results.dividend_yield == 99.99

def test_delete_by_id(db: SQLAlchemy):

    asset_1: ValuationIndicators = ValuationIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828', dividend_yield=6.48, price_earnings=22.22, 
                                                       peg_ratio=0.56, price_book_value=4.00, ev_ebitda=12.57, ev_ebit=14.73,
                                                       price_ebitda=13.77, price_ebit=16.15, book_value_share=3.97, price_asset=2.11,
                                                       earnings_share=0.72, prices_sales_ratio=9.92, prices_working_capital=13.20, price_net_current_assets=-3.32)
    
    asset_2: ValuationIndicators = ValuationIndicators(asset_id=2, asset_symbol='PETR4', search_date='2021-08-09T11:23:52.277828', dividend_yield=4.28, price_earnings=22.22, 
                                                       peg_ratio=0.56, price_book_value=4.00, ev_ebitda=12.57, ev_ebit=14.73,
                                                       price_ebitda=13.77, price_ebit=16.15, book_value_share=3.97, price_asset=2.11,
                                                       earnings_share=0.72, prices_sales_ratio=9.92, prices_working_capital=13.20, price_net_current_assets=-3.32)
    
    db.session.add(asset_1)
    db.session.add(asset_2)
    db.session.commit()

    ValuationIndicatorsService.delete_by_symbol('B3SA3')
    db.session.commit()

    results: List[ValuationIndicators] = ValuationIndicators.query.all()

    assert len(results) == 1
    assert asset_1 not in results and asset_2 in results

def test_create(db: SQLAlchemy):

    asset_1: ValuationIndicatorsInterface = dict(asset_symbol='B3SA3', search_date=datetime.datetime(2021,8,7,11,23,52), dividend_yield=6.48, price_earnings=22.22, 
                                                       peg_ratio=0.56, price_book_value=4.00, ev_ebitda=12.57, ev_ebit=14.73,
                                                       price_ebitda=13.77, price_ebit=16.15, book_value_share=3.97, price_asset=2.11,
                                                       earnings_share=0.72, prices_sales_ratio=9.92, prices_working_capital=13.20, price_net_current_assets=-3.32)
    
    ValuationIndicatorsService.create(asset_1)
    results: List[ValuationIndicators] = ValuationIndicators.query.all()

    assert len(results) == 1

    for k in asset_1.keys():
        assert getattr(results[0], k) == asset_1[k]


import datetime
from typing import List

from financial_data.tests.fixtures import app, db
from flask_sqlalchemy import SQLAlchemy

from .interface import DebtIndicatorsInterface
from .model import DebtIndicators
from .service import DebtIndicatorsService


def test_get_all(db: SQLAlchemy):

    asset_1: DebtIndicators = DebtIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828',
                                             debt_net_worth=-1.86, debt_ebitda=-7.33, debt_ebit=-32.71,
                                             net_worth_assets=0.29, liabilities_assets=0.71, current_liquidity=2.25)

    asset_2: DebtIndicators = DebtIndicators(asset_id=2, asset_symbol='ASSET2', search_date='2021-08-07T11:23:52.277828',
                                             debt_net_worth=-9.99, debt_ebitda=6, debt_ebit=-99.99,
                                             net_worth_assets=0.00, liabilities_assets=0.59, current_liquidity=4.20)

    db.session.add(asset_1)
    db.session.add(asset_2)
    db.session.commit()

    results: List[DebtIndicators] = DebtIndicatorsService.get_all()

    assert len(results) == 2
    assert asset_1 in results and asset_2 in results

def test_update(db: SQLAlchemy):

    asset: DebtIndicators = DebtIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828',
                                           debt_net_worth=-1.86, debt_ebitda=-7.33, debt_ebit=-32.71,
                                           net_worth_assets=0.29, liabilities_assets=0.71, current_liquidity=2.25)

    db.session.add(asset)
    db.session.commit()

    updates: DebtIndicatorsInterface = dict(debt_net_worth=9999, debt_ebit=-12.99)

    DebtIndicatorsService.update(asset, updates)

    results: DebtIndicators = DebtIndicators.query.get((asset.asset_id, asset.asset_symbol))
    assert results.debt_net_worth == 9999
    assert results.debt_ebit == -12.99

def test_delete_by_id(db: SQLAlchemy):

    asset_1: DebtIndicators = DebtIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828',
                                             debt_net_worth=-1.86, debt_ebitda=-7.33, debt_ebit=-32.71,
                                             net_worth_assets=0.29, liabilities_assets=0.71, current_liquidity=2.25)

    asset_2: DebtIndicators = DebtIndicators(asset_id=2, asset_symbol='ASSET2', search_date='2021-08-07T11:23:52.277828',
                                             debt_net_worth=-9.99, debt_ebitda=6, debt_ebit=-99.99,
                                             net_worth_assets=0.00, liabilities_assets=0.59, current_liquidity=4.20)

    db.session.add(asset_1)
    db.session.add(asset_2)
    db.session.commit()

    DebtIndicatorsService.delete_by_symbol('B3SA3')
    db.session.commit()

    results: List[DebtIndicators] = DebtIndicators.query.all()

    assert len(results) == 1
    assert asset_1 not in results and asset_2 in results

def test_create(db: SQLAlchemy):

    asset_1: DebtIndicatorsInterface = dict(asset_symbol='B3SA3', search_date=datetime.datetime(2021,8,7,11,23,52),
                                             debt_net_worth=-1.86, debt_ebitda=-7.33, debt_ebit=-32.71,
                                             net_worth_assets=0.29, liabilities_assets=0.71, current_liquidity=2.25)

    DebtIndicatorsService.create(asset_1)
    results: List[DebtIndicators] = DebtIndicators.query.all()

    assert len(results) == 1

    for k in asset_1.keys():
        assert getattr(results[0], k) == asset_1[k]


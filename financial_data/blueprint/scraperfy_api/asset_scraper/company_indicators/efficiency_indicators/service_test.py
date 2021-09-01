import datetime
from typing import List

from financial_data.tests.fixtures import app, db
from flask_sqlalchemy import SQLAlchemy

from .interface import EfficiencyIndicatorsInterface
from .model import EfficiencyIndicators
from .service import EfficiencyIndicatorsService


def test_get_all(db: SQLAlchemy):

    asset_1: EfficiencyIndicators = EfficiencyIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828',
                                                         gross_margin = 10.16, ebitda_margin = 10.71, ebit_margin = 2.40, net_margin = 9.74)

    asset_2: EfficiencyIndicators = EfficiencyIndicators(asset_id=2, asset_symbol='ASSET2', search_date='2021-08-07T11:23:52.277828',
                                                         gross_margin = 99.99, ebitda_margin = 88.88, ebit_margin = 77.77, net_margin = 66.66)

    db.session.add(asset_1)
    db.session.add(asset_2)
    db.session.commit()

    results: List[EfficiencyIndicators] = EfficiencyIndicatorsService.get_all()

    assert len(results) == 2
    assert asset_1 in results and asset_2 in results

def test_update(db: SQLAlchemy):

    asset: EfficiencyIndicators = EfficiencyIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828',
                                                       gross_margin = 10.16, ebitda_margin = 10.71, ebit_margin = 2.40, net_margin = 9.74)

    db.session.add(asset)
    db.session.commit()

    updates: EfficiencyIndicatorsInterface = dict(gross_margin=9999, ebitda_margin=-88.88)

    EfficiencyIndicatorsService.update(asset, updates)

    results: EfficiencyIndicators = EfficiencyIndicators.query.get((asset.asset_id, asset.asset_symbol))
    assert results.gross_margin == 9999
    assert results.ebitda_margin == -88.88

def test_delete_by_id(db: SQLAlchemy):

    asset_1: EfficiencyIndicators = EfficiencyIndicators(asset_id=1, asset_symbol='B3SA3', search_date='2021-08-07T11:23:52.277828',
                                                         gross_margin = 10.16, ebitda_margin = 10.71, ebit_margin = 2.40, net_margin = 9.74)

    asset_2: EfficiencyIndicators = EfficiencyIndicators(asset_id=2, asset_symbol='ASSET2', search_date='2021-08-07T11:23:52.277828',
                                                         gross_margin = 99.99, ebitda_margin = 88.88, ebit_margin = 77.77, net_margin = 66.66)

    db.session.add(asset_1)
    db.session.add(asset_2)
    db.session.commit()

    EfficiencyIndicatorsService.delete_by_symbol('B3SA3')
    db.session.commit()

    results: List[EfficiencyIndicators] = EfficiencyIndicators.query.all()

    assert len(results) == 1
    assert asset_1 not in results and asset_2 in results

def test_create(db: SQLAlchemy):

    asset_1: EfficiencyIndicatorsInterface = dict(asset_id=1, asset_symbol='B3SA3', search_date=datetime.datetime(2021,8,7,11,23,52),
                                                         gross_margin = 10.16, ebitda_margin = 10.71, ebit_margin = 2.40, net_margin = 9.74)
    
    EfficiencyIndicatorsService.create(asset_1)
    results: List[EfficiencyIndicators] = EfficiencyIndicators.query.all()

    assert len(results) == 1

    for k in asset_1.keys():
        assert getattr(results[0], k) == asset_1[k]


from typing import List

from flask_sqlalchemy import SQLAlchemy
from financial_data.tests.fixtures import app, db

from .interface import CurrentPriceInterface
from .model import CurrentPrice
from .service import CurrentPriceService


def test_get_all(db: SQLAlchemy):

    ibov: CurrentPrice = CurrentPrice(asset_id=1, asset_symbol='IBOV', asset_price=118430.53, asset_oscilation=-0.64)
    ifix: CurrentPrice = CurrentPrice(asset_id=2, asset_symbol='IFIX', asset_price=2893.99, asset_oscilation=+0.11)

    db.session.add(ibov)
    db.session.add(ifix)
    db.session.commit()

    results: List[CurrentPrice] = CurrentPriceService.get_all()

    assert len(results) == 2
    assert ibov in results and ifix in results

def test_update(db: SQLAlchemy):

    asset : CurrentPrice = CurrentPrice(asset_id=1, asset_symbol='RBRP11', asset_price=96.00, asset_oscilation=+0.18)

    db.session.add(asset)
    db.session.commit()

    updates: CurrentPriceInterface = dict(asset_price=96.99)

    CurrentPriceService.update(asset, updates)

    results: CurrentPrice = CurrentPrice.query.get((asset.asset_id, asset.asset_symbol))
    assert results.asset_price == 96.99

def test_delete_by_id(db: SQLAlchemy):

    ibov: CurrentPrice = CurrentPrice(asset_id=1, asset_symbol='IBOV', asset_price=121040.73, asset_oscilation=-0.45)
    ifix: CurrentPrice = CurrentPrice(asset_id=2, asset_symbol='IFIX', asset_price=2842.01, asset_oscilation=+0.14)

    db.session.add(ibov)
    db.session.add(ifix)
    db.session.commit()

    CurrentPriceService.delete_by_symbol('IBOV')
    db.session.commit()

    results: List[CurrentPrice] = CurrentPrice.query.all()

    assert len(results) == 1
    assert ibov not in results and ifix in results

def test_create(db: SQLAlchemy):

    ifix: CurrentPriceInterface = dict(asset_symbol='IFIX', asset_price=3042.01, asset_oscilation=+3.22)

    CurrentPriceService.create(ifix)
    results: List[CurrentPrice] = CurrentPrice.query.all()

    assert len(results) == 1

    for k in ifix.keys():
        assert getattr(results[0], k) == ifix[k]


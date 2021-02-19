from typing import List

from flask_sqlalchemy import SQLAlchemy
from scraperfy_api.test.fixtures import app, db

from .interface import CurrentPriceInterface
from .model import CurrentPrice
from .service import CurrentPriceService

def test_get_all(db: SQLAlchemy):
    ibov: CurrentPrice = CurrentPrice(asset_id=1, asset_symbol='IBOV', asset_price=118430.53, asset_oscilation=-0.64)
    ifix: CurrentPrice = CurrentPrice(asset_id=2, asset_symbol='IFIX', asset_price=2893.97, asset_oscilation=+0.11)

    db.session.add(ibov)
    db.session.add(ifix)
    db.session.commit()

    results: List[CurrentPrice] = CurrentPriceService.get_all()

    assert len(results) == 2
    assert ibov in results and ifix in results


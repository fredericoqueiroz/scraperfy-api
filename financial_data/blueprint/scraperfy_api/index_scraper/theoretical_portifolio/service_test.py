from datetime import date
from typing import List

from financial_data.tests.fixtures import app, db
from flask_sqlalchemy import SQLAlchemy

from .interface import TheoreticalPortifolioInterface
from .model import TheoreticalPortifolio
from .service import TheoreticalPortifolioService


def test_get_all(db: SQLAlchemy):

    ibov: TheoreticalPortifolio = TheoreticalPortifolio(
        index_symbol = 'IBOV',
        portifolio_date = date(2021,7,22),
        asset_symbol = 'PETR4',
        asset_name = 'PETROBRAS',
        asset_type = 'PN N2',
        theoretical_quantity = '4.566.457.037',
        percentage_share = '5,133'
    )

    ifix: TheoreticalPortifolio = TheoreticalPortifolio(
        index_symbol = 'IFIX',
        portifolio_date = date(2021,7,22),
        asset_symbol = 'HGRU11',
        asset_name = 'FII CSHG URB',
        asset_type = 'CI',
        theoretical_quantity = '18.406.458',
        percentage_share = '2,528'
    )
    
    db.session.add(ibov)
    db.session.add(ifix)
    db.session.commit()

    result: List[TheoreticalPortifolio] = TheoreticalPortifolioService.get_all()

    assert len(result) == 2
    assert ibov in result and ifix in result

def test_update(db: SQLAlchemy):

    tp: TheoreticalPortifolio = TheoreticalPortifolio(
        index_symbol = 'IFIX',
        portifolio_date = date(2021,7,22),
        asset_symbol = 'HGRU11',
        asset_name = 'FII CSHG URB',
        asset_type = 'CI',
        theoretical_quantity = '18.406.458',
        percentage_share = '2,528'
    )

    db.session.add(tp)
    db.session.commit()

    updates: TheoreticalPortifolioInterface = dict(percentage_share = '4,842')

    TheoreticalPortifolioService.update(tp, updates)

    result: TheoreticalPortifolio = TheoreticalPortifolio.query.get((tp.index_symbol, tp.portifolio_date, tp.asset_symbol))
    assert result.percentage_share == '4,842'

def test_delete_by_index_and_asset(db: SQLAlchemy):

    ibov: TheoreticalPortifolio = TheoreticalPortifolio(
        index_symbol = 'IBOV',
        portifolio_date = date(2021,7,22),
        asset_symbol = 'PETR4',
        asset_name = 'PETROBRAS',
        asset_type = 'PN N2',
        theoretical_quantity = '4.566.457.037',
        percentage_share = '5,133'
    )

    ifix: TheoreticalPortifolio = TheoreticalPortifolio(
        index_symbol = 'IFIX',
        portifolio_date = date(2021,7,22),
        asset_symbol = 'HGRU11',
        asset_name = 'FII CSHG URB',
        asset_type = 'CI',
        theoretical_quantity = '18.406.458',
        percentage_share = '2,528'
    )

    db.session.add(ibov)
    db.session.add(ifix)
    db.session.commit()

    TheoreticalPortifolioService.delete_by_index_and_asset('IBOV', 'PETR4')
    db.session.commit()

    result: List[TheoreticalPortifolio] = TheoreticalPortifolio.query.all()

    assert len(result) == 1
    assert ibov not in result and ifix in result


def test_create(db: SQLAlchemy):

    ifix: TheoreticalPortifolio = dict(
        index_symbol = 'IFIX',
        portifolio_date = date(2021, 1, 21),
        asset_symbol = 'HGRU11',
        asset_name = 'FII CSHG URB',
        asset_type = 'CI',
        theoretical_quantity = '18.406.458',
        percentage_share = '2,528'
    )

    TheoreticalPortifolioService.create(ifix)

    result: List[TheoreticalPortifolio] = TheoreticalPortifolio.query.all()

    assert len(result) == 1

    for k in ifix.keys():
        assert getattr(result[0], k) == ifix[k]


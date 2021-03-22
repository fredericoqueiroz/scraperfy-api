import datetime
from typing import List

from financial_data.tests.fixtures import app, db
from flask_sqlalchemy import SQLAlchemy

from .interface import TheoreticalPortifolioInterface
from .model import TheoreticalPortifolio
from .service import TheoreticalPortifolioService


def test_get_all(db: SQLAlchemy):

    ibov: TheoreticalPortifolio = TheoreticalPortifolio(
        index = 'IBOV',
        asset_symbol = 'PETR4',
        asset_name = 'PETROBRAS',
        asset_type = 'PN N2',
        theoretical_quantity = '4.566.457.037',
        percentage_share = '5,133',
        portifolio_date = '2021-01-20'
    )

    ifix: TheoreticalPortifolio = TheoreticalPortifolio(
        index = 'IFIX',
        asset_symbol = 'HGRU11',
        asset_name = 'FII CSHG URB',
        asset_type = 'CI',
        theoretical_quantity = '18.406.458',
        percentage_share = '2,528',
        portifolio_date = '2021-01-21'
    )
    
    db.session.add(ibov)
    db.session.add(ifix)
    db.session.commit()

    result: List[TheoreticalPortifolio] = TheoreticalPortifolioService.get_all()

    assert len(result) == 2
    assert ibov in result and ifix in result

def test_update(db: SQLAlchemy):

    tp: TheoreticalPortifolio = TheoreticalPortifolio(
        index = 'IFIX',
        asset_symbol = 'HGRU11',
        asset_name = 'FII CSHG URB',
        asset_type = 'CI',
        theoretical_quantity = '18.406.458',
        percentage_share = '2,528',
        portifolio_date = '2021-01-21'
    )

    db.session.add(tp)
    db.session.commit()

    updates: TheoreticalPortifolioInterface = dict(percentage_share = '4,842')

    TheoreticalPortifolioService.update(tp, updates)

    result: TheoreticalPortifolio = TheoreticalPortifolio.query.get((tp.index, tp.asset_symbol))
    assert result.percentage_share == '4,842'

def test_delete_by_index_and_symbol(db: SQLAlchemy):

    ibov: TheoreticalPortifolio = TheoreticalPortifolio(
        index = 'IBOV',
        asset_symbol = 'PETR4',
        asset_name = 'PETROBRAS',
        asset_type = 'PN N2',
        theoretical_quantity = '4.566.457.037',
        percentage_share = '5,133',
        portifolio_date = '2021-01-20'
    )

    ifix: TheoreticalPortifolio = TheoreticalPortifolio(
        index = 'IFIX',
        asset_symbol = 'HGRU11',
        asset_name = 'FII CSHG URB',
        asset_type = 'CI',
        theoretical_quantity = '18.406.458',
        percentage_share = '2,528',
        portifolio_date = '2021-01-21'
    )

    db.session.add(ibov)
    db.session.add(ifix)
    db.session.commit()

    TheoreticalPortifolioService.delete_by_index_and_symbol('IBOV', 'PETR4')
    db.session.commit()

    result: List[TheoreticalPortifolio] = TheoreticalPortifolio.query.all()

    assert len(result) == 1
    assert ibov not in result and ifix in result


def test_create(db: SQLAlchemy):

    ifix: TheoreticalPortifolio = dict(
        index = 'IFIX',
        asset_symbol = 'HGRU11',
        asset_name = 'FII CSHG URB',
        asset_type = 'CI',
        theoretical_quantity = '18.406.458',
        percentage_share = '2,528',
        portifolio_date = datetime.date(2021, 1, 21)
    )

    TheoreticalPortifolioService.create(ifix)

    result: List[TheoreticalPortifolio] = TheoreticalPortifolio.query.all()

    assert len(result) == 1

    for k in ifix.keys():
        assert getattr(result[0], k) == ifix[k]


from pytest import fixture

from .interface import TheoreticalPortifolioInterface
from .model import TheoreticalPortifolio


@fixture
def interface() -> TheoreticalPortifolioInterface:
    return TheoreticalPortifolioInterface(
        index = 'IBOV',
        asset_symbol = 'PETR4',
        asset_name = 'PETROBRAS',
        asset_type = 'PN N2',
        theoretical_quantity = '4.566.457.037',
        percentage_share = '5,133',
        portifolio_date = '2021-01-20'
    )

def test_theoretical_portifolio_interface_create(interface: TheoreticalPortifolioInterface):
    assert interface

def test_theoretical_portifolio_works(interface: TheoreticalPortifolioInterface):
    tp = TheoreticalPortifolio(**interface)
    assert tp


from pytest import fixture

from .model import TheoreticalPortifolio


@fixture
def theoretical_portifolio() -> TheoreticalPortifolio:
    return TheoreticalPortifolio(
        index_symbol = 'IBOV',
        portifolio_date = '2021-01-20',
        asset_symbol = 'PETR4',
        asset_name = 'PETROBRAS',
        asset_type = 'PN N2',
        theoretical_quantity = '4.566.457.037',
        percentage_share = '5,133'
    )

def test_theoretical_portifolio_create(theoretical_portifolio: TheoreticalPortifolio):
    assert theoretical_portifolio


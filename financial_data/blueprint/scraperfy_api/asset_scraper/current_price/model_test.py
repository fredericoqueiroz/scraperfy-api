from pytest import fixture

from .model import CurrentPrice


@fixture
def current_price() -> CurrentPrice:
    return CurrentPrice(
        asset_id = 1,
        asset_symbol = 'IBOV',
        asset_price = 119198.63,
        asset_oscilation = -0.96,
        search_date = '2021-01-20',
        search_time = '16:20:00'
    )

def test_current_price_create(current_price: CurrentPrice):
    assert current_price


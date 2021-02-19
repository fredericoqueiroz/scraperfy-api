from pytest import fixture
from .model import CurrentPrice

@fixture
def current_price() -> CurrentPrice:
    return CurrentPrice(
        asset_id=1, asset_symbol='IBOV', asset_price=119198.63, asset_oscilation=-0.96
    )

def test_current_price_create(current_price: CurrentPrice):
    assert current_price


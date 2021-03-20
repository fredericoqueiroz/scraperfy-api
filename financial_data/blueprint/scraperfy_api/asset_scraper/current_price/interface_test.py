from pytest import fixture

from .interface import CurrentPriceInterface
from .model import CurrentPrice


@fixture
def interface() -> CurrentPriceInterface:
    return CurrentPriceInterface(
        asset_id=1,
        asset_symbol='IFIX',
        asset_price=2892.76,
        asset_oscilation=-0.09,
        search_date = '2021-01-20',
        search_time = '16:20:00'
    )


def test_current_price_interface_create(interface: CurrentPriceInterface):
    assert interface

def test_current_price_works(interface: CurrentPriceInterface):
    current_price = CurrentPrice(**interface)
    assert current_price

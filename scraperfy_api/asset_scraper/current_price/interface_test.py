from pytest import fixture
from .model import CurrentPrice
from .interface import CurrentPriceInterface

@fixture
def interface() -> CurrentPriceInterface:
    return CurrentPriceInterface(
        asset_id=1, asset_symbol='IFIX', asset_price=2892.76, asset_oscilation=-0.09
    )


def test_current_price_interface_create(interface: CurrentPriceInterface):
    assert interface

def test_current_price_works(interface: CurrentPriceInterface):
    current_price = CurrentPrice(**interface)
    assert current_price
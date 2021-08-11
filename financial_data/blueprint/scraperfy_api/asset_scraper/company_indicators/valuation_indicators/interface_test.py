from pytest import fixture

from .interface import ValuationIndicatorsInterface
from .model import ValuationIndicators


@fixture
def interface() -> ValuationIndicatorsInterface:
    return ValuationIndicatorsInterface(
        asset_id = 1,
        asset_symbol = 'B3SA3',
        search_date = '2021-08-07T11:23:52.277828',
        dividend_yield = 6.52,
        price_earnings = 22.10,
        peg_ratio = 0.55,
        price_book_value = 3.98,
        ev_ebitda = 12.48,
        ev_ebit = 14.63,
        price_ebitda = 13.70,
        price_ebit = 16.06,
        book_value_share = 3.97,
        price_asset = 2.10,
        earnings_share = 0.72,
        prices_sales_ratio = 0,
        prices_working_capital = 13.13,
        price_net_current_assets = -3.30
    )


def test_valuation_indicators_interface_create(interface: ValuationIndicatorsInterface):
    assert interface

def test_valuation_indicators_works(interface: ValuationIndicatorsInterface):
    valuation_indicators = ValuationIndicators(**interface)
    assert valuation_indicators


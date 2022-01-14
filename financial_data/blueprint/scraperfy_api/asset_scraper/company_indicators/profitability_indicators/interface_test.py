from pytest import fixture

from .interface import ProfitabilityIndicatorsInterface
from .model import ProfitabilityIndicators

@fixture
def interface() -> ProfitabilityIndicatorsInterface:
    return ProfitabilityIndicatorsInterface(
        asset_id = 1,
        asset_symbol = 'SULA11',
        search_date = '2021-08-26T11:23:52.277828',
        return_on_equity = 23.06,
        return_on_assets = 6.66,
        return_on_invested_capital = 3.34,
        asset_turnover_ratio = 0.68
    )

def test_profitability_indicators_interface_create(interface: ProfitabilityIndicatorsInterface):
    assert interface

def test_profitability_indicators_works(interface: ProfitabilityIndicatorsInterface):
    profitability_indicators = ProfitabilityIndicators(**interface)
    assert profitability_indicators


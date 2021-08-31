from pytest import fixture

from .interface import DebtIndicatorsInterface
from . model import DebtIndicators

@fixture
def interface() -> DebtIndicatorsInterface:
    return DebtIndicatorsInterface(
        asset_id = 1,
        asset_symbol = 'SULA11',
        search_date = '2021-08-26T11:23:52.277828',
        debt_net_worth = -1.86,
        debt_ebitda = -7.33,
        debt_ebit = -32.71,
        net_worth_assets = 0.29,
        liabilities_assets = 0.71,
        current_liquidity = 2.25
    )

def test_debt_indicators_interface_create(interface: DebtIndicatorsInterface):
    assert interface

def test_debt_indicators_works(interface: DebtIndicatorsInterface):
    debt_indicators = DebtIndicators(**interface)
    assert debt_indicators


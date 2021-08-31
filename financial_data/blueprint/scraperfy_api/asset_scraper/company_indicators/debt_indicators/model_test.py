from datetime import datetime

from pytest import fixture

from .model import DebtIndicators


@fixture
def debt_indicators() -> DebtIndicators:
    return DebtIndicators(
        asset_id = 1,
        asset_symbol = 'SULA11',
        search_date = datetime.now().isoformat(),
        debt_net_worth = -1.86,
        debt_ebitda = -7.33,
        debt_ebit = -32.71,
        net_worth_assets = 0.29,
        liabilities_assets = 0.71,
        current_liquidity = 2.25
    )

def test_debt_indicators_create(debt_indicators: DebtIndicators):
    assert debt_indicators


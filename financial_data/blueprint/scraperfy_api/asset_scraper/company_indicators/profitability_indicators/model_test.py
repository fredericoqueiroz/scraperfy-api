from datetime import datetime

from pytest import fixture

from .model import ProfitabilityIndicators


@fixture
def profitability_indicators() -> ProfitabilityIndicators:
    return ProfitabilityIndicators(
        asset_id = 1,
        asset_symbol = 'SULA11',
        search_date = datetime.now().isoformat(),
        return_on_equity = 23.06,
        return_on_assets = 6.66,
        return_on_invested_capital = 3.34,
        asset_turnover_ratio = 0.68
    )

def test_profitability_indicators_create(profitability_indicators: ProfitabilityIndicators):
    assert profitability_indicators


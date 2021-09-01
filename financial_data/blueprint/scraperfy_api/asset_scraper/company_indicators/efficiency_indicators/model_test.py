from datetime import datetime

from pytest import fixture

from .model import EfficiencyIndicators


@fixture
def efficiency_indicators() -> EfficiencyIndicators:
    return EfficiencyIndicators(
        asset_id = 1,
        asset_symbol = 'SULA11',
        search_date = datetime.now().isoformat(),
        gross_margin = 10.16,
        ebitda_margin = 10.71,
        ebit_margin = 2.40,
        net_margin = 9.74
    )

def test_efficiency_indicators_create(efficiency_indicators: EfficiencyIndicators):
    assert efficiency_indicators


from pytest import fixture

from .interface import EfficiencyIndicatorsInterface
from .model import EfficiencyIndicators

@fixture
def interface() -> EfficiencyIndicatorsInterface:
    return EfficiencyIndicatorsInterface(
        asset_id = 1,
        asset_symbol = 'SULA11',
        search_date = '2021-08-26T11:23:52.277828',
        gross_margin = 10.16,
        ebitda_margin = 10.71,
        ebit_margin = 2.40,
        net_margin = 9.74
    )

def test_efficiency_indicators_interface_create(interface: EfficiencyIndicatorsInterface):
    assert interface

def test_efficiency_indicators_works(interface: EfficiencyIndicatorsInterface):
    efficiency_indicators = EfficiencyIndicators(**interface)
    assert efficiency_indicators


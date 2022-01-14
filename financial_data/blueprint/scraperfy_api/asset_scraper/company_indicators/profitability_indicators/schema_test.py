import datetime

from pytest import fixture

from .interface import ProfitabilityIndicatorsInterface
from .model import ProfitabilityIndicators
from .schema import ProfitabilityIndicatorsSchema


@fixture
def schema() -> ProfitabilityIndicatorsSchema:
    return ProfitabilityIndicatorsSchema()


def test_profitability_indicators_schema_create(schema: ProfitabilityIndicatorsSchema):
    assert schema


def test_profitability_indicators_schema_works(schema: ProfitabilityIndicatorsSchema):

    params: ProfitabilityIndicatorsInterface = schema.load(
        {
            'assetId': '9999',
            'assetSymbol': 'SULA11',
            'searchDate': '2021-08-07T11:23:52.277828',
            'returnOnEquity': '23.06',
            'returnOnAssets': '6.66',
            'returnOnInvestedCapital': '3.34',
            'assetTurnoverRatio': '0.68'
        }
    )

    profitability_indicators = ProfitabilityIndicators(**params)

    assert profitability_indicators.asset_id == 9999
    assert profitability_indicators.asset_symbol == 'SULA11'
    assert profitability_indicators.search_date == datetime.datetime(2021,8,7,11,23,52,277828)
    assert profitability_indicators.return_on_equity == 23.06
    assert profitability_indicators.return_on_assets == 6.66
    assert profitability_indicators.return_on_invested_capital == 3.34
    assert profitability_indicators.asset_turnover_ratio == 0.68


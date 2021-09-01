import datetime
from financial_data.blueprint.scraperfy_api.asset_scraper.company_indicators.debt_indicators.model_test import debt_indicators

from pytest import fixture

from .interface import EfficiencyIndicatorsInterface
from .model import EfficiencyIndicators
from .schema import EfficiencyIndicatorsSchema


@fixture
def schema() -> EfficiencyIndicatorsSchema:
    return EfficiencyIndicatorsSchema()


def test_efficiency_indicators_schema_create(schema: EfficiencyIndicatorsSchema):
    assert schema


def test_efficiency_indicators_schema_works(schema: EfficiencyIndicatorsSchema):

    params: EfficiencyIndicatorsInterface = schema.load(
        {
            'assetId': '9999',
            'assetSymbol': 'SULA11',
            'searchDate': '2021-08-07T11:23:52.277828',
            'grossMargin': '10.16',
            'ebitdaMargin': '10.71',
            'ebitMargin': '2.40',
            'netMargin': '9.74'
        }
    )

    efficiency_indicators = EfficiencyIndicators(**params)

    assert efficiency_indicators.asset_id == 9999
    assert efficiency_indicators.asset_symbol == 'SULA11'
    assert efficiency_indicators.search_date == datetime.datetime(2021,8,7,11,23,52,277828)
    assert efficiency_indicators.gross_margin == 10.16
    assert efficiency_indicators.ebitda_margin == 10.71
    assert efficiency_indicators.ebit_margin == 2.40
    assert efficiency_indicators.net_margin == 9.74


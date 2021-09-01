import datetime

from pytest import fixture

from .interface import DebtIndicatorsInterface
from .model import DebtIndicators
from .schema import DebtIndicatorsSchema


@fixture
def schema() -> DebtIndicatorsSchema:
    return DebtIndicatorsSchema()


def test_debt_indicators_schema_create(schema: DebtIndicatorsSchema):
    assert schema


def test_debt_indicators_schema_works(schema: DebtIndicatorsSchema):

    params: DebtIndicatorsInterface = schema.load(
        {
            'assetId': '9999',
            'assetSymbol': 'SULA11',
            'searchDate': '2021-08-07T11:23:52.277828',
            'debtNetWorth': '-1.86',
            'debtEbitda': '-7.33',
            'debtEbit': '-32.71',
            'netWorthAssets': '0.29',
            'liabilitiesAssets': '0.71',
            'currentLiquidity': '2.25'
        }
    )

    debt_indicators = DebtIndicators(**params)

    assert debt_indicators.asset_id == 9999
    assert debt_indicators.asset_symbol == 'SULA11'
    assert debt_indicators.search_date == datetime.datetime(2021,8,7,11,23,52,277828)
    assert debt_indicators.debt_net_worth == -1.86
    assert debt_indicators.debt_ebitda == -7.33
    assert debt_indicators.debt_ebit == -32.71
    assert debt_indicators.net_worth_assets == 0.29
    assert debt_indicators.liabilities_assets == 0.71
    assert debt_indicators.current_liquidity == 2.25

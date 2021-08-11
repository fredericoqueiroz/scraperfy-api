import datetime

from pytest import fixture

from .interface import ValuationIndicatorsInterface
from .model import ValuationIndicators
from .schema import ValuationIndicatorsSchema


@fixture
def schema() -> ValuationIndicatorsSchema:
    return ValuationIndicatorsSchema()


def test_valuation_indicators_schema_create(schema: ValuationIndicatorsSchema):
    assert schema


def test_valuation_indicators_schema_works(schema: ValuationIndicatorsSchema):

    params: ValuationIndicatorsInterface = schema.load(
        {
            'assetId': '12345',
            'assetSymbol': 'B3SA3',
            'searchDate':'2021-08-07T11:23:52.277828',
            'dividendYield': '6.48',
            'priceEarnings': '22.22',
            'pegRatio': '0.56',
            'priceBookValue': '4.00',
            'evEbitda': '12.57',
            'evEbit': '14.73',
            'priceEbitda': '13.77',
            'priceEbit': '16.15',
            'bookValueShare': '3.97',
            'priceAsset': '2.11',
            'earningsShare': '0.72',
            'pricesSalesRatio': '9.92',
            'pricesWorkingCapital': '13.20',
            'priceNetCurrentAssets': '-3.32'
        }
    )

    valuation_indicators = ValuationIndicators(**params)

    assert valuation_indicators.asset_id == 12345
    assert valuation_indicators.asset_symbol == 'B3SA3'
    assert valuation_indicators.search_date == datetime.datetime(2021,8,7,11,23,52,277828)
    assert valuation_indicators.dividend_yield == 6.48
    assert valuation_indicators.price_earnings == 22.22
    assert valuation_indicators.peg_ratio == 0.56
    assert valuation_indicators.price_book_value == 4.00
    assert valuation_indicators.ev_ebitda == 12.57
    assert valuation_indicators.ev_ebit == 14.73
    assert valuation_indicators.price_ebitda == 13.77
    assert valuation_indicators.price_ebit == 16.15
    assert valuation_indicators.book_value_share == 3.97
    assert valuation_indicators.price_asset == 2.11
    assert valuation_indicators.earnings_share == 0.72
    assert valuation_indicators.prices_sales_ratio == 9.92
    assert valuation_indicators.prices_working_capital == 13.20
    assert valuation_indicators.price_net_current_assets == -3.32


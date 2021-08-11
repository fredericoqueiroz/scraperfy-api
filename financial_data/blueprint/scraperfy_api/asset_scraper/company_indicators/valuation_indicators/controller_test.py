import datetime
from unittest.mock import patch

from financial_data.blueprint.scraperfy_api import URL_PREFIX
from financial_data.tests.fixtures import app, client
from flask.testing import FlaskClient

from . import BASE_ROUTE
from .interface import ValuationIndicatorsInterface
from .model import ValuationIndicators
from .schema import ValuationIndicatorsSchema
from .service import ValuationIndicatorsService

#2021-08-07T11:23:52.277828
#datetime.datetime(2021,8,7,11,23,52)

def make_valuation_indicator(
    id: int = 123, symbol: str = 'Teste symbol', searchDate: datetime.datetime = datetime.datetime(2021,8,7,11,23,52),
    dividendYield: float = 6.48, priceEarnings: float = 22.22, pegRatio: float = 0.56, priceBookValue: float = 4.00,
    evEbitda: float = 12.57, evEbit: float = 14.73, priceEbitda: float = 13.77, priceEbit: float = 16.15,
    bookValueShare: float = 3.97, priceAsset: float = 2.11, earningsShare: float = 0.72, 
    pricesSalesRatio: float = 9.92, pricesWorkingCapital: float = 13.20, priceNetCurrentAssets: float = -3.32
) -> ValuationIndicators:
    return ValuationIndicators(asset_id=id, asset_symbol=symbol.upper(), search_date=searchDate, dividend_yield=dividendYield,
                               price_earnings=priceEarnings, peg_ratio=pegRatio, price_book_value=priceBookValue, ev_ebitda=evEbitda,
                               ev_ebit=evEbit, price_ebitda=priceEbitda, price_ebit=priceEbit, book_value_share=bookValueShare, price_asset=priceAsset,
                               earnings_share=earningsShare, prices_sales_ratio=pricesSalesRatio, prices_working_capital=pricesWorkingCapital, 
                               price_net_current_assets=priceNetCurrentAssets)


class TestValuationIndicatorsResource:

    @patch.object(
        ValuationIndicatorsService,
        'get_all',
        lambda: [
            make_valuation_indicator(123, symbol='Test symbol 1'),
            make_valuation_indicator(456, symbol='Test symbol 2'),
        ]
    )
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'{URL_PREFIX}{BASE_ROUTE}', follow_redirects=True).get_json()
            expected = (
                ValuationIndicatorsSchema(many=True)
                .dump(
                    [
                        make_valuation_indicator(123, symbol='Test symbol 1'),
                        make_valuation_indicator(456, symbol='Test symbol 2'),
                    ]
                )
            )
            for r in results:
                assert r in expected

    @patch.object(
        ValuationIndicatorsService,
        'create',
        lambda create_request: ValuationIndicators(**create_request)
    )
    def test_post(self, client: FlaskClient):
        with client:
            payload = dict(assetSymbol='B3SA3', dividendYield=9.99, priceEarnings=99.99)
            result = client.post(f'{URL_PREFIX}{BASE_ROUTE}/', json=payload).get_json()
            expected = (
                ValuationIndicatorsSchema()
                .dump(ValuationIndicators(
                    asset_symbol=payload['assetSymbol'],
                    dividend_yield=payload['dividendYield'],
                    price_earnings=payload['priceEarnings']
                ))
            )
            assert result == expected

def fake_update(asset: ValuationIndicators, changes: ValuationIndicatorsInterface) -> ValuationIndicators:
    '''To simulate an update, just return a new object'''
    updated_asset = ValuationIndicators(
        asset_id = asset.asset_id,
        asset_symbol = changes['asset_symbol'],
        search_date = datetime.datetime(2021,8,7,11,23,52),
        dividend_yield = changes['dividend_yield'],
        price_earnings = changes['price_earnings'],
        peg_ratio = changes['peg_ratio'],
        price_book_value = changes['price_book_value'],
        ev_ebitda = changes ['ev_ebitda'],
        ev_ebit = changes['ev_ebit'],
        price_ebitda = changes['price_ebitda'],
        price_ebit = changes['price_ebit'],
        book_value_share = changes['book_value_share'],
        price_asset = changes['price_asset'],
        earnings_share = changes['earnings_share'],
        prices_sales_ratio = changes['prices_sales_ratio'],
        prices_working_capital = changes['prices_working_capital'],
        price_net_current_assets = changes['price_net_current_assets']
    )
    return updated_asset

class TestValuationIndicatorsSymbolResource:

    @patch.object(
        ValuationIndicatorsService,
        'get_by_symbol',
        lambda symbol: make_valuation_indicator(symbol=symbol)
    )
    def test_get(self, client: FlaskClient):
        with client:
            result = client.get(f'{URL_PREFIX}{BASE_ROUTE}/TEST SYMBOL').get_json()
            expected = make_valuation_indicator(symbol = 'Test symbol')
            assert result['assetSymbol'] == expected.asset_symbol

    @patch.object(ValuationIndicatorsService, 'delete_by_symbol', lambda symbol: symbol.upper())
    def test_delete(self, client: FlaskClient):
        result = client.delete(f'{URL_PREFIX}{BASE_ROUTE}/Test Symbol').get_json()
        expected = dict(status='Success', symbol='TEST SYMBOL')
        assert result == expected

    @patch.object(
        ValuationIndicatorsService,
        'get_by_symbol',
        lambda symbol: make_valuation_indicator(symbol=symbol)
    )
    @patch.object(ValuationIndicatorsService, 'update', fake_update)
    def test_put(self, client: FlaskClient):
        result = client.put(
            f'{URL_PREFIX}{BASE_ROUTE}/Test Symbol',
            json={
                'assetSymbol': 'New Asset',
                'searchDate': '2021-08-11T16:31:56.167936',
                'dividendYield': '99.99',
                'priceEarnings': '88.88',
                'pegRatio': '4.69',
                'priceBookValue': '3.98',
                'evEbitda': '12.49',
                'evEbit': '14.63',
                'priceEbitda': '13.70',
                'priceEbit': '16.06',
                'bookValueShare': '3.97',
                'priceAsset': '2.10',
                'earningsShare': '0.72',
                'pricesSalesRatio': '0',
                'pricesWorkingCapital': '13.13',
                'priceNetCurrentAssets': '-3.30'
            }
        ).get_json()

        expected = (
            ValuationIndicatorsSchema()
            .dump(
                ValuationIndicators(
                    asset_id = 123,
                    asset_symbol = 'New Asset',
                    search_date = datetime.datetime(2021,8,7,11,23,52),
                    dividend_yield = 99.99,
                    price_earnings = 88.88,
                    peg_ratio = 4.69,
                    price_book_value = 3.98,
                    ev_ebitda = 12.49,
                    ev_ebit = 14.63,
                    price_ebitda = 13.70,
                    price_ebit = 16.06,
                    book_value_share = 3.97,
                    price_asset = 2.10,
                    earnings_share = 0.72,
                    prices_sales_ratio = 0,
                    prices_working_capital = 13.13,
                    price_net_current_assets = -3.30
                )
            )
        )
        assert result == expected


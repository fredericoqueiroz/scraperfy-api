from unittest.mock import patch

from financial_data.blueprint.scraperfy_api import URL_PREFIX
from financial_data.tests.fixtures import app, client
from flask.testing import FlaskClient

from . import BASE_ROUTE
from .interface import CurrentPriceInterface
from .model import CurrentPrice
from .schema import CurrentPriceSchema
from .service import CurrentPriceService


def make_current_price(
    id: int = 123, symbol: str = 'Test symbol', price: float = 123.45, oscilation: float = -12.34
) -> CurrentPrice:
    return CurrentPrice(asset_id=id, asset_symbol=symbol.upper(), asset_price=price, asset_oscilation=oscilation)


class TestCurrentPriceResource:
    
    @patch.object(
        CurrentPriceService,
        'get_all',
        lambda: [
            make_current_price(123, symbol='Test symbol 1'),
            make_current_price(456, symbol='Test symbol 2'),
        ]
    )
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'{URL_PREFIX}{BASE_ROUTE}', follow_redirects=True).get_json()
            expected = (
                CurrentPriceSchema(many=True)
                .dump(
                    [
                        make_current_price(123, symbol='Test symbol 1'),
                        make_current_price(456, symbol='Test symbol 2'),
                    ]
                )
            )
            for r in results:
                assert r in expected

    @patch.object(
        CurrentPriceService,
        'create',
        lambda create_request:  CurrentPrice(**create_request)
    )
    def test_post(self, client: FlaskClient):
        with client:
            payload = dict(assetSymbol='IBOV', assetPrice=112787.81, assetOscilation=-4.76)
            result = client.post(f'{URL_PREFIX}{BASE_ROUTE}/', json=payload).get_json()
            expected = (
                CurrentPriceSchema()
                .dump(CurrentPrice(
                    asset_symbol=payload['assetSymbol'],
                    asset_price=payload['assetPrice'],
                    asset_oscilation=payload['assetOscilation'],
                ))
            )
            assert result == expected

def fake_update(asset: CurrentPrice, changes: CurrentPriceInterface) -> CurrentPrice:
    '''To simulate an update, just return a new object'''
    updated_asset = CurrentPrice(
        asset_id = asset.asset_id,
        asset_symbol = changes['asset_symbol'],
        asset_price = changes['asset_price'],
        asset_oscilation = changes['asset_oscilation']
    )
    return updated_asset

class TestCurrentPriceSymbolResource:

    @patch.object(
        CurrentPriceService,
        'get_by_symbol',
        lambda symbol: make_current_price(symbol=symbol)
    )
    def test_get(self, client: FlaskClient):
        with client:
            result = client.get(f'{URL_PREFIX}{BASE_ROUTE}/TEST SYMBOL').get_json()
            expected = make_current_price(symbol='Test symbol')
            assert result['assetSymbol'] == expected.asset_symbol

    @patch.object(CurrentPriceService, 'delete_by_symbol', lambda symbol: symbol.upper())
    def test_delete(self, client: FlaskClient):
        result = client.delete(f'{URL_PREFIX}{BASE_ROUTE}/Test Symbol').get_json()
        expected = dict(status='Success', symbol='TEST SYMBOL')
        assert result == expected

    @patch.object(
        CurrentPriceService,
        'get_by_symbol',
        lambda symbol: make_current_price(symbol=symbol)
    )
    @patch.object(CurrentPriceService, 'update', fake_update)
    def test_put(self, client: FlaskClient):
        result = client.put(
            f'{URL_PREFIX}{BASE_ROUTE}/Test Symbol',
            json={
                "assetSymbol": "New Asset",
                "assetPrice": 112033.02,
                "assetOscilation": -5.14
            }
        ).get_json()
        expected = (
            CurrentPriceSchema()
            .dump(
                CurrentPrice(
                    asset_id = 123,
                    asset_symbol = 'New Asset',
                    asset_price = 112033.02, 
                    asset_oscilation = -5.14
                )
            )
        )
        assert result == expected

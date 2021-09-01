import datetime
from unittest.mock import patch

from financial_data.blueprint.scraperfy_api import URL_PREFIX
from financial_data.tests.fixtures import app, client
from flask.testing import FlaskClient

from . import BASE_ROUTE
from .interface import EfficiencyIndicatorsInterface
from .model import EfficiencyIndicators
from .schema import EfficiencyIndicatorsSchema
from .service import EfficiencyIndicatorsService

def make_efficiency_indicator(
    id: int = 123, symbol: str = 'Teste symbol', searchDate: datetime.datetime = datetime.datetime(2021,8,7,11,23,52),
    grossMargin: float = 10.16, ebitdaMargin: float = 10.71, ebitMargin: float = 2.40, netMargin: float = 9.74
) -> EfficiencyIndicators:
    return EfficiencyIndicators(asset_id=id, asset_symbol=symbol.upper(), search_date=searchDate,
                                gross_margin=grossMargin, ebitda_margin=ebitdaMargin, ebit_margin=ebitMargin, net_margin=netMargin)


class TestEfficiencyIndicatorsResource:

    @patch.object(
        EfficiencyIndicatorsService,
        'get_all',
        lambda: [
            make_efficiency_indicator(123, symbol='Test symbol 1'),
            make_efficiency_indicator(456, symbol='Test symbol 2'),
        ]
    )
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'{URL_PREFIX}{BASE_ROUTE}', follow_redirects=True).get_json()
            expected = (
                EfficiencyIndicatorsSchema(many=True)
                .dump(
                    [
                        make_efficiency_indicator(123, symbol='Test symbol 1'),
                        make_efficiency_indicator(456, symbol='Test symbol 2'),
                    ]
                )
            )
            for r in results:
                assert r in expected

    @patch.object(
        EfficiencyIndicatorsService,
        'create',
        lambda create_request: EfficiencyIndicators(**create_request)
    )
    def test_post(self, client: FlaskClient):
        with client:
            payload = dict(assetSymbol='B3SA3', grossMargin=9.99, ebitdaMargin=-99.99)
            result = client.post(f'{URL_PREFIX}{BASE_ROUTE}/', json=payload).get_json()
            expected = (
                EfficiencyIndicatorsSchema()
                .dump(EfficiencyIndicators(
                    asset_symbol=payload['assetSymbol'],
                    gross_margin=payload['grossMargin'],
                    ebitda_margin=payload['ebitdaMargin']
                ))
            )
            assert result == expected

def fake_update(asset: EfficiencyIndicators, changes: EfficiencyIndicatorsInterface) -> EfficiencyIndicators:
    '''To simulate an update, just return a new object'''
    updated_asset = EfficiencyIndicators(
        asset_id = asset.asset_id,
        asset_symbol = changes['asset_symbol'],
        search_date = datetime.datetime(2021,8,7,11,23,52),
        gross_margin = changes['gross_margin'],
        ebitda_margin = changes['ebitda_margin'],
        ebit_margin = changes['ebit_margin'],
        net_margin = changes['net_margin']
    )
    return updated_asset

class TestEfficiencyIndicatorsSymbolResource:

    @patch.object(
        EfficiencyIndicatorsService,
        'get_by_symbol',
        lambda symbol: make_efficiency_indicator(symbol=symbol)
    )
    def test_get(self, client: FlaskClient):
        with client:
            result = client.get(f'{URL_PREFIX}{BASE_ROUTE}/TEST SYMBOL').get_json()
            expected = make_efficiency_indicator(symbol = 'Test Symbol')
            assert result['assetSymbol'] == expected.asset_symbol

    @patch.object(
        EfficiencyIndicatorsService,
        'get_by_symbol',
        lambda symbol: make_efficiency_indicator(symbol=symbol)
    )
    @patch.object(EfficiencyIndicatorsService, 'update', fake_update)
    def test_put(self, client: FlaskClient):
        result = client.put(
            f'{URL_PREFIX}{BASE_ROUTE}/Test Symbol',
            json={
                'assetSymbol': 'New Asset',
                'searchDate': '2021-08-07T11:23:52.277828',
                'grossMargin': '10.16',
                'ebitdaMargin': '10.71',
                'ebitMargin': '2.40',
                'netMargin': '9.74'
            }
        ).get_json()

        expected = (
            EfficiencyIndicatorsSchema()
            .dump(
                EfficiencyIndicators(
                    asset_id = 123,
                    asset_symbol = 'New Asset',
                    search_date = datetime.datetime(2021,8,7,11,23,52),
                    gross_margin = 10.16,
                    ebitda_margin = 10.71,
                    ebit_margin = 2.40,
                    net_margin = 9.74
                )
            )
        )
        assert result == expected


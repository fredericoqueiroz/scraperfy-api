import datetime
from unittest.mock import patch

from financial_data.blueprint.scraperfy_api import URL_PREFIX
from financial_data.tests.fixtures import app, client
from flask.testing import FlaskClient

from . import BASE_ROUTE
from .interface import DebtIndicatorsInterface
from .model import DebtIndicators
from .schema import DebtIndicatorsSchema
from .service import DebtIndicatorsService

def make_debt_indicator(
    id: int = 123, symbol: str = 'Teste symbol', searchDate: datetime.datetime = datetime.datetime(2021,8,7,11,23,52),
    debtNetWorth: float = -1.86, debtEbitda: float = -7.33, debtEbit: float = -32.71, netWorthAssets: float = 0.29,
    liabilitiesAssets: float = 0.71, currentLiquidity: float = 2.25
) -> DebtIndicators:
    return DebtIndicators(asset_id=id, asset_symbol=symbol.upper(), search_date=searchDate,
                          debt_net_worth=debtNetWorth, debt_ebitda=debtEbitda, debt_ebit=debtEbit,
                          net_worth_assets=netWorthAssets, liabilities_assets=liabilitiesAssets, current_liquidity=currentLiquidity)


class TestDebtIndicatorsResource:

    @patch.object(
        DebtIndicatorsService,
        'get_all',
        lambda: [
            make_debt_indicator(123, symbol='Test symbol 1'),
            make_debt_indicator(456, symbol='Test symbol 2'),
        ]
    )
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'{URL_PREFIX}{BASE_ROUTE}', follow_redirects=True).get_json()
            expected = (
                DebtIndicatorsSchema(many=True)
                .dump(
                    [
                        make_debt_indicator(123, symbol='Test symbol 1'),
                        make_debt_indicator(456, symbol='Test symbol 2'),
                    ]
                )
            )
            for r in results:
                assert r in expected
    
    @patch.object(
        DebtIndicatorsService,
        'create',
        lambda create_request: DebtIndicators(**create_request)
    )
    def test_post(self, client: FlaskClient):
        with client:
            payload = dict(assetSymbol='B3SA3', debtNetWorth=9.99, debtEbitda=-99.99)
            result = client.post(f'{URL_PREFIX}{BASE_ROUTE}/', json=payload).get_json()
            expected = (
                DebtIndicatorsSchema()
                .dump(DebtIndicators(
                    asset_symbol=payload['assetSymbol'],
                    debt_net_worth=payload['debtNetWorth'],
                    debt_ebitda=payload['debtEbitda']
                ))
            )
            assert result == expected

def fake_update(asset: DebtIndicators, changes: DebtIndicatorsInterface) -> DebtIndicators:
    '''To simulate an update, just return a new object'''
    updated_asset = DebtIndicators(
        asset_id = asset.asset_id,
        asset_symbol= changes['asset_symbol'],
        search_date = datetime.datetime(2021,8,7,11,23,52),
        debt_net_worth = changes['debt_net_worth'],
        debt_ebitda = changes['debt_ebitda'],
        debt_ebit = changes['debt_ebit'],
        net_worth_assets = changes['net_worth_assets'],
        liabilities_assets = changes['liabilities_assets'],
        current_liquidity = changes['current_liquidity']
    )
    return updated_asset

class TestDebtIndicatorsSymbolResource:

    @patch.object(
        DebtIndicatorsService,
        'get_by_symbol',
        lambda symbol: make_debt_indicator(symbol=symbol)
    )
    def test_get(self, client: FlaskClient):
        with client:
            result = client.get(f'{URL_PREFIX}{BASE_ROUTE}/TEST SYMBOL').get_json()
            expected = make_debt_indicator(symbol = 'Test Symbol')
            assert result['assetSymbol'] == expected.asset_symbol

    @patch.object(DebtIndicatorsService, 'delete_by_symbol', lambda symbol: symbol.upper())
    def test_delete(self, client: FlaskClient):
        result = client.delete(f'{URL_PREFIX}{BASE_ROUTE}/Test Symbol').get_json()
        expected = dict(status='Success', symbol='TEST SYMBOL')
        assert result == expected

    @patch.object(
        DebtIndicatorsService,
        'get_by_symbol',
        lambda symbol: make_debt_indicator(symbol=symbol)
    )
    @patch.object(DebtIndicatorsService, 'update', fake_update)
    def test_put(self, client: FlaskClient):
        result = client.put(
            f'{URL_PREFIX}{BASE_ROUTE}/Test Symbol',
            json={
                'assetSymbol': 'New Asset',
                'searchDate': '2021-08-11T16:31:56.167936',
                'debtNetWorth': '99.99',
                'debtEbitda': '88.88',
                'debtEbit': '77.77',
                'netWorthAssets': '66.66',
                'liabilitiesAssets': '55.55',
                'currentLiquidity': '44.44'
            }
        ).get_json()

        expected = (
            DebtIndicatorsSchema()
            .dump(
                DebtIndicators(
                    asset_id = 123,
                    asset_symbol = 'New Asset',
                    search_date = datetime.datetime(2021,8,7,11,23,52),
                    debt_net_worth = 99.99,
                    debt_ebitda = 88.88,
                    debt_ebit = 77.77,
                    net_worth_assets = 66.66,
                    liabilities_assets = 55.55,
                    current_liquidity= 44.44
                )
            )
        )
        assert  result == expected


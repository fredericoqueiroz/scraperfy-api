import datetime
from operator import index
from unittest.mock import patch

from financial_data.blueprint.scraperfy_api import URL_PREFIX
from financial_data.tests.fixtures import app, client
from flask.testing import FlaskClient

from . import BASE_ROUTE
from .interface import TheoreticalPortifolioInterface
from .model import TheoreticalPortifolio
from .schema import TheoreticalPortifolioSchema
from .service import TheoreticalPortifolioService


def make_theoretical_portifolio(
    index: str = 'IBOV', symbol: str = 'PETR4', name: str = 'BRADESPAR',
    type: str = 'PN N1', quantity: str = '222.075.664', share: str = '0,672',
    date: datetime.date = datetime.date(2021,1,20)
) -> TheoreticalPortifolio:
    return TheoreticalPortifolio(index=index, asset_symbol=symbol,asset_name=name,
                                asset_type=type, theoretical_quantity=quantity,
                                percentage_share=share, portifolio_date=date)


class TestTheoreticalPortifolioResource:

    @patch.object(
        TheoreticalPortifolioService,
        'get_all',
        lambda: [
            make_theoretical_portifolio('IBOV', symbol='PETR4'),
            make_theoretical_portifolio('IFIX', symbol='RBRP11'),
        ]
    )
    def test_get(self, client: FlaskClient):
        with client:
            results = client.get(f'{URL_PREFIX}{BASE_ROUTE}', follow_redirects=True).get_json()
            expected = (
                TheoreticalPortifolioSchema(many=True)
                .dump(
                    [
                        make_theoretical_portifolio('IBOV', symbol='PETR4'),
                        make_theoretical_portifolio('IFIX', symbol='RBRP11'),
                    ]
                )
            )
            for r in results:
                assert r in expected

    @patch.object(
        TheoreticalPortifolioService,
        'create',
        lambda create_request: TheoreticalPortifolio(**create_request)
    )
    def test_post(self, client: FlaskClient):
        with client:
            payload = dict(
                index='IBOV', assetSymbol='B3SA3', assetType='ON NM',
                assetName='B3', theoreticalQuantity='1.930.877.944',
                portifolioDate='2021-01-20', percentageShare='4,849'
            )
            result = client.post(f'{URL_PREFIX}{BASE_ROUTE}/', json=payload).get_json()
            expected = (
                TheoreticalPortifolioSchema()
                .dump(TheoreticalPortifolio(
                    index = payload['index'],
                    asset_symbol = payload['assetSymbol'],
                    asset_name = payload['assetName'],
                    asset_type = payload['assetType'],
                    theoretical_quantity = payload['theoreticalQuantity'],
                    percentage_share = payload['percentageShare'],
                    portifolio_date = datetime.date(2021,1,20)
                ))
            )
            assert result == expected

def fake_update(asset: TheoreticalPortifolio, changes: TheoreticalPortifolioInterface) -> TheoreticalPortifolio:
    '''To simulate an update, just return a new object'''
    updated_asset = TheoreticalPortifolio(
        index = asset.index.upper(),
        asset_symbol = changes['asset_symbol'].upper(),
        asset_name = changes['asset_name'].upper(),
        theoretical_quantity = changes['theoretical_quantity'],
        asset_type= changes['asset_type'],
        percentage_share= changes['percentage_share'],
        portifolio_date= changes['portifolio_date']
    )
    return updated_asset

class TestTheoreticalPortifolioIndexSymbolResource:

    @patch.object(
        TheoreticalPortifolioService,
        'get_by_index_and_symbol',
        lambda index, symbol: make_theoretical_portifolio(index=index, symbol=symbol)
    )
    def test_get(self, client: FlaskClient):
        with client:
            result = client.get(f'{URL_PREFIX}{BASE_ROUTE}/IFIX/VGIP11').get_json()
            expected = make_theoretical_portifolio(index='IFIX', symbol='VGIP11')
            assert result['index'] == expected.index
            assert  result['assetSymbol'] == expected.asset_symbol

    @patch.object(
        TheoreticalPortifolioService,
        'delete_by_index_and_symbol',
        lambda index, symbol: [index.upper(),symbol.upper()],
    )
    def test_delete(self, client: FlaskClient):
        result = client.delete(f'{URL_PREFIX}{BASE_ROUTE}/ifix/vgip11').get_json()
        expected = dict(status='Success', index='IFIX', symbol='VGIP11')
        assert result == expected

    @patch.object(
        TheoreticalPortifolioService,
        'get_by_index_and_symbol',
        lambda index, symbol: make_theoretical_portifolio(index=index, symbol=symbol)
    )
    @patch.object(TheoreticalPortifolioService,'update',fake_update)
    def test_put(self, client: FlaskClient):
        result = client.put(
            f'{URL_PREFIX}{BASE_ROUTE}/ibov/itsa4',
            json={
                "assetSymbol": "BBAS3",
                "assetName": "BRASIL",
                "assetType": "PN N1",
                "theoreticalQuantity": "222.075.664",
                "percentageShare": "0,672",
                "portifolioDate": "2021-02-20"
            }
        ).get_json()
        expected = (
            TheoreticalPortifolioSchema()
            .dump(
                TheoreticalPortifolio(
                    index = 'IBOV',
                    asset_symbol = 'BBAS3',
                    asset_name = 'BRASIL',
                    asset_type = 'PN N1',
                    theoretical_quantity = '222.075.664',
                    percentage_share= '0,672',
                    portifolio_date= datetime.date(2021,2,20)
                )
            )
        )
        assert result == expected

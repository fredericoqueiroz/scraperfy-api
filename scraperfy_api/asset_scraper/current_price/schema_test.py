from pytest import fixture

from .interface import CurrentPriceInterface
from .model import CurrentPrice
from .schema import CurrentPriceSchema

@fixture
def schema() -> CurrentPriceSchema:
    return CurrentPriceSchema()


def test_current_price_schema_create(schema: CurrentPriceSchema):
    assert schema


def test_current_price_schema_works(schema: CurrentPriceSchema):
    params: CurrentPriceInterface = schema.load(
        {'assetId': '12345',
         'assetSymbol': 'VGIP11',
         'assetPrice': '114.92',
         'assetOscilation': '+0.33'
        }
    )

    current_price = CurrentPrice(**params)

    assert current_price.asset_id == 12345
    assert current_price.asset_symbol == 'VGIP11'
    assert current_price.asset_price == 114.92
    assert  current_price.asset_oscilation == +0.33


import datetime

from _pytest.mark import param
from pytest import fixture

from .interface import TheoreticalPortifolioInterface
from .model import TheoreticalPortifolio
from .schema import TheoreticalPortifolioSchema


@fixture
def schema() -> TheoreticalPortifolioSchema:
    return TheoreticalPortifolioSchema()

def test_theoretical_portifolio_schema_create(schema: TheoreticalPortifolioSchema):
    assert schema


def test_theoretical_portifolio_schema_works(schema: TheoreticalPortifolioSchema):
    
    params: TheoreticalPortifolioInterface = schema.load(
        {
            'index': 'IFIX',
            'assetSymbol': 'BCFF11',
            'assetName': 'FII BC FFII',
            'assetType': 'CI ERS',
            'theoreticalQuantity': '26.921.354',
            'percentageShare': '2,629',
            'portifolioDate': '2021-01-20'
        }
    )

    tp = TheoreticalPortifolio(**params)

    assert tp.index == 'IFIX'
    assert tp.asset_symbol == 'BCFF11'
    assert tp.asset_name == 'FII BC FFII'
    assert tp.asset_type == 'CI ERS'
    assert tp.theoretical_quantity == '26.921.354'
    assert tp.percentage_share == '2,629'
    assert tp.portifolio_date == datetime.date(2021, 1, 20)

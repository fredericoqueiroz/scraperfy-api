from .model import CurrentPrice
from .schema import CurrentPriceSchema

BASE_ROUTE = '/currentPrice'


def register_routes(api):
    from .controller import api as current_price_api

    api.add_namespace(current_price_api, path=f'{BASE_ROUTE}')


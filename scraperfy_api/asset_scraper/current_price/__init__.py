from .model import CurrentPrice
from .schema import CurrentPriceSchema

BASE_ROUTE = 'currentPrice'


def register_routes(api, app, root='scraperfy'):
    from .controller import api as current_price_api

    api.add_namespace(current_price_api, path=f'/{root}/{BASE_ROUTE}')


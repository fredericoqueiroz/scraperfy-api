from .model import CurrentPrice
from .schema import CurrentPriceSchema

BASE_ROUTE = 'price'


def register_routes(api, app, root='api'):
    from .controller import api as current_price_api

    api.add_namespace(current_price_api, path=f'/{root}/{BASE_ROUTE}')



BASE_ROUTE = '/theoreticalPortifolio'


def register_routes(api):
    from .controller import api as theoretical_portifolio_api

    api.add_namespace(theoretical_portifolio_api, path=f'{BASE_ROUTE}')


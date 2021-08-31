
BASE_ROUTE = '/companyIndicators/valuationIndicators'


def register_routes(api):
    from .controller import api as valuation_indicators_api

    api.add_namespace(valuation_indicators_api, path=f'{BASE_ROUTE}')


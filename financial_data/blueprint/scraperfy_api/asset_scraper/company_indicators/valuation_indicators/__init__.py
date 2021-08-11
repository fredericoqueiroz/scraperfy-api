
BASE_ROUTE = '/companyIndicators/valuationIndicators'


def register_routes(api):
    from .controller import api as company_indicators_api

    api.add_namespace(company_indicators_api, path=f'{BASE_ROUTE}')


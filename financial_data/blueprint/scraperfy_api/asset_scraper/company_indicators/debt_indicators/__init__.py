
BASE_ROUTE = '/companyIndicators/debtIndicators'


def register_routes(api):
    from .controller import api as debt_indicators_api

    api.add_namespace(debt_indicators_api, path=f'{BASE_ROUTE}')


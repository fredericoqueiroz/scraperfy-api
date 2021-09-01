
BASE_ROUTE = '/companyIndicators/efficiencyIndicators'


def register_routes(api):
    from .controller import api as efficiency_indicators_api

    api.add_namespace(efficiency_indicators_api, path=f'{BASE_ROUTE}')


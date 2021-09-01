def register_routes(api):
    from .asset_scraper.current_price import register_routes as attach_current_price
    from .index_scraper.theoretical_portifolio import register_routes as attach_theoretical_portifolio
    from .asset_scraper.company_indicators.valuation_indicators import register_routes as attach_valuation_indicators
    from .asset_scraper.company_indicators.debt_indicators import register_routes as attach_debt_indicators
    from .asset_scraper.company_indicators.efficiency_indicators import register_routes as attach_efficiency_indicators

    #Add route
    attach_current_price(api)
    attach_theoretical_portifolio(api)
    attach_valuation_indicators(api)
    attach_debt_indicators(api)
    attach_efficiency_indicators(api)


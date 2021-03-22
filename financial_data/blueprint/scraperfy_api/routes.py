def register_routes(api):
    from .asset_scraper.current_price import register_routes as attach_current_price
    from .index_scraper.theoretical_portifolio import register_routes as attach_theoretical_portifolio

    #Add route
    attach_current_price(api)
    attach_theoretical_portifolio(api)

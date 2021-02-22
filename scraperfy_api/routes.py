def register_routes(api, app, root='api'):
    from scraperfy_api.asset_scraper.current_price import register_routes as attach_current_price

    #Add route
    attach_current_price(api, app)
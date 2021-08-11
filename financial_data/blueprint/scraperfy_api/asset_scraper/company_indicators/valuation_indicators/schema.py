from marshmallow import Schema, fields


class ValuationIndicatorsSchema(Schema):


    assetId = fields.Number(attribute='asset_id')
    assetSymbol = fields.String(attribute='asset_symbol')
    searchDate = fields.DateTime(attribute='search_date')
    dividendYield = fields.Float(attribute='dividend_yield')
    priceEarnings = fields.Float(attribute='price_earnings')
    pegRatio = fields.Float(attribute='peg_ratio')
    priceBookValue = fields.Float(attribute='price_book_value')
    evEbitda = fields.Float(attribute='ev_ebitda')
    evEbit = fields.Float(attribute='ev_ebit')
    priceEbitda = fields.Float(attribute='price_ebitda')
    priceEbit = fields.Float(attribute='price_ebit')
    bookValueShare = fields.Float(attribute='book_value_share')
    priceAsset = fields.Float(attribute='price_asset')
    earningsShare = fields.Float(attribute='earnings_share')
    pricesSalesRatio = fields.Float(attribute='prices_sales_ratio')
    pricesWorkingCapital = fields.Float(attribute='prices_working_capital')
    priceNetCurrentAssets = fields.Float(attribute='price_net_current_assets')


from marshmallow import Schema, fields


class ProfitabilityIndicatorsSchema(Schema):

    assetId = fields.Number(attribute='asset_id')
    assetSymbol = fields.String(attribute='asset_symbol')
    searchDate = fields.DateTime(attribute='search_date')
    returnOnEquity = fields.Float(attribute='return_on_equity')
    returnOnAssets = fields.Float(attribute='return_on_assets')
    returnOnInvestedCapital = fields.Float(attribute='return_on_invested_capital')
    assetTurnoverRatio = fields.Float(attribute='asset_turnover_ratio')


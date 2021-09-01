from marshmallow import Schema, fields

class EfficiencyIndicatorsSchema(Schema):

    assetId = fields.Number(attribute='asset_id')
    assetSymbol = fields.String(attribute='asset_symbol')
    searchDate = fields.DateTime(attribute='search_date')
    grossMargin = fields.Float(attribute='gross_margin')
    ebitdaMargin = fields.Float(attribute='ebitda_margin')
    ebitMargin = fields.Float(attribute='ebit_margin')
    netMargin = fields.Float(attribute='net_margin')


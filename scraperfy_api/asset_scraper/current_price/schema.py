from marshmallow import Schema, fields


class CurrentPriceSchema(Schema):
    '''CurrentPrice schema'''

    assetId = fields.Number(attribute='asset_id')
    assetSymbol = fields.String(attribute='asset_symbol')
    assetPrice = fields.Float(attribute='asset_price')
    assetOscilation = fields.Float(attribute='asset_oscilation')


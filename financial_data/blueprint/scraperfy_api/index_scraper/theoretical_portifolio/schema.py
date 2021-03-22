from marshmallow import Schema, fields


class TheoreticalPortifolioSchema(Schema):
    '''TheoreticalPortifolio schema'''

    index = fields.String(attribute='index')
    assetSymbol = fields.String(attribute='asset_symbol')
    assetName = fields.String(attribute='asset_name')
    assetType = fields.String(attribute='asset_type')
    theoreticalQuantity = fields.String(attribute='theoretical_quantity')
    percentageShare = fields.String(attribute='percentage_share')
    portifolioDate = fields.Date(attribute='portifolio_date')


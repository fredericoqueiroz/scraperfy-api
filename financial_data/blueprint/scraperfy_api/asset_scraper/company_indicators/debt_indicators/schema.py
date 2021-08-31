from marshmallow import Schema, fields

class DebtIndicatorsSchema(Schema):

    assetId = fields.Number(attribute='asset_id')
    assetSymbol = fields.String(attribute='asset_symbol')
    searchDate = fields.DateTime(attribute='search_date')
    debtNetWorth = fields.Float(attribute='debt_net_worth')
    debtEbitda = fields.Float(attribute='debt_ebitda')
    debtEbit = fields.Float(attribute='debt_ebit')
    netWorthAssets = fields.Float(attribute='net_worth_assets')
    liabilitiesAssets = fields.Float(attribute='liabilities_assets')
    currentLiquidity = fields.Float(attribute='current_liquidity')

from datetime import datetime
from typing import TypedDict

class EfficiencyIndicatorsInterface(TypedDict, total=False):
    asset_id: int
    asset_symbol: str
    search_date: datetime
    debt_net_worth: float
    debt_ebitda: float
    debt_ebit: float
    net_worth_assets: float
    liabilities_assets: float
    current_liquidity: float


from datetime import datetime
from typing import TypedDict


class ProfitabilityIndicatorsInterface(TypedDict, total=False):
    asset_id: int
    asset_symbol: str
    search_date: datetime
    return_on_equity: float
    return_on_assets: float
    return_on_invested_capital: float
    asset_turnover_ratio: float


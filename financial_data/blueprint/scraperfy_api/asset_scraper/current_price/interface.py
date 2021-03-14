from datetime import date
from typing import TypedDict


class CurrentPriceInterface(TypedDict, total=False):
    asset_id: int
    asset_symbol: str
    asset_price: float
    asset_oscilation: float
    search_date: date
    search_time: str


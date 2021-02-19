from typing import TypedDict

class CurrentPriceInterface(TypedDict, total=False):
    asset_id: int
    asset_symbol: str
    asset_price: float
    asset_oscilation: float


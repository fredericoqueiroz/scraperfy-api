from datetime import datetime
from typing import TypedDict


class ValuationIndicatorsInterface(TypedDict, total=False):
    asset_id: int
    asset_symbol: str
    search_date: datetime
    dividend_yield: float
    price_earnings: float
    peg_ratio: float
    price_book_value: float
    ev_ebitda: float
    ev_ebit: float
    price_ebitda: float
    price_ebit: float
    book_value_share: float
    price_asset: float
    earnings_share: float
    prices_sales_ratio: float
    prices_working_capital: float
    price_net_current_assets: float

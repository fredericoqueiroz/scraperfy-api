from datetime import date
from typing import TypedDict


class TheoreticalPortifolioInterface(TypedDict, total=False):
    index_symbol: str
    portifolio_date: date
    asset_symbol: str
    asset_name: str
    asset_type: str
    theoretical_quantity: str
    percentage_share: str


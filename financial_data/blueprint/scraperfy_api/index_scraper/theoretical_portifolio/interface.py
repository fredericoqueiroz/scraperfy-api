from datetime import date
from typing import TypedDict


class TheoreticalPortifolioInterface(TypedDict, total=False):
    index: str
    asset_symbol: str
    asset_name: str
    asset_type: str
    theoretical_quantity: str
    percentage_share: str
    portifolio_date: date


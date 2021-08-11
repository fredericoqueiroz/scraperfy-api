from financial_data.extensions.database import db
from sqlalchemy import Column, Float, Integer, String, DateTime

from .interface import ValuationIndicatorsInterface

class ValuationIndicators(db.Model):

    __tablename__ = 'valuation_indicators'

    asset_id = Column(Integer(), primary_key=True, autoincrement=True)
    asset_symbol = Column(String(10), primary_key=True, index=True)
    search_date = Column(DateTime())
    dividend_yield = Column(Float())
    price_earnings = Column(Float())
    peg_ratio = Column(Float())
    price_book_value = Column(Float())
    ev_ebitda = Column(Float())
    ev_ebit = Column(Float())
    price_ebitda = Column(Float())
    price_ebit = Column(Float())
    book_value_share = Column(Float())
    price_asset = Column(Float())
    earnings_share = Column(Float())
    prices_sales_ratio = Column(Float())
    prices_working_capital = Column(Float())
    price_net_current_assets = Column(Float())
    
    def __repr__(self):
        return '<AssetSymbol %r>' % self.asset_symbol

    def update(self, changes: ValuationIndicatorsInterface):
        for key, val in changes.items():
            if type(val) == str:
                val = val.upper()
            setattr(self, key, val)
        return self


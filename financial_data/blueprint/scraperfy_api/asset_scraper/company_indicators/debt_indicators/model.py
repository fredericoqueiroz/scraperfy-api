from financial_data.extensions.database import db
from sqlalchemy import Column, Float, Integer, String, DateTime

from .interface import DebtIndicatorsInterface

class DebtIndicators(db.Model):

    __tablename__ = 'debt_indicators'

    asset_id = Column(Integer(), primary_key=True, autoincrement=True)
    asset_symbol = Column(String(10), primary_key=True, index=True)
    search_date = Column(DateTime())
    debt_net_worth = Column(Float())
    debt_ebitda = Column(Float())
    debt_ebit = Column(Float())
    net_worth_assets = Column(Float())
    liabilities_assets = Column(Float())
    current_liquidity = Column(Float())

    def __repr__(self):
        return '<AssetSymbol %r>' % self.asset_symbol

    def update(self, changes: DebtIndicatorsInterface):
        for key, val in changes.items():
            if type(val) == str:
                val = val.upper()
            setattr(self, key, val)
        return self


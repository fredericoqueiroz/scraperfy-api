from financial_data.extensions.database import db
from sqlalchemy import Column, Float, Integer, String, DateTime


class ProfitabilityIndicators(db.Model):

    __tablename__ = 'profitability_indicators'

    asset_id = Column(Integer(), primary_key=True, autoincrement=True)
    asset_symbol = Column(String(10), primary_key=True, index=True)
    search_date = Column(DateTime())
    return_on_equity = Column(Float())
    return_on_assets = Column(Float())
    return_on_invested_capital = Column(Float())
    asset_turnover_ratio = Column(Float())

    def __repr__(self):
        return '<AssetSymbol %r>' % self.asset_symbol


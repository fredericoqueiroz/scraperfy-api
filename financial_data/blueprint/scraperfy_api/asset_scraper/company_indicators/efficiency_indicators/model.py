from financial_data.extensions.database import db
from sqlalchemy import Column, Float, Integer, String, DateTime

from .interface import EfficiencyIndicatorsInterface

class EfficiencyIndicators(db.Model):

    __tablename__ = 'efficiency_indicators'

    asset_id = Column(Integer(), primary_key=True, autoincrement=True)
    asset_symbol = Column(String(10), primary_key=True, index=True)
    search_date = Column(DateTime())
    gross_margin = Column(Float())
    ebitda_margin = Column(Float())
    ebit_margin = Column(Float())
    net_margin = Column(Float())

    def __repr__(self):
        return '<AssetSymbol %r>' % self.asset_symbol

    def update(self, changes: EfficiencyIndicatorsInterface):
        for key, val in changes.items():
            if type(val) == str:
                val = val.upper()
            setattr(self,key, val)
        return self


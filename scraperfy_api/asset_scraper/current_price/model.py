from app import db
from sqlalchemy import Column, Float, Integer, String

from .interface import CurrentPriceInterface


class CurrentPrice(db.Model):

    __tablename__ = 'current_price'

    asset_id = Column(Integer(), primary_key=True, autoincrement=True)
    asset_symbol = Column(String(10), primary_key=True)
    asset_price = Column(Float())
    asset_oscilation = Column(Float())
    #search_date = db.Column(db.Date)
    #search_time = db.Column(db.Time)

    def __repr__(self):
        return '<Asset %r>' % self.asset_symbol

    def update(self, changes: CurrentPriceInterface):
        for key, val in changes.items():
            if type(val) == str:
                val = val.upper()
            setattr(self, key, val)
        return self


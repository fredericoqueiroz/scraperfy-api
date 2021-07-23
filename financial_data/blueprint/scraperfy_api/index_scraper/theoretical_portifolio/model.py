from financial_data.extensions.database import db
from sqlalchemy import Column, Date, String

from .interface import TheoreticalPortifolioInterface

class TheoreticalPortifolio(db.Model):

    __tablename__ = 'theoretical_portifolio'

    index_symbol = Column(String(10), primary_key=True, index=True)
    portifolio_date = Column(Date(), primary_key=True, index=True)
    asset_symbol = Column(String(10), primary_key=True, index=True)
    asset_name = Column(String(20))
    asset_type = Column(String(20))
    theoretical_quantity = Column(String(32))
    percentage_share = Column(String(10))

    def __repr__(self):
        return '<IndexSymbol %r>' % self.index_symbol

    def update(self, changes: TheoreticalPortifolioInterface):
        for key, val in changes.items():
            if type(val) == str:
                val = val.upper()
            setattr(self, key, val)
        return self


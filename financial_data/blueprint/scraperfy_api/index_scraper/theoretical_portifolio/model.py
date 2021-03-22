from financial_data.extensions.database import db
from sqlalchemy import Column, Date, String

from .interface import TheoreticalPortifolioInterface

class TheoreticalPortifolio(db.Model):

    __tablename__ = 'theoretical_portifolio'

    index = Column(String(10), primary_key=True, index=True)
    asset_symbol = Column(String(10), primary_key=True, index=True)
    asset_name = Column(String(20))
    asset_type = Column(String(20))
    theoretical_quantity = Column(String(32))
    percentage_share = Column(String(10))
    portifolio_date = Column(Date())

    def __repr__(self):
        return '<Index %r>' % self.index

    def update(self, changes: TheoreticalPortifolioInterface):
        for key, val in changes.items():
            if type(val) == str:
                val = val.upper()
            setattr(self, key, val)
        return self


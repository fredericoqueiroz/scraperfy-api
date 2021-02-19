from enum import unique

from app import db


class CurrentPrice(db.Model):

    __tablename__ = 'current_price'

    asset_id = db.Column(db.Integer, primary_key=True)
    asset_symbol = db.Column(db.String(10), unique=True)
    asset_price = db.Column(db.Float)
    asset_oscilation = db.Column(db.Float)
    #search_date = db.Column(db.Date)
    #search_time = db.Column(db.Time)

    def __repr__(self):
        return '<Asset %r>' % self.asset_symbol


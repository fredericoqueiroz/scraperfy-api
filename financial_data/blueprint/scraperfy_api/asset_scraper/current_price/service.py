from typing import List

from financial_data.extensions.database import db

from .interface import CurrentPriceInterface
from .model import CurrentPrice


class CurrentPriceService:

    @staticmethod
    def get_all() -> List[CurrentPrice]:
        return CurrentPrice.query.all()

    @staticmethod
    def get_by_id(asset_id: int) -> CurrentPrice:
        return CurrentPrice.query.filter(CurrentPrice.asset_id == asset_id).first()
    
    @staticmethod
    def get_by_symbol(asset_symbol: str) -> CurrentPrice:
        return CurrentPrice.query.filter(CurrentPrice.asset_symbol == asset_symbol.upper()).first()
    
    @staticmethod
    def update(current_price: CurrentPrice, current_price_change: CurrentPriceInterface) -> CurrentPrice:
        current_price.update(current_price_change)
        db.session.commit()
        return current_price
    
    @staticmethod
    def delete_by_symbol(asset_symbol: str) -> List[str]:
        cp = CurrentPrice.query.filter(CurrentPrice.asset_symbol == asset_symbol.upper()).first()
        if not cp:
            return []
        db.session.delete(cp)
        db.session.commit()
        return [asset_symbol.upper()]
    
    @staticmethod
    def create(new_attrs: CurrentPriceInterface) -> CurrentPrice:
        new_cp = CurrentPrice(
                                asset_symbol=new_attrs['asset_symbol'].upper(),
                                asset_price=new_attrs['asset_price'],
                                asset_oscilation=new_attrs['asset_oscilation'],
                                search_date=new_attrs['search_date'],
                                search_time=new_attrs['search_time']
                            )
        
        db.session.add(new_cp)
        db.session.commit()

        return new_cp


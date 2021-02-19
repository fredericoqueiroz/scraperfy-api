from sqlalchemy.orm import query
from scraperfy_api.asset_scraper import current_price
from typing import List

from app import db

from .interface import CurrentPriceInterface
from .model import CurrentPrice

class CurrentPriceService:
    @staticmethod
    def get_all() -> List[CurrentPrice]:
        return CurrentPrice.query.all()

    @staticmethod
    def get_by_id(asset_id: int) -> CurrentPrice:
        return CurrentPrice.query.get(asset_id)
    
    @staticmethod
    def get_by_symbol(asset_symbol: str) -> CurrentPrice:
        return CurrentPrice.query.get(asset_symbol)
    
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
        return [asset_symbol]
    
    @staticmethod
    def create(new_attrs: CurrentPriceInterface) -> CurrentPrice:
        new_cp = CurrentPrice(asset_symbol=new_attrs['asset_symbol'],
                            asset_price=new_attrs['asset_price'],
                            asset_oscilation=new_attrs['asset_oscilation'])
        
        db.session.add(new_cp)
        db.session.commit()

        return new_cp


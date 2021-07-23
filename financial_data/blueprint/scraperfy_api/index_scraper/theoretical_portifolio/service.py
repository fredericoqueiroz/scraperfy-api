from datetime import datetime
from typing import List

from financial_data.extensions.database import db

from .interface import TheoreticalPortifolioInterface
from .model import TheoreticalPortifolio


class TheoreticalPortifolioService:

    @staticmethod
    def get_all() -> List[TheoreticalPortifolio]:
        return TheoreticalPortifolio.query.all()

    @staticmethod
    def get_by_index(index_symbol: str) -> List[TheoreticalPortifolio]:
        return TheoreticalPortifolio.query.filter(TheoreticalPortifolio.index_symbol == index_symbol.upper())

    @staticmethod
    def get_by_asset(asset_symbol: str) -> List[TheoreticalPortifolio]:
        return TheoreticalPortifolio.query.filter(TheoreticalPortifolio.asset_symbol == asset_symbol.upper())

    @staticmethod
    def get_by_date(portifolio_date: str) -> List[TheoreticalPortifolio]:
        return TheoreticalPortifolio.query.filter(TheoreticalPortifolio.portifolio_date == portifolio_date)

    @staticmethod
    def get_by_index_and_asset(index_symbol: str, asset_symbol: str) -> TheoreticalPortifolio:
        return TheoreticalPortifolio.query.filter(
                TheoreticalPortifolio.index_symbol == index_symbol.upper(),
                TheoreticalPortifolio.asset_symbol == asset_symbol.upper())

    @staticmethod
    def get_by_index_and_asset_and_date(index_symbol: str, asset_symbol: str, portifolio_date: datetime):
        return TheoreticalPortifolio.query.filter(
                TheoreticalPortifolio.index_symbol == index_symbol.upper(),
                TheoreticalPortifolio.asset_symbol == asset_symbol.upper(),
                TheoreticalPortifolio.portifolio_date == portifolio_date)

    @staticmethod
    def update(tp: TheoreticalPortifolio, tp_change: TheoreticalPortifolioInterface) -> TheoreticalPortifolio:
        tp.update(tp_change)
        db.session.commit()
        return tp
    
    @staticmethod
    def delete_by_index(index_symbol: str) -> List[str]:
        tp = TheoreticalPortifolio.query.filter(TheoreticalPortifolio.index == index_symbol.upper()).first()
        if not tp:
            return []
        db.session.delete(tp)
        db.session.commit()
        return [index_symbol.upper()]
    
    @staticmethod
    def delete_by_symbol(asset_symbol: str) -> List[str]:
        tp = TheoreticalPortifolio.query.filter(TheoreticalPortifolio.asset_symbol == asset_symbol.upper()).first()
        if not tp:
            return []
        db.session.delete(tp)
        db.session.commit()
        return [asset_symbol.upper()]

    @staticmethod
    def delete_by_index_and_asset(index_symbol: str, asset_symbol: str) -> List[str]:
        tp = TheoreticalPortifolio.query.filter(
                TheoreticalPortifolio.index_symbol == index_symbol.upper(),
                TheoreticalPortifolio.asset_symbol == asset_symbol.upper()
            ).first()
        if not tp:
            return []
        db.session.delete(tp)
        db.session.commit()
        return [index_symbol.upper(), asset_symbol.upper()]

    @staticmethod
    def create(new_attrs: TheoreticalPortifolioInterface) -> TheoreticalPortifolio:
        new_tp = TheoreticalPortifolio(
                                        index_symbol=new_attrs['index_symbol'].upper(),
                                        portifolio_date=new_attrs['portifolio_date'],
                                        asset_symbol=new_attrs['asset_symbol'].upper(),
                                        asset_name=new_attrs['asset_name'].upper(),
                                        asset_type=new_attrs['asset_type'].upper(),
                                        theoretical_quantity=new_attrs['theoretical_quantity'],
                                        percentage_share=new_attrs['percentage_share']
                                    )
        
        db.session.add(new_tp)
        db.session.commit()

        return new_tp


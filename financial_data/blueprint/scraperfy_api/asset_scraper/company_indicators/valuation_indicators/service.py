from typing import List

from financial_data.extensions.database import db

from .interface import ValuationIndicatorsInterface
from .model import ValuationIndicators


class ValuationIndicatorsService:

    @staticmethod
    def get_all() -> List[ValuationIndicators]:
        return ValuationIndicators.query.all()
    
    @staticmethod
    def get_by_id(asset_id: int) -> ValuationIndicators:
        return ValuationIndicators.query.filter(ValuationIndicators.asset_id == asset_id).first()
    
    @staticmethod
    def get_by_symbol(asset_symbol: str) -> ValuationIndicators:
        return ValuationIndicators.query.filter(ValuationIndicators.asset_symbol == asset_symbol.upper()).first()
    
    @staticmethod
    def update(vi: ValuationIndicators, vi_changes: ValuationIndicatorsInterface) -> ValuationIndicators:
        vi.update(vi_changes)
        db.session.commit()
        return vi
    
    @staticmethod
    def delete_by_symbol(asset_symbol: str) -> List[str]:
        vi = ValuationIndicators.query.filter(ValuationIndicators.asset_symbol == asset_symbol.upper()).first()
        if not vi:
            return []
        db.session.delete(vi)
        db.session.commit()
        return asset_symbol.upper()
    
    @staticmethod
    def create(new_attrs: ValuationIndicatorsInterface) -> ValuationIndicators:
        new_vi = ValuationIndicators(
            asset_symbol=new_attrs['asset_symbol'].upper(),
            search_date=new_attrs['search_date'],
            dividend_yield=new_attrs['dividend_yield'],
            price_earnings=new_attrs['price_earnings'],
            peg_ratio=new_attrs['peg_ratio'],
            price_book_value=new_attrs['price_book_value'],
            ev_ebitda=new_attrs['ev_ebitda'],
            ev_ebit=new_attrs['ev_ebit'],
            price_ebitda=new_attrs['price_ebitda'],
            price_ebit=new_attrs['price_ebit'],
            book_value_share=new_attrs['book_value_share'],
            price_asset=new_attrs['price_asset'],
            earnings_share=new_attrs['earnings_share'],
            prices_sales_ratio=new_attrs['prices_sales_ratio'],
            prices_working_capital=new_attrs['prices_working_capital'],
            price_net_current_assets=new_attrs['price_net_current_assets']
        )

        db.session.add(new_vi)
        db.session.commit()

        return new_vi


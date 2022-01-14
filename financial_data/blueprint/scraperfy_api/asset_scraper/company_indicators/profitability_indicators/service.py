from typing import List

from financial_data.extensions.database import db

from .interface import ProfitabilityIndicatorsInterface
from .model import ProfitabilityIndicators


class ProfitabilityIndicatorsService:

    @staticmethod
    def get_all() -> List[ProfitabilityIndicators]:
        return ProfitabilityIndicators.query.all()
    
    @staticmethod
    def get_by_id(asset_id: int) -> ProfitabilityIndicators:
        return ProfitabilityIndicators.query.filter(ProfitabilityIndicators.asset_id == asset_id).first()
    
    @staticmethod
    def get_by_symbol(asset_symbol: str) -> ProfitabilityIndicators:
        return ProfitabilityIndicators.query.filter(ProfitabilityIndicators.asset_symbol == asset_symbol.upper()).first()
    
    @staticmethod
    def update(pi: ProfitabilityIndicators, pi_changes: ProfitabilityIndicatorsInterface) -> ProfitabilityIndicators:
        pi.update(pi_changes)
        db.session.commit()
        return pi

    @staticmethod
    def delete_by_symbol(asset_symbol: str) -> List[str]:
        pi = ProfitabilityIndicators.query.filter(ProfitabilityIndicators.asset_symbol == asset_symbol.upper()).first()
        if not pi:
            return []
        db.session.delete(pi)
        db.session.commit()
        return asset_symbol.upper()

    @staticmethod
    def create(new_attrs: ProfitabilityIndicatorsInterface) -> ProfitabilityIndicators:
        new_pi = ProfitabilityIndicators(
            asset_symbol=new_attrs['asset_symbol'],
            search_date=new_attrs['search_date'],
            return_on_equity=new_attrs['return_on_equity'],
            return_on_assets=new_attrs['return_on_assets'],
            return_on_invested_capital=new_attrs['return_on_invested_capital'],
            asset_turnover_ratio=new_attrs['asset_turnover_ratio']
        )

        db.session.add(new_pi)
        db.session.commit()

        return new_pi


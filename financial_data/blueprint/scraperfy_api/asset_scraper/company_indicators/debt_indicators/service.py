from typing import List

from financial_data.extensions.database import db

from .interface import DebtIndicatorsInterface
from .model import DebtIndicators


class DebtIndicatorsService:

    @staticmethod
    def get_all() -> List[DebtIndicators]:
        return DebtIndicators.query.all()

    @staticmethod
    def get_by_id(asset_id: int) -> DebtIndicators:
        return DebtIndicators.query.filter(DebtIndicators.asset_id == asset_id).first()
    
    @staticmethod
    def get_by_symbol(asset_symbol: str) -> DebtIndicators:
        return DebtIndicators.query.filter(DebtIndicators.asset_symbol == asset_symbol.upper()).first()

    @staticmethod
    def update(di: DebtIndicators, di_changes: DebtIndicatorsInterface) -> DebtIndicators:
        di.update(di_changes)
        db.session.commit()
        return di

    @staticmethod
    def delete_by_symbol(asset_symbol: str) -> List[str]:
        di = DebtIndicators.query.filter(DebtIndicators.asset_symbol == asset_symbol.upper()).first()
        if not di:
            return []
        db.session.delete(di)
        db.session.commit()
        return asset_symbol.upper()

    @staticmethod
    def create(new_attrs: DebtIndicatorsInterface) -> DebtIndicators:
        new_di = DebtIndicators(
            asset_symbol=new_attrs['asset_symbol'].upper(),
            search_date=new_attrs['search_date'],
            debt_net_worth=new_attrs['debt_net_worth'],
            debt_ebitda=new_attrs['debt_ebitda'],
            debt_ebit=new_attrs['debt_ebit'],
            net_worth_assets=new_attrs['net_worth_assets'],
            liabilities_assets=new_attrs['liabilities_assets'],
            current_liquidity=new_attrs['current_liquidity']
        )

        db.session.add(new_di)
        db.session.commit()

        return new_di


from typing import List

from financial_data.extensions.database import db

from .interface import EfficiencyIndicatorsInterface
from .model import EfficiencyIndicators


class EfficiencyIndicatorsService:

    @staticmethod
    def get_all() -> List[EfficiencyIndicators]:
        return EfficiencyIndicators.query.all()
    
    @staticmethod
    def get_by_id(asset_id: int) -> EfficiencyIndicators:
        return EfficiencyIndicators.query.filter(EfficiencyIndicators.asset_id == asset_id).first()
    
    @staticmethod
    def get_by_symbol(asset_symbol: str) -> EfficiencyIndicators:
        return EfficiencyIndicators.query.filter(EfficiencyIndicators.asset_symbol == asset_symbol.upper()).first()

    @staticmethod
    def update(ei: EfficiencyIndicators, ei_changes: EfficiencyIndicatorsInterface) -> EfficiencyIndicators:
        ei.update(ei_changes)
        db.session.commit()
        return ei

    @staticmethod
    def delete_by_symbol(asset_symbol: str) -> List[str]:
        ei = EfficiencyIndicators.query.filter(EfficiencyIndicators.asset_symbol == asset_symbol.upper()).first()
        if not ei:
            return []
        db.session.delete(ei)
        db.session.commit()
        return asset_symbol.upper()

    @staticmethod
    def create(new_attrs: EfficiencyIndicatorsInterface) -> EfficiencyIndicators:
        new_ei = EfficiencyIndicators(
            asset_symbol=new_attrs['asset_symbol'].upper(),
            search_date=new_attrs['search_date'],
            gross_margin=new_attrs['gross_margin'],
            ebitda_margin=new_attrs['ebitda_margin'],
            ebit_margin=new_attrs['ebit_margin'],
            net_margin=new_attrs['net_margin']
        )

        db.session.add(new_ei)
        db.session.commit()

        return new_ei



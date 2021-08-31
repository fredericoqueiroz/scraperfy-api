from typing import List

from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from .interface import DebtIndicatorsInterface
from .model import DebtIndicators
from .schema import DebtIndicatorsSchema
from .service import DebtIndicatorsService

api = Namespace('DebtIndicators', description='Companies Debt Indicators')

@api.route('/')
class DebtIndicatorsResource(Resource):

    @responds(schema=DebtIndicatorsSchema(many=True))
    def get(self) -> List[DebtIndicators]:
        '''Get all companies debt indicators'''
        return DebtIndicatorsService.get_all()

    @accepts(schema=DebtIndicatorsSchema, api=api)
    @responds(schema=DebtIndicatorsSchema)
    def post(self) -> DebtIndicators:
        '''Create a single company indicator'''
        return DebtIndicatorsService.create(request.parsed_obj)


@api.route('/<string:assetSymbol>')
@api.param('assetSymbol', 'Asset Symbol')
class DebtIndicatorsSymbolResource(Resource):

    @responds(schema=DebtIndicatorsSchema)
    def get(self, assetSymbol: str) -> DebtIndicators:
        '''Get single company indicator'''
        return DebtIndicatorsService.get_by_symbol(assetSymbol)

    def delete(self, assetSymbol: str) -> Response:
        '''Delete single company indicator'''
        from flask import jsonify

        symbol = DebtIndicatorsService.delete_by_symbol(assetSymbol)
        return jsonify(dict(status='Success', symbol=symbol))
    
    @accepts(schema=DebtIndicatorsSchema, api=api)
    @responds(schema=DebtIndicatorsSchema)
    def put(self, assetSymbol: str) -> DebtIndicators:
        '''Update single company indicator'''

        changes: DebtIndicatorsInterface = request.parsed_obj
        di = DebtIndicatorsService.get_by_symbol(assetSymbol)
        return DebtIndicatorsService.update(di, changes)


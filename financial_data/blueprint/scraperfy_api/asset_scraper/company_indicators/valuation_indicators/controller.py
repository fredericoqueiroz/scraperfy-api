from typing import List

from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from .interface import ValuationIndicatorsInterface
from .model import ValuationIndicators
from .schema import ValuationIndicatorsSchema
from .service import ValuationIndicatorsService

api = Namespace('ValuationIndicators', description='Companies Valuantion Indicators')

@api.route('/')
class ValuationIndicatorsResource(Resource):

    @responds(schema=ValuationIndicatorsSchema(many=True))
    def get(self) -> List[ValuationIndicators]:
        '''Get all companies valuation indicators'''
        return ValuationIndicatorsService.get_all()
    
    @accepts(schema=ValuationIndicatorsSchema, api=api)
    @responds(schema=ValuationIndicatorsSchema)
    def post(self) -> ValuationIndicators:
        '''Create a single company indicator'''
        return ValuationIndicatorsService.create(request.parsed_obj)


@api.route('/<string:assetSymbol>')
@api.param('assetSymbol', 'Asset Symbol')
class ValuationIndicatorsSymbolResource(Resource):

    @responds(schema=ValuationIndicatorsSchema)
    def get(self, assetSymbol: str) -> ValuationIndicators:
        '''Get single company indicator'''
        return ValuationIndicatorsService.get_by_symbol(assetSymbol)
    
    def delete(self, assetSymbol: str) -> Response:
        '''Delete single company indicator'''
        from flask import jsonify

        symbol = ValuationIndicatorsService.delete_by_symbol(assetSymbol)
        return jsonify(dict(status='Success', symbol=symbol))

    @accepts(schema=ValuationIndicatorsSchema, api=api)
    @responds(schema=ValuationIndicatorsSchema)
    def put(self, assetSymbol: str) -> ValuationIndicators:
        '''Update single company indicator'''

        changes: ValuationIndicatorsInterface = request.parsed_obj
        vi = ValuationIndicatorsService.get_by_symbol(assetSymbol)
        return ValuationIndicatorsService.update(vi, changes)


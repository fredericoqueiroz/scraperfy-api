from typing import List

from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from .interface import CurrentPriceInterface
from .model import CurrentPrice
from .schema import CurrentPriceSchema
from .service import CurrentPriceService

api = Namespace('CurrentPrice', description='Current intraday asset prices')

@api.route('/')
class CurrentePriceResource(Resource):

    @responds(schema=CurrentPriceSchema(many=True))
    def get(self) -> List[CurrentPrice]:
        '''Get all Prices'''
        return CurrentPriceService.get_all()

    @accepts(schema=CurrentPriceSchema, api=api)
    @responds(schema=CurrentPriceSchema)
    def post(self) -> CurrentPrice:
        '''Create a single Price'''
        return CurrentPriceService.create(request.parsed_obj)


@api.route('/<string:assetSymbol>')
@api.param('assetSymbol', 'Asset Symbol')
class CurrentPriceSymbolResource(Resource):

    @responds(schema=CurrentPriceSchema)
    def get(self, assetSymbol: str) -> CurrentPrice:
        '''Get single Asset'''
        return CurrentPriceService.get_by_symbol(assetSymbol)
    
    def delete(self, assetSymbol: str) -> Response:
        '''Delete single Asset'''
        from flask import jsonify

        symbol = CurrentPriceService.delete_by_symbol(assetSymbol)
        return jsonify(dict(status='Success', symbol=symbol))

    @accepts(schema=CurrentPriceSchema, api=api)
    @responds(schema=CurrentPriceSchema)
    def put(self, assetSymbol: str) -> CurrentPrice:
        '''Update single Asset'''

        changes: CurrentPriceInterface = request.parsed_obj
        CurrentPrice = CurrentPriceService.get_by_symbol(assetSymbol)
        return CurrentPriceService.update(CurrentPrice, changes)

from typing import List

from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from .interface import TheoreticalPortifolioInterface
from .model import TheoreticalPortifolio
from .schema import TheoreticalPortifolioSchema
from .service import TheoreticalPortifolioService

api = Namespace('TheoreticalPortifolio', description='Index daily theoretical portifolio')

@api.route('/')
class TheoreticalPortifolioResource(Resource):

    @responds(schema=TheoreticalPortifolioSchema(many=True))
    def get(self) -> List[TheoreticalPortifolio]:
        '''Get all assets from the portifolio table'''
        return TheoreticalPortifolioService.get_all()
    
    @accepts(schema=TheoreticalPortifolioSchema, api=api)
    @responds(schema=TheoreticalPortifolioSchema)
    def post(self) -> TheoreticalPortifolio:
        '''Create a single asset in a portifolio'''
        return TheoreticalPortifolioService.create(request.parsed_obj)

@api.route('/<string:indexSymbol>')
@api.param('indexSymbol', 'Index symbol')
class TheoreticalPortifolioIndexResouce(Resource):

    @responds(schema=TheoreticalPortifolioSchema)
    def get(self, indexSymbol: str) -> List[TheoreticalPortifolio]:
        '''Get all assets in a portifolio'''
        return TheoreticalPortifolioService.get_by_index(indexSymbol)
    
    def delete(self, indexSymbol: str) -> Response:
        '''Delete all assets in a portifolio'''
        from flask import jsonify

        idx = TheoreticalPortifolioService.delete_by_index(indexSymbol)
        return jsonify(dict(status='Success', indexSymbol=idx))

@api.route('/<string:indexSymbol>/<string:assetSymbol>')
@api.param('indexSymbol', 'Index symbol')
@api.param('assetSymbol', 'Asset Symbol')
class TheoreticalPortifolioIndexSymbolResource(Resource):

    @responds(schema=TheoreticalPortifolioSchema)
    def get(self, indexSymbol: str, assetSymbol: str) -> TheoreticalPortifolio:
        '''Get a single Asset from a Index'''
        return TheoreticalPortifolioService.get_by_index_and_asset(indexSymbol, assetSymbol)
    
    def delete(self, indexSymbol: str, assetSymbol: str) -> Response:
        '''Delete a single Asset from a Index'''
        from flask import jsonify

        [idx, asset] = TheoreticalPortifolioService.delete_by_index_and_asset(indexSymbol, assetSymbol)
        return jsonify(dict(status='Success', indexSymbol=idx, assetSymbol=asset))

    @accepts(schema=TheoreticalPortifolioSchema, api=api)
    @responds(schema=TheoreticalPortifolioSchema)
    def put(self, indexSymbol: str, assetSymbol: str) -> TheoreticalPortifolio:
        '''Update a single Asset from a Index'''

        changes: TheoreticalPortifolioInterface = request.parsed_obj
        tp = TheoreticalPortifolioService.get_by_index_and_asset(indexSymbol, assetSymbol)
        return TheoreticalPortifolioService.update(tp, changes)


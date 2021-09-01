from typing import List

from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from marshmallow import schema

from .interface import EfficiencyIndicatorsInterface
from .model import EfficiencyIndicators
from .schema import EfficiencyIndicatorsSchema
from .service import EfficiencyIndicatorsService

api = Namespace('EfficiencyIndicators', description='Companies Efficiency Indicators')

@api.route('/')
class EfficiencyIndicatorsResource(Resource):

    @responds(schema=EfficiencyIndicatorsSchema(many=True))
    def get(self) -> List[EfficiencyIndicators]:
        '''Get all companies debt indicators'''
        return EfficiencyIndicatorsService.get_all()
    
    @accepts(schema=EfficiencyIndicatorsSchema, api=api)
    @responds(schema=EfficiencyIndicatorsSchema)
    def post(self) -> EfficiencyIndicators:
        '''Create a single company indicator'''
        return EfficiencyIndicatorsService.create(request.parsed_obj)

@api.route('/<string:assetSymbol>')
@api.param('assetSymbol', 'Asset Symbol')
class EfficiencyIndicatorsSymbolResource(Resource):

    @responds(schema=EfficiencyIndicatorsSchema)
    def get(self, assetSymbol: str) -> EfficiencyIndicators:
        '''Get single company indicator'''
        return EfficiencyIndicatorsService.get_by_symbol(assetSymbol)

    def delete(self, assetSymbol: str) -> Response:
        '''Delete single company indicator'''
        from flask import jsonify

        symbol = EfficiencyIndicatorsService.delete_by_symbol(assetSymbol)
        return jsonify(dict(status='Success', symbol=symbol))
    
    @accepts(schema=EfficiencyIndicatorsSchema, api=api)
    @responds(schema=EfficiencyIndicatorsSchema)
    def put(self, assetSymbol: str) -> EfficiencyIndicators:
        '''Update single company indicator'''

        changes: EfficiencyIndicatorsInterface = request.parsed_obj
        ei = EfficiencyIndicatorsService.get_by_symbol(assetSymbol)
        return EfficiencyIndicatorsService.update(ei, changes)


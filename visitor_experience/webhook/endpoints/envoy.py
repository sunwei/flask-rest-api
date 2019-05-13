import logging
from http import HTTPStatus

from flask import request
from flask_restplus import Resource
from visitor_experience.serializers import envoy_callback
from visitor_experience.domain.visitor import sign_in
from visitor_experience.webhook.endpoints import ns

log = logging.getLogger(__name__)


@ns.route('/')
class EnvoyCallback(Resource):

    @ns.response(HTTPStatus.CREATED, 'Envoy callback received.')
    @ns.expect(envoy_callback)
    def post(self):
        """
        Envoy callback received
        """
        data = request.json
        sign_in(data)
        return {'message': 'Envoy callback received.'}, HTTPStatus.CREATED

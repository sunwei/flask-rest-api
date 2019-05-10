import logging

from flask import request
from flask_restplus import Resource
from visitor_experience.restplus import api
from visitor_experience.serializers import envoy_callback
from visitor_experience.domain.visitor import sign_in

log = logging.getLogger(__name__)
ns = api.namespace('webhook/envoy', description='Webhook listen to Envoy callback')


@ns.route('/')
class EnvoyCallback(Resource):

    @api.response(201, 'Envoy callback received.')
    @api.expect(envoy_callback)
    def post(self):
        """
        Envoy callback received
        """
        data = request.json
        sign_in(data)
        return None, 201

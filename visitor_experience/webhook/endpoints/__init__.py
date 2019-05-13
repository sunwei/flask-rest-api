from flask_restplus import Namespace

ns = Namespace('webhook/envoy', description='Webhook listen to Envoy callback')

from . import envoy

from flask_restplus import fields
from visitor_experience.restplus import api

envoy_callback = api.model('Envoy callback', {
    'api_key': fields.String(required=True, description='Envoy api key'),
    'timestamp': fields.String(required=True, description='Callback timestamp'),
    'token': fields.String(required=True, description='Callback token'),
    'signature': fields.String(required=True, description='Callback signature')
})


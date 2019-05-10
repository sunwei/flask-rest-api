from flask_restplus import fields
from visitor_experience.restplus import api

envoy_callback = api.model('Envoy callback', {
    'token': fields.String(required=True, description='Callback token'),
})


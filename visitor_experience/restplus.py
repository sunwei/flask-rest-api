import logging

from flask_restplus import Api
from visitor_experience import settings


log = logging.getLogger(__name__)


api = Api(version='1.0', title='Flask REST API',
          description='A simple Flask RestPlus API')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
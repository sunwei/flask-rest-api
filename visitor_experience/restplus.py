import logging
from http import HTTPStatus

from flask import current_app
from flask_restplus import Api

log = logging.getLogger(__name__)


api = Api(version='1.0', title='Flask REST API',
          description='A simple Flask RestPlus API')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not current_app.config['DEBUG']:
        return {'message': message}, HTTPStatus.SERVICE_UNAVAILABLE

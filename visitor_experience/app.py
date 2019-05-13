import logging.config

import os
from flask import Flask, Blueprint

from visitor_experience.config import config
from visitor_experience.restplus import api
from visitor_experience.webhook.endpoints.envoy import ns as envoy_webhook_namespace


def create_app(config_name):
    flask_app = Flask(__name__)

    configure_app(flask_app, config_name)
    initialize_app(flask_app)

    return flask_app


def configure_app(flask_app, config_name):
    flask_app.config.from_object(config[config_name])


def initialize_app(flask_app):
    configure_log()

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(envoy_webhook_namespace)
    flask_app.register_blueprint(blueprint)


def configure_log():
    logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
    logging.config.fileConfig(logging_conf_path)


if __name__ == "__main__":
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    log = logging.getLogger(__name__)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run()

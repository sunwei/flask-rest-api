import logging
import os
import sys

from flask import Flask, jsonify, request

from tdp.foundation.auth import AUTH, verify_password
from tdp.blueprint import Subject
from tdp.blueprint.access_token_controller import ACCESS_TOKEN
from tdp.blueprint.certificate_controller import CERTIFICATE
from tdp.blueprint.cluster_controller import CLUSTER
from tdp.blueprint.island_controller import ISLAND
from tdp.blueprint.log_controller import LOG
from tdp.blueprint.pipeline_controller import PIPELINE
from tdp.blueprint.planet_controller import PLANET
from tdp.blueprint.portal_controller import PORTAL
from tdp.blueprint.response_helper import response
from tdp.blueprint.secret_controller import SECRET
from tdp.blueprint.storage_controller import STORAGE
from tdp.blueprint.user_controller import USERS
from tdp.config import BaseConfig
from tdp.constant.http_code import HttpCode
from tdp.exception.error_hanler import register_error_handlers
from tdp.extending.async_task import logging_proc
from tdp.foundation.logger import config_logging
from tdp.swagger import config_swagger

DEFAULT_BLUEPRINTS = [
    USERS,
    PLANET,
    ISLAND,
    PORTAL,
    LOG,
    SECRET,
    STORAGE,
    ACCESS_TOKEN,
    CLUSTER,
    PIPELINE,
    CERTIFICATE
]


def create_app():
    config_logging()

    app = Flask(__name__)
    runtime_config_setup(app)
    logging_proc()
    config_basic_check(app)
    register_blueprints(app)
    register_error_handlers(app)
    config_swagger(app)

    return app


def runtime_config_setup(app):
    runtime = os.getenv('FLASK_RUNTIME_ENV')
    if runtime == 'dev':
        app.config.from_object('tdp.config.DevelopmentConfig')
    elif runtime == 'qa':
        app.config.from_object('tdp.config.QaConfig')
    elif runtime == 'staging':
        app.config.from_object('tdp.config.StagingConfig')
    else:
        app.config.from_object('tdp.config.ProductionConfig')


def register_blueprints(app):
    for blueprint in DEFAULT_BLUEPRINTS:
        app.register_blueprint(blueprint)


def config_basic_check(app):
    @app.route('/health')
    def _health():
        health_status = {'code': HttpCode.OK.value, 'status': 'OK'}
        return jsonify(health_status)

    @app.route('/', methods=['POST'])
    def _check_auth():
        username = request.get_json()['username']
        password = request.get_json()['password']
        http_code = HttpCode.OK if verify_password(username, password) else HttpCode.UNAUTHORIZED
        return response(code=http_code)

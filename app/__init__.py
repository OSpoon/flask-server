#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: __init__.py.py
@time: 2019/11/25 15:57
@desc:
'''
from flask import Flask

from app.resource import ShortUrl, Working
from app.security import security
from app.config import config
from app.utils import errors


from flask_restful import Api
from flask_redis import FlaskRedis
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

from app.utils.common import log_exception

api = Api()
redis_client = FlaskRedis()
swagger = Swagger()
db = SQLAlchemy()


def init_api_plugin(app):
    api.add_resource(ShortUrl, '/surl', endpoint="surl_post")
    api.add_resource(ShortUrl, '/surl/<id>', endpoint="surl_get")
    api.add_resource(Working, '/work/<date>', endpoint="work_get")
    api.catch_all_404s = True
    api.errors = errors
    api.init_app(app)


def init_redis_plugin(app):
    redis_client.init_app(app, decode_responses=True)


def init_swagger_plugin(app):
    swagger.init_app(app)


def init_db_plugin(app):
    db.init_app(app)


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(security[config_name])
    app.config.from_object(config[config_name])

    init_api_plugin(app)
    init_redis_plugin(app)
    init_swagger_plugin(app)
    init_db_plugin(app)

    register_blueprint(app)

    from flask import got_request_exception
    got_request_exception.connect(log_exception, app)

    return app
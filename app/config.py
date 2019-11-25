#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: config.py
@time: 2019/11/25 15:58
@desc:
'''

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    HOST = '0.0.0.0'
    PORT = '4567'

    SWAGGER = {
        'title': 'ShortUrl Server API',
        'version':'1.0.0',
        'uiversion': 2
    }

    SQLALCHEMY_DATABASE_URI = 'sqlite:///date.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
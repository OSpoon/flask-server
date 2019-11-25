#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: security.py
@time: 2019/11/25 15:58
@desc:
'''

class Security:

    REDIS_URL = "redis://:@localhost:6379/0"

    @staticmethod
    def init_app(app):
        pass


class Development(Security):

    REDIS_URL = "redis://:@localhost:6379/1"

    pass


class Production(Security):

    REDIS_URL = "redis://:@localhost:6379/1"

    pass


security = {
    'development': Development,
    'production': Production,
    'default': Security
}
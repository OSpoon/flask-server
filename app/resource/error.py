#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: errors.py
@time: 2019/11/22 17:06
@desc:
'''

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
    'AttributeError': {
        'message': "Incorrect incoming parameters.",
        'status': 500,
        'extra': "Any extra information you want.",
    },
}
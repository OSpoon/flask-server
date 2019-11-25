#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: __init__.py.py
@time: 2019/11/14 10:55
@desc:
'''
from flask import Blueprint

web = Blueprint('web', __name__, url_prefix='/')

from . import views, error
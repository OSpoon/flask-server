#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: errors.py
@time: 2019/11/14 10:56
@desc:
'''

from flask import render_template
from . import web


@web.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@web.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
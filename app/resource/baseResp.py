#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: baseResp.py
@time: 2019/11/22 15:18
@desc:
'''


class BaseResp:

    def __init__(self, code , status, message, resp):
        self.code = code
        self.status = status
        self.message = message
        self.resp = resp
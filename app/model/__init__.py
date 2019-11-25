#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: __init__.py.py
@time: 2019/11/25 16:12
@desc:
'''

from app import db


class DateModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    isWork = db.Column(db.Boolean, default=True)

    def __init__(self, date):
        self.date = date

    def __init__(self, date, isWork):
        self.date = date
        self.isWork = isWork


    def __repr__(self):
        return '<Date %r>' % self.date
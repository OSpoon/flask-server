#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: views.py
@time: 2019/11/14 10:56
@desc:
'''
import datetime
import json

from flask import render_template, request

from app.model import DateModel
from app.web import web


@web.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@web.route('/iswork', methods=['GET', 'POST'])
def iswork():
    dateObj = DateModel.query.filter_by(date=request.args.get('date')).first()
    print(dateObj.date, dateObj.isWork)
    return "请安心上班" if dateObj.isWork else "好好休息吧" 
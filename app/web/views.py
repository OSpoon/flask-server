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

import requests
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


@web.route('/token', methods=['GET'])
def token():
    '''
    27_Y1zLsNMmba1e7gHxkipKpdRhJu90u0rAqgqVmqeuYyhCX_FRrW9AzRKw111ta7JYMVufswntaDZ8t20xT3pqTTZuL7ftkr5owIg0TfOnwCSLft2ufKc7hq0EIYzxskI95amQNIRsKwul-G5-NHKbAHASMP
    :return:
    '''
    appID = 'wxa933302f1681f80a'
    appsecret = 'e30afdbf3e5f1f20168c5b82689c3129'
    return requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appID+'&secret='+appsecret).content


@web.route('/callbackip', methods=['GET'])
def callbackIP():
    access_token = '27_Y1zLsNMmba1e7gHxkipKpdRhJu90u0rAqgqVmqeuYyhCX_FRrW9AzRKw111ta7JYMVufswntaDZ8t20xT3pqTTZuL7ftkr5owIg0TfOnwCSLft2ufKc7hq0EIYzxskI95amQNIRsKwul-G5-NHKbAHASMP'
    return requests.get('https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token='+access_token).content


@web.route('/check', methods=['GET'])
def check():
    data = {
        'action': "all",
        'check_operator': "DEFAULT"
    }
    return requests.post('https://api.weixin.qq.com/cgi-bin/callback/check?access_token=27_evTTyyPKyRCPQX81b-qwaQbaE-BU4mLVqVzUU79wfsLJusE-_3i_NyvI-jCGy9NcaABk3gJh2aOLaNlE0HVhIHdjPInC3ummy7deKi1WBbGCU1wanDEK8QcfqFrctkIOEO2E5zX0XdQBj_ZTDTNdAAAIYS',data=data).content
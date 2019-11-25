#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: manage.py
@time: 2019/11/25 15:57
@desc:
'''
import datetime
from http.client import HTTPException

from app import create_app, db
from flask_script import Manager, Shell, Server

from app.model import DateModel
from app.utils.api_exception import APIException
from app.utils.common import getAllDayPerYear
from app.utils.errors import ServerError

app = create_app('default')
manager = Manager(app)


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


@manager.command
def create_data():
    print("create_data start")
    all_date_list = getAllDayPerYear("2020")
    for date in all_date_list:
        print('插入 : ', date)
        now_date = datetime.datetime.strptime(date,"%Y-%m-%d")
        if now_date.weekday() == 5 or now_date.weekday() == 6:
            db.session.add(DateModel(now_date, False))
        else:
            db.session.add(DateModel(now_date, True))
        db.session.commit()
    print("create_data end")


def make_shell_context():
    return dict(app=app, db=db, DateModel=DateModel)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(use_debugger=True))


if __name__ == '__main__':
    manager.run()
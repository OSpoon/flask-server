#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: __init__.py.py
@time: 2019/11/13 16:00
@desc:
'''

from flasgger import swag_from
from flask_restful import Resource, abort, reqparse, fields, marshal_with

from app.resource.baseResp import BaseResp
from app.utils.errors import ParameterException


def abort_if_todo_doesnt_exist(id):
    from app import redis_client
    if id not in redis_client.keys():
        abort(404, message="surl {} doesn't exist".format(id))


# 参数校验
from app.utils import short_url

parser = reqparse.RequestParser()
parser.add_argument('source', type=str, required=True, help="source cannot be blank!")

resource_fields = {
    'code': fields.Integer,
    'status': fields.Integer,
    'message': fields.String,
    'resp': fields.Raw
}


class ShortUrl(Resource):
    @swag_from('short_url_get.yml', endpoint='surl_get')
    def get(self, id):
        abort_if_todo_doesnt_exist(id)
        from app import redis_client
        response = redis_client.get(id)
        response = {
            "source": response
        }
        return BaseResp(200, 0, '成功', response)

    @swag_from('short_url_post.yml', endpoint='surl_post')
    def post(self):
        args = parser.parse_args()
        print(args['source'])
        short = short_url.shorturl(args['source'])
        response = {
            "short": "http://localhost:5000/surl/" + short
        }
        from app import redis_client
        bool = redis_client.set(short, args['source'])
        if bool:
            return BaseResp(200, 0, '成功', response)
        else:
            abort(503)


class Working(Resource):

    @marshal_with(resource_fields)
    @swag_from('work_get.yml', endpoint='work_get')
    def get(self, date):
        from app.model import DateModel
        date_model = DateModel.query.filter_by(date=date).first()
        response = {
            "date": date_model.date.strftime("%Y-%m-%d"),
            "isWork": date_model.isWork
        }
        return BaseResp(200, 0, '成功', response)

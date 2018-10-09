# -*- coding: UTF-8 -*-

from dao.base_dao import BaseDAO


class OrderDAO(BaseDAO):
    columns = ['id', 'status', 'biz', 'realname', 'nickname', 'headimgurl', 'mobile',
               'address', 'lon', 'lat', 'installtime']
    table = "`order`"

# -*- coding: UTF-8 -*-

import logging

import flask

from dao.biz import BizDAO
from dao.operator import OperatorDAO
from dao.bizproperty import BizPropertyDAO

from blueprints.public.pages import pages

logger = logging.getLogger(__name__)


@pages.route('/bizs/<int:bizid>')
def biz_review(bizid):
    try:
        biz = BizDAO.first_or_default(id=bizid)

        if biz is None:
            return flask.render_template('404.html', message='套餐不存在'), 404

        operator = OperatorDAO.first_or_default(id=biz['operator'])
        properties = BizPropertyDAO.all(biz=bizid)

        biz['operatorname'] = operator['name']
        biz['properties'] = {p['name']: p for p in properties}

        return flask.render_template('bizpreview.html', biz=biz)

    except:
        logger.exception('套餐预览页面异常 %d', bizid)
        return flask.render_template('500.html'), 500
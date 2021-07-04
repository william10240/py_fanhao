#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
import json as sjson
import os,shutil,logging

from aiohttp import web

#from smb.SMBConnection import SMBConnection

__author__ = 'SunCoder'

APP_PATH = os.path.dirname(os.path.abspath(__file__))
PHOTO_PATH = os.path.join(APP_PATH, 'data/photos')
STATIC_PATH = os.path.join(APP_PATH, 'static')

CONFIGBASE = os.path.join(APP_PATH, 'config.ini.base')
CONFIG = os.path.join(APP_PATH, 'config.ini')


"""
读取配置文件信息
"""

def getconfig(sector,item):
    if not os.path.exists(CONFIG):
        shutil.copyfile(CONFIGBASE, CONFIG)
        logging.info("con`t find conf.ini, use the default config")
    cf = configparser.ConfigParser()
    cf.read(CONFIG, encoding='utf8')  # 注意ini配置文件的路径
    value = cf.get(sector, item)
    return value


def json(code, msg='', data='', callback=None):
    json_data = {
        'code': code,
        'msg': msg,
        'data': data
    }
    return json_data

def jsonres(code, msg='', data='', callback=None):
    json_data = {
        'code': code,
        'msg': msg,
        'data': data
    }
    jsonstr = sjson.dumps(json_data)
    return web.Response(body=bytes(jsonstr, encoding="utf-8"),content_type='text/html')

class Pager():
    url = ''
    total = 0
    index = 1
    size = 15
    pages = []

    def __init__(self, total, index, size):
        '''
        分页函数
        :param count: 总数
        :param index: 页码
        :param size: 页容量
        :return: object paging
        '''
        self.total = total
        self.index = index
        self.size = size
        self.count, tail = divmod(total, size)
        if tail != 0:
            self.count += 1

    def render(self):

        self.pages.clear()
        self.pages.append('<nav><ul class="pagination">')

        rag = range(0, self.count)
        if self.count > 10:
            if self.index <= 5:
                rag = rag[0: 10]
            elif self.index > 5:
                if self.count - self.index < 5:
                    rag = rag[-10:]
                else:
                    rag = rag[self.index - 5:self.index + 5]

        if self.index == 1:
            self.pages.append('<li class="disabled"><span>第1页</a></li>')
            self.pages.append('<li class="disabled"><span>&laquo;&laquo;&laquo;</a></li>')
        else:
            self.pages.append('<li><a href="javascript:goPage(%s);">第1页</a></li>' % 1)
            self.pages.append('<li><a href="javascript:goPage(%s);">&laquo;&laquo;&laquo;</a></li>' % (self.index - 1))

        for i in rag:
            v = i + 1
            if self.index == v:
                self.pages.append('<li class="active"><span>%s</span></li>' % (v if v > 9 else ('0%s' % v)))
            else:
                self.pages.append('<li><a href="javascript:goPage(%s);">%s</a></li>' % (v, (v if v > 9 else ('0%s' % v))))

        if self.index == self.count:
            self.pages.append('<li class="disabled"><span>&raquo;&raquo;&raquo;</span></li>')
            self.pages.append('<li class="disabled"><span>第%s页</span></li>' % self.count)
        else:
            self.pages.append('<li><a href="javascript:goPage(%s);">&raquo;&raquo;&raquo;</a></li>' % (self.index + 1))
            self.pages.append('<li><a href="javascript:goPage(%s);">第%s页</a></li>' % (self.count, self.count))

        self.pages.append('<li><span>共%s个</span></li></ul></nav>' % self.total)
        return "".join(self.pages)

    def __str__(self):
        return self.render()


if __name__ == '__main__':
    # print(Pager(202, 10, 4))
    # print(Pager(202, 2, 4))
    # print(Pager(202, 50, 4))
    # print(Pager(10, 2, 3))
    # print(Pager(10, 3, 3))
    print(os.path.join(APP_PATH,'config.ini'))
    print(getconfig('db', 'host'))
    print(getconfig('db', 'user'))
    print(getconfig('db', 'passwd'))
    print(getconfig('db', 'database'))
    print(getconfig('db', 'charset'))
    print(getconfig('db', 'port'))

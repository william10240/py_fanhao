#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SunCoder'

import time,os
from peewee import Model,PrimaryKeyField,CharField,CharField,IntegerField
from Base import getconfig, APP_PATH

# from peewee import MySQLDatabase
# db = SqliteDatabase(host=getconfig('db', 'host'),
#                    user=getconfig('db', 'user'),
#                    passwd=getconfig('db', 'passwd'),
#                    database=getconfig('db', 'database'),
#                    charset=getconfig('db', 'charset'),
#                    port=int(getconfig('db', 'port'))
#                 )

from peewee import SqliteDatabase
db = SqliteDatabase(os.path.join(APP_PATH, 'data/fan.db'))


class BaseModel(Model):
    class Meta:
        database = db

class fanhao(BaseModel):
    id = PrimaryKeyField(primary_key=True)
    code = CharField(64)
    title = CharField(128)
    star = CharField(64,null=True)
    starcode = CharField(64,null=True)
    img = CharField(128,null=True)
    fname = CharField(128,null=True)
    ima = IntegerField(default=0)
    iface = IntegerField(default=0)
    starnum = IntegerField(default=0)
    updateTime = IntegerField(default=int(time.time()))
    downed = IntegerField(default=0)


if __name__ == '__main__':
    # print(dir(fanhao._meta))
    # print('fanhao的类型是:',type(fanhao._meta.database))
    # print('是MySQLDatabase吗:',isinstance(fanhao._meta.database,MySQLDatabase))
    # print('是SqliteDatabase吗:',isinstance(fanhao._meta.database,SqliteDatabase))
    # print('数据表是否存在:',fanhao.table_exists())
    # if not fanhao.table_exists():
    #     print('开始创建数据表')
    #     fanhao.create_table()
    # print('再次检测数据表是否存在:',fanhao.table_exists())
    print(fanhao.table_exists())
    # ps = fanhao.select()
    # for p in ps:
        # print(p)
    # print(ps.count())
    #fanhao.create_table()

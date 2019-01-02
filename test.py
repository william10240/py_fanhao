#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
"""
读取配置文件信息
"""

class ConfigParser():

    config_dic = {}
    @classmethod
    def get_config(cls, sector, item):
        value = None
        try:
            value = cls.config_dic[sector][item]
        except KeyError:
            cf = configparser.ConfigParser()
            cf.read('config.ini', encoding='utf8')  #注意setting.ini配置文件的路径
            value = cf.get(sector, item)
            cls.config_dic = value
        finally:
            return value


if __name__ == '__main__':
    con = ConfigParser()
    res = con.get_config('db', 'host')
    print(res)

